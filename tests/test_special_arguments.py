import os.path
import unittest

from simple_dependency_injector import DependencyInjector


class TestSpecialArguments(unittest.TestCase):
    def setUp(self):
        self.injector = DependencyInjector(base_path=os.path.dirname(os.path.dirname(__file__)))

    def test_get_dependency_injector(self):
        self.injector.load("tests/config/services.yaml")
        self.injector.compile()
        service = self.injector.get("another_service")
        self.assertEqual(service.context, self.injector)

    def test_get_context(self):
        self.injector.load("tests/config/services.yaml")
        self.injector.compile()
        context = self.injector.create_context()
        service = context.get("another_service")
        self.assertEqual(service.context, context)

    def test_get_other_service(self):
        self.injector.load("tests/config/services.yaml")
        self.injector.compile()
        service = self.injector.get("another_service")
        self.assertEqual(service.name, "Another Service")
        self.assertEqual(service.core.name, "Core Service")

    def test_get_tag_list(self):
        self.injector.load("tests/config/services.py")
        self.injector.compile()
        service = self.injector.get("another_service")
        self.assertEqual(service.name, "Another Service")
        self.assertEqual(service.services[0].name, "Core Service")
        self.assertEqual(service.services[1].name, "Base Service")

    def test_load_json_class_service(self):
        self.injector.load("tests/config/services.json")
        self.injector.compile()
        service = self.injector.get("my_service")
        self.assertEqual(service.name, "Service")


if __name__ == "__main__":
    unittest.main()
