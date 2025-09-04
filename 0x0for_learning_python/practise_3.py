#!/usr/bin/env python3
def store_person(name, age):
    person = {"name": name, "age": age}
    print(f"Name: {person['name']}, Age: {person['age']}")
    return person

store_person(input(), input())