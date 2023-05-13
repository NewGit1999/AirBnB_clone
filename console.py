#!/usr/bin/python3
"""Console module"""

import json
import cmd
import re
from models import *


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb)'
    classes = [
            'BaseMdel',
            'Place',
            'State',
            'City',
            'User',
            'Amenity',
            'Review'
            ]

    def do_EOF(self, line):
        """exit the programme"""
        return True

    def do_quit(self, line):
        """exit the programme"""
        return True

    def emptyline(self):
        """funtion shouldn't execute anything with Enter"""
        pass

    def do_create(self, bnb):
        """creates new instance of BaseModel"""
        if bnb == "" or bnb is None:
            print("** class name missing **")
        elif bnb not in storage.classes():
            print("** class doesn't exist **")
        else:
            value = storage.classes()[bnb]()
            value.save()
            print(value.id)

    def do_show(self, bnb):
        """prints string representation of instances"""
        if bnb == "" or bnb is None:
            print("** class name missing **")
        else:
            data = bnb.split(' ')
            if data[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(data) < 2:
                print("** instance id missing **")
            else:
                yas = "{}.{}".format(data[0], data[1])
                if yas not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[yas])

    def do_destroy(self, bnb):
        """deletes instance based on class name"""
        if bnb == "" or bnb is None:
            print("** class name missing **")
        else:
            data = bnb.split(' ')
            if data[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(data) < 2:
                print("** instance id missing **")
            else:
                yas = "{}.{}".format(data[0], data[1])
                if yas not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[yas]
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
