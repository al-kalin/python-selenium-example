"""
Module for generating test data and temporary files.
"""

from pathlib import Path

import random

from faker import Faker
from data.data import Person

faker_en = Faker("en")
Faker.seed()


def generated_person():
    """
    Generate random person data using Faker and random values.

    Creates and returns a Person object containing randomly generated
    personal information, contact details, and employment data.

    Generated fields:
        - Full name
        - First name
        - Last name
        - Age (16–80)
        - Salary (1000–5000)
        - Email
        - Department
        - Current address
        - Permanent address

    Yields:
        Person: A Person object populated with randomly generated data.
    """

    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        age=random.randint(16, 80),
        salary=random.randint(1000, 5000),
        email=faker_en.email(),
        department=faker_en.company(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
    )


def generated_file():
    """
    Generate a temporary text file with random content.

    Creates a file in the project's temp directory, writes random
    text into it, and returns the file name and its full path.

    Returns:
        tuple: File name and full path to the generated file.
    """
    path = (
        Path(__file__).resolve().parent.parent
        / "temp"
        / f"file_test{random.randint(0, 999)}.txt"
    )
    file = open(path, "w+")
    file.write(f"Hello world {random.randint(0, 999)}")
    file.close()
    return file.name
