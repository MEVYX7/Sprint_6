from faker import Faker
import random

fake = Faker("ru_RU")


class Utils:
    @staticmethod
    def generate_name():
        return fake.first_name()

    @staticmethod
    def generate_last_name():
        return fake.last_name()

    @staticmethod
    def generate_address():
        return f"Москва, ул. {fake.street_name()}, д. {random.randint(1, 200)}"

    @staticmethod
    def generate_phone_number():
        return f"89{random.randint(100000000, 999999999)}"
