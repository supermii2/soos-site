from django.db import models

CHAR_FIELD_MAX_SIZE = 50

class PokemonTyping(models.Model):
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=CHAR_FIELD_MAX_SIZE)
    slug = models.CharField(max_length=CHAR_FIELD_MAX_SIZE)

    def __str__(self):
        return self.name
    
class PokemonTypingEffectiveness(models.Model):
    EFFECTIVE_CHOICES = [
        (1.0, 'Effective'),
        (2.0, 'Super Effective'),
        (0.5, 'Not Very Effective'),
        (0.0, 'No Effect'),
    ]
        
    attacking_type = models.ForeignKey(PokemonTyping, on_delete=models.CASCADE, related_name='attacking_type')
    defending_type = models.ForeignKey(PokemonTyping, on_delete=models.CASCADE, related_name='defending_type')
    effectiveness = models.DecimalField(max_digits=2, decimal_places=1, choices=EFFECTIVE_CHOICES)

class PokemonAbility(models.Model):
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=CHAR_FIELD_MAX_SIZE)
    slug = models.CharField(max_length=CHAR_FIELD_MAX_SIZE)
    desc = models.TextField()

    def serialize(self):
        return {
            "id" : self.num,
            "name" : self.name,
            "desc" : self.desc,
        }

    def __str__(self):
        return self.name

class PokemonSpecies(models.Model):
    dex_num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=CHAR_FIELD_MAX_SIZE)
    slug = models.CharField(max_length=CHAR_FIELD_MAX_SIZE)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_SIZE)
    slug = models.CharField(max_length=CHAR_FIELD_MAX_SIZE, primary_key=True)

    species = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    type1 = models.ForeignKey(PokemonTyping, on_delete=models.CASCADE, related_name='pokemon_type1')
    type2 = models.ForeignKey(PokemonTyping, on_delete=models.CASCADE, related_name='pokemon_type2', null=True)

    ability1 = models.ForeignKey(PokemonAbility, on_delete=models.CASCADE, related_name='pokemon_abil1')
    ability2 = models.ForeignKey(PokemonAbility, on_delete=models.CASCADE, related_name='pokemon_abil2', null=True)
    abilityhidden = models.ForeignKey(PokemonAbility, on_delete=models.CASCADE, related_name='pokemon_abil_hidden', null=True)

    stathp = models.IntegerField()
    statatk = models.IntegerField()
    statdef = models.IntegerField()
    statspa = models.IntegerField()
    statspd = models.IntegerField()
    statspe = models.IntegerField()

    form_num = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
        "name": self.name,
        "type": [
            self.type1.__str__(),
            self.type2.__str__() if self.type2 is not None else None,
        ],
        "abilities": {
            "1": self.ability1.__str__(),
            "2": self.ability2.__str__() if self.ability2 is not None else None,
            "H": self.abilityhidden.__str__() if self.abilityhidden is not None else None,
        },
        "stats": {
            "hp": self.stathp,
            "atk": self.statatk,
            "def": self.statdef,
            "spa": self.statspa,
            "spd": self.statspd,
            "spe": self.statspe,
        }
    }

class PokemonGame(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_SIZE)
    slug = models.CharField(max_length=CHAR_FIELD_MAX_SIZE)

class PokedexEntry(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    game = models.ForeignKey(PokemonGame, on_delete=models.CASCADE)
    text = models.TextField()

    @classmethod
    def add_entry(cls, pokemon, game, text):
        x = PokedexEntry.objects.create(
            pokemon=Pokemon.objects.get(slug=pokemon),
            game=PokemonGame.objects.get(slug=game),
            text=text
        )
        x.save()

