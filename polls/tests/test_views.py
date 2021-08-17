from djangotestpatterns.test import TestCase


class TestIndexView(TestCase):
    def test_better_status(self):
        response = self.get("")
        self.assert_http_200_ok(response)
