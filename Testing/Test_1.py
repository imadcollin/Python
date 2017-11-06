"""Using test techniques TDD 

Args: 
None: no thing to pass

Raises:
Exception such as not string 

Returns:
None: Nothing to return 
"""

import unittest 

 ## Add pass function 
def stringCheck(str):
    pass

class StringTest(unittest.TestCase):
    """Test for string length"""

 
    def setUp(self):
        """ Fixture that creates a string """
        self.str="This is a string"

    def tearDown(self):
        """Fixture that remove the strings """
        try:
            self.str=""
        except:
            pass 

    def test_runner(self):
         stringCheck(self.str)

   
    
# Main 
if __name__=="__main__":
    unittest.main()