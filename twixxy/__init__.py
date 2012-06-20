import twiggy

log = twiggy.log.name('twixxy')
log.min_level = twiggy.levels.DISABLED

__all__ = ('TwiggyLoggingObserver', 'observerFactory', 'log')

from twixxy.observer import TwiggyLoggingObserver, observerFactory
## appease pyflakes
(TwiggyLoggingObserver, observerFactory)
