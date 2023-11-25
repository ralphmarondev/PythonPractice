def simple_dictionary():
    person = {"name": "Ralph", "age": 20, "degree": "Computer Engineer"}

    # accessing element [may raise error if not exist]
    print(person['name'])  # Ralph
    print(person['age'])  # 20

    # to avoid error
    print(person.get('name', 'default value'))

    # adding new element in dictionary
    # simply assign a value to corresponding key
    person['personality'] = 'cute'

    # removing an element
    person.pop('personality') # or [below]
    del person['personality']

    # clearing dictionary
    person.clear()

    # copying dictionary
    copied_dict = person.copy() # using copy method
    copied_dict = dict(person)  # using dict() constructor


def dictionary_comprehension():
    # dictionary of squares
    squares = {x: x*x for x in range(1,6)}


def nested_dictionary():
    family = {
        "father": {"name": "John", "age": 40},
        "mother": {"name": "Mary", "age": 41},
        "children": [
            {"name": "Alice", "age": 12},
            {"name": "Bob", "age": 8}
        ]
    }

    print(family['father'])
    print(family.get('father', 'cute si maron'))

class DictionaryExercises:
    # counting occurrences of elements in a list using dictionary
    def counting(self):
        fruits = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana']
        fruit_count = {}

        for fruit in fruits:
            fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
        print(fruit_count)

if __name__ == '__main__':
    # nested_dictionary()
    # simple_dictionary()
    de = DictionaryExercises()

    de.counting()
