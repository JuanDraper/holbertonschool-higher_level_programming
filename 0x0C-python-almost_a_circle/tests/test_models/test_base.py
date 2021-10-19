"""Unittest for the Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
""" Base = Base
to_json_string = Base.to_json_string
save_to_file = Base.save_to_file
from_json_string = Base.from_json_string
create = Base.create
load_from_file = Base.load_from_file
 """
class TestBase(unittest.TestCase):



    def doc_test(self):
        """tests the documantattion"""

        self.assertTrue(len(Base.__doc__) > 0)

    def cdoc_test(self):
        """test for class doc"""

        self.assertTrue(len(Base.__doc__) > 0)

    def testJsonString(self):
        """test the representation of json"""

        self.assertTrue(len(Base.to_json_string.__doc__) > 0)

    def saveFileTest(self):
        """tests the save file"""

        self.assertTrue(len(Base.save_to_file.__doc__) > 0)

    def JsonStringTest(self):
        """test from json"""

        self.assertTrue(len(Base.from_json_string.__doc__) > 0)

    def CreateTest(self):
        """test the create"""

        self.assertTrue(len(Base.create.__doc__) > 0)

    def LoadFileTest(self):
        """test the load file"""

        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

    """Base class test cases"""
    def arg01Test(self):
        """no argument passed """
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def arg02Test(self):
        """with one object created but with argument"""
        Base._Base__nb_objects = 0
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(98)
        self.assertEqual(b4.id, 98)
        b5 = Base(-8)
        self.assertEqual(b5.id, -8)
        b6 = Base(9)
        self.assertEqual(b6.id, 9)

    def arg03Test(self):
        """many ojects one with arg"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b5.id, 3)

    def arg04Test(self):
        """many objects one with arg"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b3 = Base()
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def 2argsTest(self):
        """tests with args"""
        Base._Base__nb_objects = 0
        b3 = Base(6)
        b4 = Base(98)
        self.assertEqual(b4.id, 98)

    def testTypeInstance(self):
        """type and instance."""
        b6 = Base()
        self.assertEqual(type(b6), Base)
        self.assertTrue(isinstance(b6, Base))

    def arg05Test(self):
        """ many objects, one without arg"""
        Base._Base__nb_objects = 0
        b3 = Base(5)
        b4 = Base(12)
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def pATest(self):
        """checks the existence of attributes"""
        self.assertFalse(hasattr(Base, '__nb_objects'))

    def RectangleSaveFileTest(self):
        """ saving JSON"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(r1.to_dictionary(), my_list[0])
            self.assertDictEqual(r2.to_dictionary(), my_list[1])

    def NoneSaveRectangleTest(self):
        """saving  with none"""
        Base._Base__nb_objects = 0
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertListEqual(my_list, [])

    def emptyListTest(self):
        """saving to file with none"""
        Base._Base__nb_objects = 0
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertListEqual(my_list, [])

    def testRectangleOnly(self):
        """O.o"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(r1.to_dictionary(), my_list[0])

    def SquareSaveTest(self):
        """ saving json"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        s2 = Square(2)
        Square.save_to_file([r1, s2])
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(r1.to_dictionary(), my_list[0])
            self.assertDictEqual(s2.to_dictionary(), my_list[1])

    def SquareSaveTest02(self):
        """saving to file"""
        Base._Base__nb_objects = 0
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertListEqual(my_list, [])

    def OnlySquareSaveTest(self):
        """saving only Square"""
        Base._Base__nb_objects = 0
        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(s1.to_dictionary(), my_list[0])

    def CreateRectangleTest(self):
        ""new rectangle"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertDictEqual(r1_dictionary, r2.to_dictionary())

    def CreateSquareTEst(self):
        """new sqare"""
        Base._Base__nb_objects = 0
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertDictEqual(s1_dictionary, s2.to_dictionary())

    def RectangleLoadFileTest(self):
        """rectangle loading file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_input[0].__str__(),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rectangles_output[0].__str__(),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rectangles_input[1].__str__(),
                         "[Rectangle] (2) 0/0 - 2/4")
        self.assertEqual(list_rectangles_output[1].__str__(),
                         "[Rectangle] (2) 0/0 - 2/4")

    def loadSquareFileTest(self):
        """Square loading file"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_input[0].__str__(),
                         "[Square] (5) 0/0 - 5")
        self.assertEqual(list_squares_output[0].__str__(),
                         "[Square] (5) 0/0 - 5")
        self.assertEqual(list_squares_input[1].__str__(),
                         "[Square] (6) 9/1 - 7")
        self.assertEqual(list_squares_output[1].__str__(),
                         "[Square] (6) 9/1 - 7")

    def JsonToStringTest(self):
        """to_json_string with wrong args."""

        s1 = ("to_json_string() missing 1 required positional argument: " +
              "'list_dictionaries'")
        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(s1, str(x.exception))
        s2 = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(s2, str(x.exception))

    def ToJsonStringTest(self):
        """json string"""
        a = Base()
        b = a.__dict__
        self.assertTrue(type(b) is dict)
        c = Base.to_json_string([b])
        self.assertTrue(type(c) is str)

    def FromJsonStringTest(self):
        """json string"""
        a = Base(12)
        b = a.__dict__
        c = Base.to_json_string([b])
        d = Base.from_json_string(c)
        self.assertTrue(type(c) is str)
        self.assertTrue(type(d) is list)


if __name__ == "__main__":
    unittest.main()
