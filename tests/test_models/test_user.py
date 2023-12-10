#!/user/bin/python3
import unittest
from datetime import datetime
from models.user import User  # Assuming User class is defined in models.user module

class TestUser(unittest.TestCase):

    def test_init(self):
        user = User(email='test@example.com', password='pass123', first_name='John', last_name='Doe')

        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'pass123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_str(self):
        user = User(email='test@example.com', password='pass123', first_name='John', last_name='Doe')

        expected_str = f"[{user.__class__.__name__}] ({user.id}) {user.__dict__}"
        self.assertEqual(str(user), expected_str)

    def test_save(self):
        user = User(email='test@example.com', password='pass123', first_name='John', last_name='Doe')

        initial_updated_at = user.updated_at
        user.save()

        self.assertNotEqual(user.updated_at, initial_updated_at)

    def test_to_dict(self):
        user = User(email='test@example.com', password='pass123', first_name='John', last_name='Doe')

        user_dict = user.to_dict()

        self.assertEqual(user_dict['email'], 'test@example.com')
        self.assertEqual(user_dict['password'], 'pass123')
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(datetime.fromisoformat(user_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(user_dict['updated_at']), datetime)

if __name__ == '__main__':
    unittest.main()
