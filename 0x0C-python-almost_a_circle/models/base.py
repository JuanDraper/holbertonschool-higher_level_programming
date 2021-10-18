#!/usr/bin/python3
"""module containing the Base"""
import json
class Base:
    """
    Base class 
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor .
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Json of a list of dictionarries"""
        if list_dictionaries is None or list_dictionaries  == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves the json into a file"""
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
                return
            listi = list()
            for i in list_objs:
                listi.append(i.to_dictionary())
            f.write(Base.to_json_string(listi))

    @staticmethod
    def from_json_string(json_string):
        """returns object from json"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns a new object from a dictionary"""
        if cls.__name__ == "Rectangle":
            o = cls(1, 1)
        elif cls.__name__ == "Square":
                o = cls(1)
        o.update(**dictionary)
        return o

    @classmethod
    def load_from_file(cls):


