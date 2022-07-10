#!/usr/bin/env python3
import ipdb

class Dog:
    breeds = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
        ]

    def get_name(self):
        pass
        return self._name

    def set_name(self, name):
        pass
        if (type(name) == (str)) and (1 <= len(name) <= 25):
            self._name = name
        
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        pass
        return self._breed

    def set_breed(self, breed):
        pass
        if (breed in self.breeds):
            pass
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

fido = Dog()
# ipdb.set_trace()