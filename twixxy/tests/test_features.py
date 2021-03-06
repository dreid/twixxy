import twiggy

from twisted.trial.unittest import TestCase
from twisted.web.server import Request
from twisted.web.test.test_web import DummyChannel

from twisted.python.failure import Failure

from twixxy.features.request import request
from twixxy.features.failure import failure

from twixxy.tests.utils import stringIOTwiggySetup


class FeatureTests(TestCase):
    def setUp(self):
        self.out = stringIOTwiggySetup()
        self.log = twiggy.log.name('feature_tests')

    def test_requestFeature(self):
        self.log.addFeature(request)
        req = Request(DummyChannel(), False)
        req.method = 'GET'
        req.uri = '/foo'

        self.log.request(req).info('handling request')
        self.assertIn('method=GET', self.out.getvalue())
        self.assertIn('uri=/foo', self.out.getvalue())

    def test_failureFeature(self):
        self.log.addFeature(failure)

        try:
            1 / 0
        except:
            f = Failure()
            self.log.failure(f).error('got a failure')

        self.assertIn('ERROR:feature_tests:got a failure', self.out.getvalue())
        self.assertIn('TRACE ZeroDivisionError', self.out.getvalue())
