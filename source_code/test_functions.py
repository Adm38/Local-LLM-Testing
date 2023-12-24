import unittest
from unittest.mock import patch
from io import StringIO

from functions import print_to_console
from functions_config import whitelisted_functions
from main import setup_chain

# TODO: create TestCreateLLMChatObject

class TestLLMFunctionInvocation(unittest.TestCase):
    def setUp(self):
        # This method is called before each test method.
        self.mock_stdout = patch('sys.stdout', new_callable=StringIO).start()

    def tearDown(self):
        # This method is called after each test method.
        # Stop the patch to clean up and restore the original sys.stdout.
        patch.stopall()

    def clear_mock_stdout(self):
        # Clear mock_stdout for the next test
        self.mock_stdout.truncate(0)
        self.mock_stdout.seek(0)
    
    def test_calling_hello_world_function(self):
        ...

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_to_console(self, mock_stdout):
        message = "Hello, world!"
        print_to_console(message)
        self.assertEqual(mock_stdout.getvalue().strip(), message)

        # Arrange
        chain = setup_chain()

        # Act - direct suggestion
        func_to_call_direct_suggestion = chain.invoke({"query": "print_to_console Green Tomatos", "whitelisted_functions": whitelisted_functions})
        func_to_call_direct_suggestion.invoke()
        result_direct_suggestion = mock_stdout.getvalue().strip()
        self.clear_mock_stdout()

        # Act - less direct suggestion
        func_to_call_indirect_suggestion = chain.invoke({"query": "What's the weather like where you're from?", "whitelisted_functions": whitelisted_functions})
        func_to_call_indirect_suggestion.invoke()
        result_indirect_suggestion = mock_stdout.getvalue().strip()
        self.clear_mock_stdout()

        # Assert - direct suggestion
        self.assertEqual(func_to_call_direct_suggestion, print_to_console)
        #self.assertEqual(result_direct_suggestion, "Green Tomatos")


        # Asset - less direct suggestion
        self.assertEqual(func_to_call_indirect_suggestion, print_to_console)
        #self.assertEqual(result_indirect_suggestion, "The weather is sunny and warm where I'm from.")
        
        self.clear_mock_stdout()



    def test_calling_add_two_numbers_function(self):
        ...

if __name__ == '__main__':
    unittest.main()