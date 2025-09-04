#!/usr/bin/env python3
people = []

def store_person(name, age):
    person = {"name": name, "age": age}
    people.append(person)

number_of_people = int(input("How many people? "))

for i in range(number_of_people):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    store_person(name, age)

for person in people:
    print(f"Name: {person['name']}, Age: {person['age']}")