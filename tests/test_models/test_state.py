#!/user/bin/python3
import unittest
from datetime import datetime
from models.state import State  # Assuming State class is defined in models.state module

class TestState(unittest.TestCase):

    def test_init(self):
        state = State(name='California')

        self.assertEqual(state.name, 'California')
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_str(self):
        state = State(name='California')

        expected_str = f"[{state.__class__.__name__}] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), expected_str)

    def test_save(self):
        state = State(name='California')

        initial_updated_at = state.updated_at
        state.save()

        self.assertNotEqual(state.updated_at, initial_updated_at)

    def test_to_dict(self):
        state = State(name='California')

        state_dict = state.to_dict()

        self.assertEqual(state_dict['name'], 'California')
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(datetime.fromisoformat(state_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(state_dict['updated_at']), datetime)

if __name__ == '__main__':
    unittest.main()
