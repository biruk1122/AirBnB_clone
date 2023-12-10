#!/user/bin/python3
import unittest
from datetime import datetime
from models.review import Review  # Assuming Review class is defined in models.review module

class TestReview(unittest.TestCase):

    def test_init(self):
        review = Review(
            place_id='123',
            user_id='456',
            text='Great place, highly recommended!'
        )

        self.assertEqual(review.place_id, '123')
        self.assertEqual(review.user_id, '456')
        self.assertEqual(review.text, 'Great place, highly recommended!')
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_str(self):
        review = Review(
            place_id='123',
            user_id='456',
            text='Great place, highly recommended!'
        )

        expected_str = f"[{review.__class__.__name__}] ({review.id}) {review.__dict__}"
        self.assertEqual(str(review), expected_str)

    def test_save(self):
        review = Review(
            place_id='123',
            user_id='456',
            text='Great place, highly recommended!'
        )

        initial_updated_at = review.updated_at
        review.save()

        self.assertNotEqual(review.updated_at, initial_updated_at)

    def test_to_dict(self):
        review = Review(
            place_id='123',
            user_id='456',
            text='Great place, highly recommended!'
        )

        review_dict = review.to_dict()

        self.assertEqual(review_dict['place_id'], '123')
        self.assertEqual(review_dict['user_id'], '456')
        self.assertEqual(review_dict['text'], 'Great place, highly recommended!')
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(datetime.fromisoformat(review_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(review_dict['updated_at']), datetime)

if __name__ == '__main__':
    unittest.main()
