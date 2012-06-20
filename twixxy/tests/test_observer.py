import time
from StringIO import StringIO

import mock
import twiggy

from twisted.trial.unittest import TestCase
from twisted.python import log, failure

from twixxy import TwiggyLoggingObserver


class TwiggyLoggingObserverTests(TestCase):
    def setUp(self):
        self.out = StringIO()

        twiggy.addEmitters((
            '*',
            twiggy.levels.DEBUG,
            True,
            twiggy.outputs.StreamOutput(twiggy.formats.line_format, stream=self.out)
        ))

        self.lp = log.LogPublisher()
        self.obs = TwiggyLoggingObserver()

        self.lp.addObserver(self.obs.emit)

    def test_singleString(self):
        """
        Test simple output
        """
        self.lp.msg("Hello, world.")
        self.assertIn("Hello, world.", self.out.getvalue())
        self.assertIn("INFO", self.out.getvalue())

    def test_errorString(self):
        """
        Test error output.
        """
        self.lp.msg(failure=failure.Failure(ValueError("That is bad.")), isError=True)
        self.assertIn("ERROR", self.out.getvalue())

    def test_formatString(self):
        """
        Test logging with a format.
        """
        self.lp.msg(format="%(bar)s oo %(foo)s", bar="Hello", foo="world")
        self.assertIn("Hello oo world", self.out.getvalue())

    @mock.patch('twixxy.observer.time.localtime')
    def test_logTime(self, localtime):
        """
        Test logging with a time.
        """
        localtime.return_value = time.gmtime(0)
        self.lp.msg('hello')
        self.assertIn('1970-01-01T00:00:00Z', self.out.getvalue())

    def test_failureWithReason(self):
        """
        Test error output with failure and reason.
        """
        self.lp.msg(failure=failure.Failure(ValueError("This is bad")), isError=True, why="Really Bad")
        self.assertIn('ERROR', self.out.getvalue())
        self.assertIn('Really Bad', self.out.getvalue())
        self.assertIn('TRACE ValueError: This is bad', self.out.getvalue())

    def test_systemAsLoggerName(self):
        """
        system should be used as the log name.
        """
        self.lp.msg('hello', system='twixxy_tests')
        self.assertIn('hello', self.out.getvalue())
        self.assertIn('twixxy_tests', self.out.getvalue())

    def test_logsFields(self):
        """
        Extra keyword arguments passed to log.msg should be passed to twiggy.log.fields.
        """
        self.lp.msg('hello', where='there')
        self.assertIn('where=there', self.out.getvalue())

    def test_userSpecifiedLevel(self):
        """
        Logging with a logLevel argument invokes appropriate logger methods.
        """
        self.lp.msg('hello', logLevel=twiggy.levels.DEBUG)
        self.assertIn('DEBUG', self.out.getvalue())
