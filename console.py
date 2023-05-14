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

    def do_all(self, bnb):
        """prints all representations of all instances"""
        b = bnb.split()
        instance = []
        if len(b) == 0:
            for value in storage.all().values():
                instance.append(value.__str__())
            print(instance)
        elif (b[0] not in self.classes):
            print("** class doesn't exist **")
        else:
            for k, value in storage.all().items():
                if b[0] in k:
                    instance.append(storage.all()[k].__str__())
                else:
                    return
            print(instance)

    def do_update(self, bnb):
        """updates instances"""
        b = bnb.split()
        if not bnb:
            print("** class name missing **")
            return None
        elif (b[0] not in self.classes):
            print("** class doesn't exist **")
            return None
        elif len(b) < 2:
            print("** instance id missing **")
            return None
        else:
            abc = storage.all()
            k = '{}.{}'.format(b[0], b[1])
            if k not in abc:
                print("** no instance found **")
                return None
            elif len(b) == 2:
                print("** attribute name missing **")
                return None
            elif len(b) == 3:
                print("** value missing **")
                return None
            else:
                setattr(abc[k], b[2], b[3])
                storage.save()
                return None

    def do_cout(self, bnb):
        """retrieve instance"""
        ins = 0
        for k in storage.all().keys():
            if bnb in k:
                ins += 1
        print(ins)

    def default(self, bnb):
        """retrieve instance based on methods"""
        b = bnb.split('.')
        met = b[0]
        if b[1] == 'all()':
            self.do_all(met)
            return None
        elif b[1] == 'count()':
            self.do_count(met)
            return None
        elif b[1].startswith('show'):
            id_split = b[1].split('""')
            bnb = met + ' ' + id_split[1]
            self.do_show(bnb)
            return None
        elif b[1].startswith('destroy'):
            id_split = b[1].split('""')
            bnb = met + ' ' + id_split[1]
            self.do_destroy(bnb)
            return None
        elif b[1].startswith('update'):
            proj = b[1].split('""')
            bnb = met + ' ' + proj[1] + ' ' + proj[3] + ' ' + proj[5]
            self.do_update(bnb)
            return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
