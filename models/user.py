#!/user/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the class with user-specific attributes."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """Returns the string representation of the User instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
