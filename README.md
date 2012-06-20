twixxy
======

twixxy - twiggy + twisted

twixxy consists primarily of twisted log observer which can installed to forward
calls to `log.msg` and `log.err` to the appropriate Twiggy log methods.

Using with twistd
~~~~~~~~~~~~~~~~~

twixxy provides a log observer factory compatible with `twistd --logger`.

::
    > twistd --logger=twixxy.observerFactory -n web --path=.
    2012-06-19T22:09:43Z:INFO:twisted:Log opened.
    2012-06-19T22:09:43Z:INFO:twisted:twistd 12.1.0 (/Users/dreid/.virtualenvs/twixxy/bin/python 2.7.1) starting up.
    2012-06-19T22:09:43Z:INFO:twisted:reactor class: twisted.internet.selectreactor.SelectReactor.
    2012-06-19T22:09:43Z:INFO:twisted:Site starting on 8080
    2012-06-19T22:09:43Z:INFO:twisted:Starting factory <twisted.web.server.Site instance at 0x10b718fc8>

Replacing Twisted's Logging without twistd.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

example.py::
    import sys
    import twiggy
    from twisted.python import log
    from twixxy import TwiggyLoggingObserver

    twiggy.quickSetup(file=sys.stdout)
    observer = TwiggyLoggingObserver('example')
    log.startLoggingWithObserver(observer.emit)

    log.msg('Hello, World!')

Using in conjunction with Twisted's logging.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

example2.py::
    import sys
    import twiggy
    from twisted.python import log
    from twixxy import TwiggyLoggingObserver

    twiggy.quickSetup(file='twiggy.log')
    observer = TwiggyLoggingObserver('example2')
    observer.start()
    log.startLogging(sys.stdout)

    log.msg('Hello, World!')


