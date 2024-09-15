from typing import Any, List


class MyService:
    def __init__(self):
        self.name = "Service"


class MyFactory:
    @staticmethod
    def create_service():
        return MyService()


class MyInstanceGenerator:
    def __init__(self):
        self.name = "Instance"


MyInstance = MyInstanceGenerator()


class CoreService:
    def __init__(self):
        self.name = "Core Service"


class BaseService:
    def __init__(self):
        self.name = "Base Service"


class AnotherService:
    def __init__(self, core: CoreService, services: List[Any], context: Any):
        self.name = "Another Service"
        self.core = core
        self.services = services
        self.context = context
