import unittest
import json
from app import app

class APITestCase(unittest.TestCase):

    def test_save(self):
        with app.test_client() as c:
            response = c.post(
                "/api/save",
                data=json.dumps({"content": "Test Content"}),
                content_type="application/json",
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn("message", json.loads(response.get_data()))

    def test_load(self):
        with app.test_client() as c:
            response = c.get("/api/load?page=1")
            self.assertEqual(response.status_code, 200)
            content_list = json.loads(response.get_data())
            self.assertTrue(isinstance(content_list, list))
            self.assertTrue(len(content_list) <= 20)

if __name__ == "__main__":
    unittest.main()
