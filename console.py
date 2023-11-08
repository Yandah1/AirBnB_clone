#!/usr/bin/python3
"""create a console that contains
    a command interpreter"""

import models
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """a command class that inherits from cmd"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        exit(0)

    def do_EOF(self, args):
        """EOF exits the program"""
        print("")
        exit(0)

    def emptyline(self):
        """execute nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
