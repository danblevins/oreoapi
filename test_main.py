import unittest
from main import app

class TestMain(unittest.TestCase):

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    def test_cookiejar(self):
        tester = app.test_client(self)
        response = tester.get("/cookiejar")
        self.assertEqual(response.content_type, "image/jpg")

    def test_cookiejar_json(self):
        tester = app.test_client(self)
        response = tester.get("/cookiejar.json")
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'oreo' in response.data)

if __name__ == "__main__":
    unittest.main()