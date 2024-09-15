import unittest
import os.path

from dependency_injector.dependency_injector import DependencyInjector


class TestContexts(unittest.TestCase):
    def setUp(self):
        self.injector = DependencyInjector(base_path=os.path.dirname(os.path.dirname(__file__)))

    def test_create_context(self):
        self.injector.load("tests/config/services_python.py")
        self.injector.compile()
        context = self.injector.create_context()

        service = context.get("my_service")
        self.assertEqual(service.name, "Service")


if __name__ == "__main__":
    unittest.main()
