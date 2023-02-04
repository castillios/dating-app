import random

class Profile():
    def __init__(self, name, age, occ, tagline):
        self.name = name
        self.age = age
        self.occ = occ
        self.tagline = tagline
        self.match_chance = random.random()
    

    def get_info(self) -> dict:
        db = {'name'    : self.name,
              'age'     : self.age,
              'occ'     : self.occ,
              'tagline' : self.tagline}

        return db

    def update_info(self, n_name=None, n_age=None, n_occ=None, n_tagline=None):
        if n_name != None:
            self.name = n_name
        if n_age != None:
            self.age = n_age
        if n_occ != None:
            self.occ = n_occ
        if n_tagline != None:
            self.tagline = n_tagline
