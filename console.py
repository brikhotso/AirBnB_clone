#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Define HBNB command interpreter"""
    prompt = '(hbnb)'

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, line):
        """Exit the program. Usage: quit"""
        return True

    def do_EOF(self, line):
        """Exit the program. Usage: Ctrl-D"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
