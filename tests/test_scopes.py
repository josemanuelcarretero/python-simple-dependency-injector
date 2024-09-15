import os.path
import unittest

from simple_dependency_injector import DependencyInjector


class TestScopes(unittest.TestCase):
    def setUp(self):
        self.injector = DependencyInjector(base_path=os.path.dirname(os.path.dirname(__file__)))

    def test_singleton_scope(self):
        self.injector.load("tests/config/services.yaml")
        self.injector.compile()

        service1 = self.injector.get("my_service")
        service2 = self.injector.get("my_service")

        self.assertIs(service1, service2)

    def test_request_scope(self):
        self.injector.load("tests/config/services.yaml")
        self.injector.compile()

        service1 = self.injector.get("my_factory_service")
        service2 = self.injector.get("my_factory_service")

        self.assertIsNot(service1, service2)

    def test_transient_scope(self):
        self.injector.load("tests/config/services_python.py")
        self.injector.compile()

        service1 = self.injector.get("my_factory_service")
        service2 = self.injector.get("my_factory_service")

        self.assertIsNot(service1, service2)

    def test_ambivalent_scope(self):
        self.injector.load("tests/config/services_python.py")
        self.injector.compile()

        service1 = self.injector.get("my_factory_service")
        service2 = self.injector.get("my_factory_service")

        self.assertIsNot(service1, service2)


if __name__ == "__main__":
    unittest.main()
