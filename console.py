#!/usr/bin/python3
"""create a console that contains 
a command interpreter"""

import modules
import cmd

class HBNBCommand(cmd.Cmd):
     """a command class that inherits from cmd"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """a command that exits the program"""
        Exit (0)

    def do_EOF(self, args):
       """EOF exits the program"""
        print("")
        Exit (0)
    
    def emptyline(self):
        """execute nothing"""
        pass
 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
  
