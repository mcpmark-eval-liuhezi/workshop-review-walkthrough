"""Small Python utility collection."""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def join_words(words):
    """Join a list of words with a comma and a space."""
    return ", ".join(words)


def sort_people(people):
    """Return a sorted list of people by name."""
    return sorted(people, key=lambda person: person["name"])
