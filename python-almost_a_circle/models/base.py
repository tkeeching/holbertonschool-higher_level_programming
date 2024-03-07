#!/usr/bin/python3
"""Base module"""

import json


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        result = []

        if (list_objs is not None):
            for obj in list_objs:
                result.append(obj.to_dictionary())

        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(Base.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""

        if (json_string is None or len(json_string) == 0):
            return []
        else:
            return json.loads(json_string)
        
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""

        if (cls.__name__ == 'Rectangle'):
            instance = cls(1, 1, 0)
        else:
            instance = cls(1, 0, 0)

        instance.update(**dictionary)

        return instance
        

# Tests
# if __name__ == "__main__":

#     b1 = Base()
#     print(b1.id)

#     b2 = Base()
#     print(b2.id)

#     b3 = Base()
#     print(b3.id)

#     b4 = Base(12)
#     print(b4.id)

#     b5 = Base()
#     print(b5.id)
