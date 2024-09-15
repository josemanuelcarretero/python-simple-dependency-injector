import os.path
import unittest

from simple_dependency_injector import DependencyInjector


class TestFailures(unittest.TestCase):
    def setUp(self):
        self.injector = DependencyInjector(base_path=os.path.dirname(os.path.dirname(__file__)))

    def test_invalid_class_yaml(self):
        with self.assertRaises(AttributeError) as context:
            self.injector.load("tests/config/invalid_class.yaml")
            self.injector.compile()
            self.injector.get("invalid_class")
        self.assertEqual(
            "module 'module.name' has no attribute 'NonExistentClass'",
            str(context.exception),
        )

    def test_invalid_factory_method_yaml(self):
        with self.assertRaises(AttributeError) as context:
            self.injector.load("tests/config/invalid_factory_method.yaml")
            self.injector.compile()
            self.injector.get("invalid_factory_method")
        self.assertEqual(
            "type object 'MyFactory' has no attribute 'non_existent_method'",
            str(context.exception),
        )

    def test_missing_class_parameter_yaml(self):
        with self.assertRaises(ValueError) as context:
            self.injector.load("tests/config/missing_class_parameter.yaml")
            self.injector.compile()
            self.injector.get("missing_class_parameter")
        self.assertEqual(
            "Service 'missing_class_parameter' has an invalid class name: 123",
            str(context.exception),
        )

    def test_invalid_scope_yaml(self):
        with self.assertRaises(ValueError) as context:
            self.injector.load("tests/config/invalid_scope.yaml")
            self.injector.compile()
            self.injector.get("invalid_scope")
        self.assertEqual(
            "Service 'invalid_scope' has an invalid scope: invalid_scope",
            str(context.exception),
        )

    def test_missing_instance_parameter_yaml(self):
        with self.assertRaises(ValueError) as context:
            self.injector.load("tests/config/missing_instance_parameter.yaml")
            self.injector.compile()
            self.injector.get("missing_instance_parameter")
        self.assertEqual(
            "Service 'missing_instance_parameter' has an invalid instance: 123",
            str(context.exception),
        )


if __name__ == "__main__":
    unittest.main()
