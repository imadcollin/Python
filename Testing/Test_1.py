"""Using test techniques TDD 

Args: 
None: no thing to pass

Raises:
Exception such as not string 

Returns:
None: Nothing to return 
"""

import unittest 

class StringTest(unittest.TestCase):
    """Test for string length"""

    def test_runner(self):
        stringCheck()

# Main 
if __name__=="__main__":
    unittest.main()