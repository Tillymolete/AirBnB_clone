#!/usr/bin/python3

import cmd

class HBNBC(cmd.Cmd):

    prompt = "(hbnb) "

    def quit(self, arg):
        """A quit command to exit program"""

        return True

    def EOF(self, arg):
        """EOF will also exit the program"""
        return True

if __name__ = "__main__":
    HBNBCommand().cmdloop()
