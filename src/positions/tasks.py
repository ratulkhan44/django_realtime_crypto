from django_crypto.celery import app
from .models import Test, Position
from .utils import get_random_code
import requests


# def create_test_object(name):
#     Test.objects.create(name=name)


# def create_all_codes():
#     for test in Test.objects.all():
#         test.code = get_random_code()
#         test.save()


def get_crypto_data():
    URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(URL).json()

    for item in data:
        p, _ = Position.objects.get_or_create(name=item['name'])
        p.image = item['image']
        p.price = item['current_price']
        p.rank = item['market_cap_rank']
        p.market_cap = item['market_cap']
        p.save()


@app.task
def get_crypto_current():
    get_crypto_data()


# @app.task
# def run_create_objs():
#     create_test_object(name="Ratul")
