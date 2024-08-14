
import unittest
from src.utils import preprocess, greeting, generate_response

class TestChatbot(unittest.TestCase):

    def test_preprocess(self):
        self.assertEqual(preprocess("Hello! How are you?"), ['hello', 'how', 'are', 'you'])

    def test_greeting(self):
        self.assertIn(greeting("Hello"), ["Hello!", "Hi!", "Hey!", "Greetings!", "How can I assist you today?"])
        self.assertIsNone(greeting("Goodbye"))

    def test_generate_response(self):
        response = generate_response("How can you help me?")
        self.assertTrue(isinstance(response, str))
        self.assertNotEqual(response, "")

if __name__ == "__main__":
    unittest.main()
