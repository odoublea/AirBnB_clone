#!/usr/bin/python3
"""
    Hbnb command line intepreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
        HBNB command line interpreter
    """
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
