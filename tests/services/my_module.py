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


class AnotherService:
    def __init__(self):
        self.name = "Another Service"
