import unittest
from main import App_Window

class TestHelloName(unittest.TestCase):
    
    def setUp(self):
        # Set up the HelloName instance
        self.app = App_Window()


if __name__ == "__main__":
    unittest.main()