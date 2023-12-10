#!/user/bin/python3
import unittest
from datetime import datetime
from models.amenity import Amenity  # Assuming Amenity class is defined in models.amenity module

class TestAmenity(unittest.TestCase):

    def test_init(self):
        amenity = Amenity(name='WiFi')

        self.assertEqual(amenity.name, 'WiFi')
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_str(self):
        amenity = Amenity(name='WiFi')

        expected_str = f"[{amenity.__class__.__name__}] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(str(amenity), expected_str)

    def test_save(self):
        amenity = Amenity(name='WiFi')

        initial_updated_at = amenity.updated_at
        amenity.save()

        self.assertNotEqual(amenity.updated_at, initial_updated_at)

    def test_to_dict(self):
        amenity = Amenity(name='WiFi')

        amenity_dict = amenity.to_dict()

        self.assertEqual(amenity_dict['name'], 'WiFi')
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(datetime.fromisoformat(amenity_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(amenity_dict['updated_at']), datetime)

if __name__ == '__main__':
    unittest.main()
