import unittest
import os.path

from dependency_injector.dependency_injector import DependencyInjector


class TestInstanceServices(unittest.TestCase):
    def setUp(self):
        self.injector = DependencyInjector(base_path=os.path.dirname(os.path.dirname(__file__)))

    def test_load_yaml_instance_service(self):
        self.injector.load("tests/config/services.yaml")
        self.injector.compile()
        instance = self.injector.get("my_instance_service")
        self.assertEqual(instance.name, "Instance")

    def test_load_python_instance_service(self):
        self.injector.load("tests/config/services_python.py")
        self.injector.compile()
        instance = self.injector.get("my_instance_service")
        self.assertEqual(instance.name, "Instance")


if __name__ == "__main__":
    unittest.main()
