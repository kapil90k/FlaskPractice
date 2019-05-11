import json


class Contact:
    def __init__(self):
        self.prime_count = 9876
        self.second_count = 6789


class Address:
    def __init__(self):
        self.pupulation = 120000
        self.city = 'Agra'
        self.count = Contact()


class Person():
    def __init__(self):
        self.name = 'John'
        self.age = 25
        self.id = 1

    def __init__(self, name, age, id, address):
        self.name = name
        self.age = age
        self.id = id
        self.address = address


def gettingPerson():
    address = Address()
    person = Person('Kapil', 27, 1022, address)
    person_json = json.dumps(person.__dict__, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return person_json


def gettingCustPerson(name, age, id):
    address = Address()
    person = Person(name, age, id, address)
    person_json = json.dumps(person.__dict__, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return person_json