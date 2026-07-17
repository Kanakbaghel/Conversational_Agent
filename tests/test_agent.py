import unittest
from dialogflow_client import detect_intent_text

class TestAgent(unittest.TestCase):
    def test_greeting(self):
        responses = detect_intent_text("test-session", "Hello")
        self.assertTrue(any("Hi" in r.text.text[0] for r in responses))

if __name__ == "__main__":
    unittest.main()
