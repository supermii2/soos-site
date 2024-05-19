from django.core.management.base import BaseCommand
from django.contrib.staticfiles import finders
from app_pokedata.models import PokemonTyping, PokemonAbility, PokemonSpecies, Pokemon
import csv

pattern = r'[^a-zA-Z0-9]'

class Command(BaseCommand):
    help = 'Seeds data'  # Help text displayed with `--help`

    
    def handle(self, *args, **options):
        with open(finders.find('PokemonTyping.csv'), mode='r', newline='') as file:
            PokemonTyping.objects.all().delete()

            reader = csv.DictReader(file)
            headers = reader.fieldnames

            for row in reader:
                PokemonTyping.objects.create(
                    num=row['num'],
                    name=row['name'],
                    slug=row['slug'],
                )

        with open(finders.find('PokemonAbility.csv'), mode='r', newline='') as file:
            PokemonAbility.objects.all().delete()

            reader = csv.DictReader(file)
            headers = reader.fieldnames

            for row in reader:
                PokemonAbility.objects.create(
                    num=int(row['num']),
                    name=row['name'],
                    slug=row['slug'],
                    desc=row['desc'],
                )

        with open(finders.find('PokemonSpecies.csv'), mode='r', newline='') as file:
            PokemonSpecies.objects.all().delete()

            reader = csv.DictReader(file)
            headers = reader.fieldnames

            for row in reader:
                PokemonSpecies.objects.create(
                    dex_num=int(row['dex_num']),
                    name=row['name'],
                    slug=row['slug'],
                )

        with open(finders.find('Pokemon.csv'), mode='r', newline='') as file:
            Pokemon.objects.all().delete()

            reader = csv.DictReader(file)
            headers = reader.fieldnames

            for row in reader:
                Pokemon.objects.create(
                    name=row['name'],
                    slug=row['slug'],
                    species=PokemonSpecies.objects.get(slug=row['base']),
                    type1=PokemonTyping.objects.get(slug=row['type1']),
                    type2=PokemonTyping.objects.get(slug=row['type2']) if row['type2'] != "" else None,
                    ability1=PokemonAbility.objects.get(slug=row['abil1']),
                    ability2=PokemonAbility.objects.get(slug=row['abil2']) if row['abil2'] != "" else None,
                    abilityhidden=PokemonAbility.objects.get(slug=row['abilh']) if row['abilh'] != "" else None,
                    stathp=int(row['hp']),
                    statatk=int(row['atk']),
                    statdef=int(row['def']),
                    statspa=int(row['spa']),
                    statspd=int(row['spd']),
                    statspe=int(row['spe']),
                    form_num=int(row['form_num']) if row['form_num'] != "" else None,
                )