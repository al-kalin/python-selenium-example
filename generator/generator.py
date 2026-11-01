from faker import Faker
from data.data import Person



faker_en = Faker("en")
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_adress=faker_en.address(),
    )
