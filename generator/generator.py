import random

from data.data import Person
from faker import Faker


faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
                full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
                firstname=faker_ru.first_name(),
                lastname=faker_ru.last_name(),
                age=str(random.randint(18, 70)),
                department=faker_ru.job(),
                salary=str(random.randint(300, 1000)),
                email=faker_ru.email(),
                current_address=faker_ru.address(),
                permanent_address=faker_ru.address()
                )


def generated_file():
    path = rf'C:\autotest_framework\filetest{random.randint(0, 999)}.txt'

    file = open(path, 'w+')
    file.write(f'Hello Everyone')
    file.close()
    return file.name, path