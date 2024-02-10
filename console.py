#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Define HBNB command interpreter"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, line):
        """Exit the program. Usage: quit"""
        return True

    def do_EOF(self, line):
        """Exit the program. Usage: Ctrl-D"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        try:
            cls = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return
        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 1:
            print("** instance id missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in instance:
            print("** no instance found **")
            return

        print(instance[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 1:
            print("** instance id missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in instance:
            print("** no instance found **")
            return

        del instance[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(instance) for instance in storage.all().values()])
            return

        try:
            cls = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return

        print([str(instance) for key, instance in storage.all().items() if arg in key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
