#!/usr/bin/python3
"""
    Hbnb command line intepreter
"""


import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        HBNB command line interpreter
    """
    intro = 'Welcome to the Hbnb shell. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """
        if arg == "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        if arg == "":
            print("** class name missing **")
        elif arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        if arg == "":
            print("** class name missing **")
        elif arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all
        """
        if arg == "":
            for value in models.storage.all().values():
                print(value)
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if arg in key:
                    print(value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
