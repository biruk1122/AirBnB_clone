#!/user/bin/python3
""" import libraries and files """


import uuid
from datetime import datetime
from models import storage

class BaseModel:


    """A BaseModel class with common attributes and methods
    that can be inherited by other classes."""
    

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the class with a unique identifier (id),
        creation timestamp (created_at), and update timestamp (updated_at)."""
        if kwargs:
            # Re-create instance from dictionary representation
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    # Convert string to datetime object
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            # Create a new instance with id and created_at
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # Call new method on storage for new instances

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime and calls save method on storage."""


        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""


        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
