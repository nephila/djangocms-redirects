from app_helper.base_test import BaseTestCase
from django.core.cache import cache


class BaseRedirectTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        cache.clear()
