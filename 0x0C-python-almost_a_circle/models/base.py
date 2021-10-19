#!/usr/bin/python3
"""module containing the Base"""
import json
import csv


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
        if list_dictionaries is None or list_dictionaries == []:
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
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as i:
                e = cls.from_json_string(i.read())
                new = []
                for j in e:
                    new.append(cls.create(**j))
                return new
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves to a .csv file"""
        with open(cls.__name__ + ".csv", "w") as f:
            ld = list()
            for item in list_objs:
                ld.append(item.to_dictionary())
            if cls.__name__ == "Rectangle":
                fn = ["id", "width", "height", "x", "y"]
            else:
                fn = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fn)
            writer.writeheader()
            writer.writerows(ld)

    @classmethod
    def load_from_file_csv(cls):
        """loads from a .csv file"""
        a = []
        with open(cls.__name__ + ".csv", "r") as f:
            reader = csv.DictReader(f)
            for li in reader:
                ka = dict(li)
                for k, v in ka.items():
                    ka[k] = int(v)
                a.append(cls.create(**ka))
            return a
