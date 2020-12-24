import pylint1
import adding_Multiplenumbers

class TestAddition(unittest.TestCase):
    
    def test_two_numbers(self):
        B = 2
        result = adding_Multiplenumbers.addNumbers(B)
        self.assertEqual(result, "is not a prime number")
        
    def test_multiple_numbers(self):
        A = 3
        result = adding_Multiplenumbers.addNumbers(B)
        self.assertEqual(result, "is a prime number")
    
#     def test_three_args(self):
#         A= 1
#         B= 2
#         C= 3
#         result = adding_Multiplenumbers.addNumbers(A,B,C)
#         self.assertEqual(result,"Refer to doc string")
        
    
if __name__ == '__main__':
    unittest.main()