from faker import Faker
import random

fake = Faker()

def generate_booking(totalprice, depositpaid, additionalneeds):
    checkin = fake.date_between(start_date="today", end_date="+5d").isoformat()
    checkout = fake.date_between(start_date="+6d", end_date="+10d").isoformat()

    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }
