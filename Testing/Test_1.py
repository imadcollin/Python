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

## Add pass function 
def stringCheck():
    pass


# Main 
if __name__=="__main__":
    unittest.main()