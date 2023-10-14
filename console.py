#!/usr/bin/python3
""" Module for HBNB console """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ The class for the command interpreter"""

    prompt = "(hbnb) "

    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'state': State, 'City': City, 'Amenity': Amenity,
               'Review': Review}

    def do_EOF(self, line):
        """EOF (End Of File) to exit program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """an empty line doesn't do anything on Enter"""
        pass

    def do_create(self, arg):
        """create an instance."""
        if arg is None or arg == "":
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new = HBNBCommand.classes[arg]()
            storage.save()
            print(new.id)

    def do_show(self, arg):
        """Print the string rpresentation of an instance"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            a = arg.split(' ')
            if a[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(a) == 1:
                print("** instance id missing **")
            else:
                line = "{}.{}".format(a[0], a[1])
                if line not in storage.all():
                    print("** no instance found **")
                else:
                    print(line)

    def do_destroy(self, arg):
        """ Delete an instance :destroy <class> <id>"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            a = arg.split(' ')
            if a[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(a) == 1:
                print("** instance id missing **")
            else:
                line = "{}.{}".format(a[0], a[1])
                if line not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[line]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        print_list = []
        if arg:
            arg = arg.split(' ')[0]
            if arg not in HBNBCommand.classes:
                print("")
            else:
                for k, v in storage._FileStorage__objects.items():
                    if k.split('.')[0] == arg:
                        print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))
        print(print_list)

    def remove_quot(self, arg):
        """remove the quotations and commas from the arguments"""
        for i in range(len(arg)):
            if arg[i][0] in ('"', "'"):
                arg[i] = arg[i].replace('"', "").replace("'", "")
        return arg

    def do_update(self, arg):
        """Update " certain object with new info"""
        instance_dict = storage.all()

        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            a = arg.split(' ')
            a = self.remove_quot(a)
            if a[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            else:
                classname = a[0]

            if len(a) == 1:
                print("** instance id missing **")
                return
            else:
                uid = a[1]

            key = classname + "." + uid

            if key not in storage.all():
                print("** no instance found **")
                return

            if len(a) == 2:
                print("** attribute name missing **")
                return

            if len(a) == 3:
                try:
                    type(eval(a[2])) != dict
                except NameError:
                    print("** value missing **")
                    return
            new_attr = a[2]
            if a[3].isdigit():
                new_val = eval(a[3])
            else:
                new_val = a[3]
            setattr(instance_dict[key], new_attr, new_val)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
