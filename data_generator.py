import random
from datetime import datetime, timedelta

def generate_cyrillic_surname(length=8):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    return ''.join(random.choice(cyrillic) for _ in range(length)).title()

def generate_phone_number():
    return ''.join(str(random.randint(0, 9)) for _ in range(11))

def generate_tomorrow_date():
    tomorrow = datetime.now() + timedelta(days=1)
    return tomorrow.strftime("%d.%m.%Y")

def generate_date():
    tomorrow = datetime.now() + timedelta(days=3)
    return tomorrow.strftime("%d.%m.%Y")