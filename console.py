#!/usr/bin/python3
""" Defines entry point of the command interpreter."""

import cmd
import shlex
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def generate_class_methods(class_name):
    """Generates methods for actions with a specific class"""

    def do_create_instance(self, arg):
        """Creates a new instance of {class_name}"""
        self.do_create(f"{class_name} {arg}")

    def do_show_instance(self, arg):
        """Shows an instance of {class_name}"""
        self.do_show(f"{class_name} {arg}")

    def do_destroy_instance(self, arg):
        """Deletes an instance of {class_name}"""
        self.do_destroy(f"{class_name} {arg}")

    def do_all_instances(self, arg):
        """Shows all instances of a specific class"""
        self.do_all(f"{class_name} {arg}")

    def do_update_instance(self, arg):
        """Updates an instance of {class_name}"""
        self.do_update(f"{class_name} {arg}")

    def do_count_instance(self, arg):
        """Updates an instance of {class_name}"""
        self.do_count(f"{class_name} {arg}")

    return (do_create_instance, do_show_instance, do_destroy_instance,
            do_all_instances, do_update_instance, do_count_instance)


def add_class_methods(cls):
    """ add class methods decorator definition"""
    for class_name in ["User", "Place", "State", "City", "Amenity", "Review"]:
        (create_method, show_method, destroy_method, all_method, update_method,
         count_method) = generate_class_methods(class_name)
        setattr(cls, f"do_create_{class_name.lower()}", create_method)
        setattr(cls, f"do_show_{class_name.lower()}", show_method)
        setattr(cls, f"do_destroy_{class_name.lower()}", destroy_method)
        setattr(cls, f"do_all_{class_name.lower()}", all_method)
        setattr(cls, f"do_update_{class_name.lower()}", update_method)
        setattr(cls, f"do_count_{class_name.lower()}", count_method)
    return cls


@add_class_methods
class HBNBCommand(cmd.Cmd):
    """Define HBNB command interpreter"""

    prompt = '(hbnb) '

    def default(self, arg):
        """Called on an input line when the command prefix is not recognized."""
        class_methods = {
            'all': 'do_all',
            'create': 'do_create',
            'show': 'do_show',
            'destroy': 'do_destroy',
            'update': 'do_update',
            'count': 'do_count'
        }

        parts = arg.split('.')
        if len(parts) == 2 and parts[1].startswith('update'):
            class_name, method_and_params = parts[0], parts[1]
            if method_and_params.startswith('update(') and method_and_params.endswith(')'):
                method_name, params = method_and_params.split('(')
                if method_name in class_methods:
                    class_name = class_name.capitalize()
                    method_name = f"do_{method_name}_{class_name.lower()}"
                    if hasattr(self, method_name):

                        match = re.match(r'\"(.+?)\"\s*,\s*(\{.*\})', params)
                        if match:
                            id_str = match.group(1)
                            dict_repr = match.group(2)
                            dict_repr = dict_repr.strip('{}')
                            getattr(self, method_name)(f"{id_str} {dict_repr}")
                            return
                        else:
                            match_attr = re.match(r'\"(.+?)\"\s*,\s*\"(.+?)\"\s*,\s*\"(.+?)\"', params)
                            if match_attr:
                                id_str = match_attr.group(1)
                                attribute_name = match_attr.group(2)
                                attribute_value = match_attr.group(3)
                                getattr(self, method_name)(f"{id_str} {attribute_name} {attribute_value}")
                                return
                    else:
                        print("** class doesn't exist **")
                        return

        parts = arg.split('.')
        if len(parts) == 2 and parts[1].endswith(')'):
            class_name, method = parts[0], parts[1].split('(')[0]
            if method in class_methods:
                class_name = class_name.capitalize()
                method_name = f"do_{method}_{class_name.lower()}"
                if hasattr(self, method_name):

                    id_str = parts[1].split('(')[1][:-1].strip('\"')
                    getattr(self, method_name)(id_str)
                    return
                else:
                    print("** class doesn't exist **")
                    return

        parts = arg.split('.')
        if len(parts) == 2:
            class_name, method = parts[0], parts[1]
            if method in class_methods:
                class_name = class_name.capitalize()
                method_name = f"do_{method}_{class_name.lower()}"
                if hasattr(self, method_name):
                    getattr(self, method_name)("")
                    return
                else:
                    print("** class doesn't exist **")
                    return

        print("Invalid command:", arg)

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place",
                              "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

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

        print([str(instance) for instance in storage.all().values() if isinstance(instance, cls)])

    def do_update(self, arg):
        """Updates an instance based on class name and id"""

        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
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

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        inst = instance[key]
        setattr(inst, args[2], args[3])
        inst.save()

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.capitalize()
        try:
            cls = eval(class_name)
            count = len([instance for instance in storage.all().values() if isinstance(instance, cls)])

            print(count)
        except NameError:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """Exit the program. Usage: quit"""
        return True

    def do_EOF(self, line):
        """Exit the program. Usage: Ctrl-D"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
