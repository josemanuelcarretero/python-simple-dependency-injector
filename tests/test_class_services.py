import os.path
import unittest

from simple_dependency_injector import DependencyInjector


class TestClassServices(unittest.TestCase):
    def setUp(self):
        self.injector = DependencyInjector(base_path=os.path.dirname(os.path.dirname(__file__)))

    def test_load_yaml_class_service(self):
        self.injector.load("tests/config/services.yaml")
        self.injector.compile()
        service = self.injector.get("my_service")
        self.assertEqual(service.name, "Service")

    def test_load_python_class_service(self):
        self.injector.load("tests/config/services_python.py")
        self.injector.compile()
        service = self.injector.get("my_service")
        self.assertEqual(service.name, "Service")


if __name__ == "__main__":
    unittest.main()
