#!/usr/bin/python3
""" Module for HBNB console """
import cmd


class HBNBCommand(cmd.Cmd):
    """ The class for the command interpreter"""
    
    prompt = "(hbnb) "
    
    def do_EOF(self, line):
        """EOF (End Of File) to exit program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
