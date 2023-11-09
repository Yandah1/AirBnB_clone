#!/usr/bin/python3
"""create a console that contains
    a command interpreter"""

import models
import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """a command class that inherits from cmd"""
    prompt = '(hbnb) '
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit(0)

    def do_EOF(self, arg):
        """EOF exits the program"""
        print("")
        exit(0)

    def emptyline(self):
        """execute nothing"""
        pass

    def do_create(self, arg):
        """create a new instance of Basemodel"""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_inst = eval(arg)()
            new_inst.save()
            print(new_inst.id)
        finally:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)

        if len(args) < 1:
            cls = args[0]
        else:
            print("** class name missing **")
            return
        if cls not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            id = args[1]
        else:
            print("** instance id missing **")
            return

        key = cls + '.' + id
        all_instances = storage.all()
        if key not in all_instances:
            print("** no instance found **")
            return
        print(all_instances[key])

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return

        cls = args[0]
        if cls not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id = args[1]
        key = cls + "." + id
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """print all string representation of instances"""
        args = shlex.split(arg)

        all_instances = storage.all()
        if len(args) < 1:
            print([str(inst) for inst in all_instances.values()])
            return

        cls = args[0]
        if cls not in self.__classes:
            print("* class doesn't exist *")
            return

        print([str(inst) for inst in all_instances.values() if
              type(inst).__name__ == cls])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)

        if len(args) < 1:
            print("** class name missing **")
            return

        cls = args[0]
        if cls not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id = args[1]
        key = cls + '.' + id

        all_instances = storage.all()
        if key not in all_instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        instance = all_instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
