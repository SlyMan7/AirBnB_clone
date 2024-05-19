#!/usr/bin/python3
"""
This module provides a command-line interface for managing storage of various models.
"""

import cmd
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

def parse_args(argument):
    """
    Parses command line arguments for update method.
    Returns a tuple containing the id and either a dictionary of attributes or a string of attribute name and value.
    """
    curly_braces = re.search(r'\{(.*?)\}', argument)
    if curly_braces:
        pre_brace_content = shlex.split(argument[:curly_braces.span()[0]])
        obj_id = pre_brace_content[0].strip(',')
        attributes = ast.literal_eval('{' + curly_braces.group(1) + '}')
        return obj_id, attributes
    else:
        parts = shlex.split(argument)
        return parts[0], ' '.join(parts[1:])

class HBNBCommand(cmd.Cmd):
    """
    Command console for HBNB project.
    """
    prompt = '(hbnb) '
    valid_classes = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                     'Place': Place, 'Review': Review, 'State': State, 'City': City}

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it to JSON file, and prints the id.
        """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        instance = self.valid_classescls_name
        instance.save()
        print(instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
