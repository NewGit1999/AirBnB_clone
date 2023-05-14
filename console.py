#!/usr/bin/python3
"""Console module"""

import json
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb) '
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

    def do_create(self, line):
        """creates new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return None
        else:
            line = eval(line + '()')
            line.save()
            print(line.id)

    def do_show(self, line):
        """prints string representation of instances"""
        b = line.split()
        if not line:
            print("** class name missing **")
            return None
        elif (b[0] not in self.classes):
            print("** class doesn't exist **")
            return None
        elif len(b) < 2:
            print("** instance id missing **")
            return None
        else:
            k = '{}.{}'.format(b[0], b[1])
            if k not in storage.all().keys():
                print("** no instance found **")
            else:
                a = storage.all()
                print(a[k])

    def do_destroy(self, line):
        """deletes instance based on class name"""
        b = line.split()
        if not line:
            print("** class name missing **")
            return None
        elif (b[0] not in self.classes):
            print("** class doesn't exist **")
            return None
        elif len(b) < 2:
            print("** instance id missing **")
            return None
        else:
            k = '{}.{}'.format(b[0], b[1])
            if k not in storage.all().keys():
                print("** no instance found **")
            else:
                a = storage.all()
                del a[k]
                storage.save()

    def do_all(self, line):
        """prints all representations of all instances"""
        b = line.split()
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

    def do_update(self, line):
        """updates instances"""
        b = line.split()
        if not line:
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

    def do_count(self, line):
        """retrieve instance"""
        ins = 0
        for k in storage.all().keys():
            if line in k:
                ins += 1
        print(ins)

    def default(self, line):
        """retrieve instance based on methods"""
        b = line.split('.')
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
            self.do_show(line)
            return None
        elif b[1].startswith('destroy'):
            id_split = b[1].split('""')
            line = met + ' ' + id_split[1]
            self.do_destroy(line)
            return None
        elif b[1].startswith('update'):
            proj = b[1].split('""')
            bnb = met + ' ' + proj[1] + ' ' + proj[3] + ' ' + proj[5]
            self.do_update(line)
            return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
