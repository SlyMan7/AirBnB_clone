#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    The base class for all models, providing initialization, serialization, and representation methods.

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): A datetime object noting when an instance was created.
        updated_at (datetime): A datetime object noting when an instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Unused.
            **kwargs: A dictionary of attributes for the instance, including special handling for 'created_at' and 'updated_at'.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        
        for key, value in kwargs.items():
            if key not in ["__class__", "created_at", "updated_at"]:
                setattr(self, key, value)
            elif key in ["created_at", "updated_at"]:
                setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        
        models.storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime and saves the instance to storage.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance's __dict__, including the class name and datetime attributes as strings.
        """
        inst_dict = dict(self.__dict__)
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = inst_dict["created_at"].isoformat()
        inst_dict["updated_at"] = inst_dict["updated_at"].isoformat()
        return inst_dict

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance, including the class name, id, and dictionary of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

# Example usage
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model)
    my_model_json = my_model.to_dict()
    print("JSON of my_model:")
    for key, value in my_model_json.items():
        print("\t{}: ({}) - {}".format(key, type(value).__name__, value))
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model)
    print("Are my_model and my_new_model the same instance? {}".format(my_model is my_new_model))

