import sys
import time
import twiggy

from twixxy import log

from twisted.python.log import addObserver, textFromEventDict


log = log.name('twixxy.observer')
log.min_level = twiggy.levels.DISABLED


def observerFactory():
    twiggy.addEmitters((
        '*',
        twiggy.levels.DEBUG,
        True,
        twiggy.outputs.StreamOutput(twiggy.formats.line_format, stream=sys.stdout)
    ))
    log.debug('observerFactory used to setup logging')
    return TwiggyLoggingObserver().emit


class TwiggyLoggingObserver(object):
    def __init__(self, loggerName=None):
        loggerName = loggerName or 'twisted'
        log.fields(loggerName=loggerName).debug('Created TwiggyLoggingObserver')
        self._logger = twiggy.log.name(loggerName)

    def start(self):
        log.debug('start called, adding emit as observer')
        addObserver(self.emit)

    def emit(self, eventDict):
        log.fields(eventDict=eventDict).debug('emit called')
        try:
            self._emit(eventDict)
        except:
            log.trace().error('Error logging message.')

    def _emit(self, eventDict):
        l = self._logger

        text = textFromEventDict(eventDict)
        isError = eventDict.get('isError', False)
        failure = eventDict.get('failure', None)
        why = eventDict.get('why', None)

        if eventDict.get('time'):
            eventDict['time'] = time.localtime(eventDict['time'])

        if eventDict['system'] != '-':
            l = l.name(eventDict['system'])

        filteredFields = ['message', 'format', 'isError',
                          'failure', 'why', 'printed', 'system']
        for field in filteredFields:
            eventDict.pop(field, None)

        l = l.fields(**eventDict)

        if isError:
            if failure:
                l = l.trace((failure.type, failure.value, failure.tb))
            if why:
                l.error(why)
            else:
                l.error(text)
        else:
            l.info(text)
