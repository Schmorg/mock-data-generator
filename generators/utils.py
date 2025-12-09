from faker import Faker

faker = Faker()

def random_id():
    return faker.uuid4()

def random_name():
    return faker.name()

def random_date():
    return faker.date_between(start_date="-1y", end_date="today").isoformat()

def random_future_date():
    return faker.date_between(start_date="today", end_date="+6m").isoformat()

def random_status(options):
    return faker.random_element(options)
