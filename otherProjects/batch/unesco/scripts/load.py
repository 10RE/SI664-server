import csv
from unicodedata import category  # https://docs.python.org/3/library/csv.html
import pandas as pd

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, Site, Region, State, Iso




def run():
    df = pd.read_csv('unesco/whc-sites-2018-clean.csv')
    #fhand = open('unesco/whc-sites-2018-clean.csv')
    #reader = csv.reader(fhand)
    #next(reader)  # Advance past the header

    Category.objects.all().delete()
    Site.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()

    def save_row(row):
        print(row)
        category, _ = Category.objects.get_or_create(name=row['category'])
        category.save()
        region, _ = Region.objects.get_or_create(name=row['region'])
        region.save()
        state, _ = State.objects.get_or_create(name=row['state'])
        state.save()
        iso, _ = Iso.objects.get_or_create(name=row['iso'])
        iso.save()
        site = Site(name=row['name'], 
            description=row['description'], 
            justification=row['justification'],
            year=row['year'],
            longitude=row['longitude'],
            latitude=row['latitude'],
            area_hectares=row['area_hectares'],
            category=category,
            region=region,
            state=state,
            iso=iso
        )
        site.save()

    df.apply(save_row, axis=1)