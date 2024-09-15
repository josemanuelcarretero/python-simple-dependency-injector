import os.path
import unittest

from simple_dependency_injector import DependencyInjector


class TestContexts(unittest.TestCase):
    def setUp(self):
        self.injector = DependencyInjector(base_path=os.path.dirname(os.path.dirname(__file__)))

    def test_create_context(self):
        self.injector.load("tests/config/services.yaml")
        self.injector.compile()
        context1 = self.injector.create_context()
        context2 = self.injector.create_context()

        service1 = context1.get("my_service")
        service2 = context2.get("my_service")

        self.assertEqual(service1.name, "Service")
        self.assertEqual(service2.name, "Service")
        self.assertNotEqual(service1, service2)


if __name__ == "__main__":
    unittest.main()
