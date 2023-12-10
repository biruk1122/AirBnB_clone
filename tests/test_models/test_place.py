#!/user/bin/python3
import unittest
from datetime import datetime
from models.place import Place  # Assuming Place class is defined in models.place module

class TestPlace(unittest.TestCase):

    def test_init(self):
        place = Place(
            city_id='SF',
            user_id='123',
            name='Cozy Apartment',
            description='A nice place to stay',
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=37.7749,
            longitude=-122.4194,
            amenity_ids=['wifi', 'parking']
        )

        self.assertEqual(place.city_id, 'SF')
        self.assertEqual(place.user_id, '123')
        self.assertEqual(place.name, 'Cozy Apartment')
        self.assertEqual(place.description, 'A nice place to stay')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ['wifi', 'parking'])
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_str(self):
        place = Place(
            city_id='SF',
            user_id='123',
            name='Cozy Apartment',
            description='A nice place to stay',
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=37.7749,
            longitude=-122.4194,
            amenity_ids=['wifi', 'parking']
        )

        expected_str = f"[{place.__class__.__name__}] ({place.id}) {place.__dict__}"
        self.assertEqual(str(place), expected_str)

    def test_save(self):
        place = Place(
            city_id='SF',
            user_id='123',
            name='Cozy Apartment',
            description='A nice place to stay',
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=37.7749,
            longitude=-122.4194,
            amenity_ids=['wifi', 'parking']
        )

        initial_updated_at = place.updated_at
        place.save()

        self.assertNotEqual(place.updated_at, initial_updated_at)

    def test_to_dict(self):
        place = Place(
            city_id='SF',
            user_id='123',
            name='Cozy Apartment',
            description='A nice place to stay',
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=37.7749,
            longitude=-122.4194,
            amenity_ids=['wifi', 'parking']
        )

        place_dict = place.to_dict()

        self.assertEqual(place_dict['city_id'], 'SF')
        self.assertEqual(place_dict['user_id'], '123')
        self.assertEqual(place_dict['name'], 'Cozy Apartment')
        self.assertEqual(place_dict['description'], 'A nice place to stay')
        self.assertEqual(place_dict['number_rooms'], 2)
        self.assertEqual(place_dict['number_bathrooms'], 1)
        self.assertEqual(place_dict['max_guest'], 4)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 37.7749)
        self.assertEqual(place_dict['longitude'], -122.4194)
        self.assertEqual(place_dict['amenity_ids'], ['wifi', 'parking'])
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsInstance(datetime.fromisoformat(place_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(place_dict['updated_at']), datetime)

if __name__ == '__main__':
    unittest.main()
