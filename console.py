#!/usr/bin/python3
""" Module for HBNB console """
import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ The class for the command interpreter"""
    
    prompt = "(hbnb) "

    classes = {'BaseModel': BaseModel}
    
    def do_EOF(self, line):
        """EOF (End Of File) to exit program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """create an instance."""
        if arg is None or arg == "":
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            bm = BaseModel() 
            bm.save()
            print(bm.id)

    def do_show(self, arg):
        """Print the string rpresentation of an instance"""
        if arg =="" or arg is None:
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

    def dp_update(self, arg):
        """Update " certain object with new info"""       
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
