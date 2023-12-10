#!/user/bin/python3
import unittest
from datetime import datetime
from models.city import City  # Assuming City class is defined in models.city module

class TestCity(unittest.TestCase):

    def test_init(self):
        city = City(state_id='CA', name='San Francisco')

        self.assertEqual(city.state_id, 'CA')
        self.assertEqual(city.name, 'San Francisco')
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_str(self):
        city = City(state_id='CA', name='San Francisco')

        expected_str = f"[{city.__class__.__name__}] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected_str)

    def test_save(self):
        city = City(state_id='CA', name='San Francisco')

        initial_updated_at = city.updated_at
        city.save()

        self.assertNotEqual(city.updated_at, initial_updated_at)

    def test_to_dict(self):
        city = City(state_id='CA', name='San Francisco')

        city_dict = city.to_dict()

        self.assertEqual(city_dict['state_id'], 'CA')
        self.assertEqual(city_dict['name'], 'San Francisco')
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(datetime.fromisoformat(city_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(city_dict['updated_at']), datetime)

if __name__ == '__main__':
    unittest.main()
