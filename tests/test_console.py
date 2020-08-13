#!/usr/bin/python3
""" [Test console] """

import pep8
import unittest
import os
from io import StringIO
from console import HBNBCommand
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from unittest.mock import patch


class Test_HBNBCommand(unittest.TestCase):
    def setUp(cls):
        """Set up test"""
        cls.cons = HBNBCommand
    
    def tearDown(cls):
        """Removes json file"""
        FileStorage.__Filestorage__objects = {}
        try:
            os.remove('file.json')
        except:
            pass
    
    def test_pep8(self):
        """TEst pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0)

    def test_documentation(self):
        """Test documentation"""
        self.assertIsNotNone(HBNBCommand.preloop.__doc__)
        self.assertIsNotNone(HBNBCommand.precmd.__doc__)
        self.assertIsNotNone(HBNBCommand.postcmd.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_promt(self):
        """Tests the prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_do_create(self):
        with patch("sys.stdout", new=StringIO()) as fil:
            HBNBCommand().onecmd("create BaseModel")
            value = fil.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as fil:
            HBNBCommand().onecmd("create")
        with patch("sys.stdout", new=StringIO()) as fil:
            HBNBCommand().onecmd("BaseModel.create()")
            value = fil.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as fil:
            HBNBCommand().onecmd("Amenity.create()")
            value = fil.getvalue().strip()
    
    def test_show(self):
        """test show"""
        with patch("sys.stdout", new=StringIO()) as fil:
            HBNBCommand().onecmd("create BaseModel")
            value = fil.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as fil:
            objects = storage.all()["BaseModel.{}".format(value)]
            command = "show BaseModel {}".format(value)
            HBNBCommand().onecmd(command)
            self.assertEqual(objects.__str__(), fil.getvalue().strip())
    
    def test_destroy(self):
        """Test destroy"""
        with patch("sys.stdout", new=StringIO()) as fil:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            id_object = fil.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as fil:
                objects = storage.all()["BaseModel.{}".format(id_object)]
                command = "destroy BaseModel {}".format(id_object)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(objects, storage.all())

        
            

    


if __name__ == "__main__":
    unittest.main()