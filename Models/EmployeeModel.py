import json


class Employee:
    def __init__(self, name, state, voter):
        self.name = name,
        self.state = state,
        self.voter = voter


def generate_response(payload):
    age = payload.get('age', 25)
    city = payload.get('address').get('city')
    name = payload.get('name', 'Default')

    state = state_dictionary(city)
    voter = eligible_voter(age)

    emp = Employee(name, state, voter)
    response = json.dumps(emp.__dict__, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return response


def state_dictionary(city):
    state = {
        'Agra': 'Uttar Pradesh',
        'Bangalore': 'Karnatak',
        'Chennai': 'Tamilnadu',
        'Kanyakumari': 'Kerala'
    }
    return state.get(city, 'Default')


def eligible_voter(age):
    if age >= 18:
        return 'Yes'
    else:
        return 'No'
