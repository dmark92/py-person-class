class Person:
    # class attribute to store all persons by name
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # register person in class dictionary
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    # 1. create all Person instances
    for data in people:
        person = Person(data["name"], data["age"])
        result.append(person)

    # 2. add wife / husband links
    for data in people:
        person = Person.people[data["name"]]

        if "wife" in data and data["wife"] is not None:
            person.wife = Person.people[data["wife"]]

        if "husband" in data and data["husband"] is not None:
            person.husband = Person.people[data["husband"]]

    return result
