import unittest
import os.path

from simple_dependency_injector import DependencyInjector


class TestImportedServices(unittest.TestCase):
    def setUp(self):
        self.injector = DependencyInjector(base_path=os.path.dirname(os.path.dirname(__file__)))

    def test_load_yaml_imported_service(self):
        self.injector.load("tests/config/services.yaml")
        self.injector.compile()
        another_service = self.injector.get("another_service")
        self.assertEqual(another_service.name, "Another Service")

    def test_load_python_imported_service(self):
        self.injector.load("tests/config/services_python.py")
        self.injector.compile()
        another_service = self.injector.get("another_service")
        self.assertEqual(another_service.name, "Another Service")


if __name__ == "__main__":
    unittest.main()
