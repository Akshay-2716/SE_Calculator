import unittest
from matrix import MatrixOperations
#tested matrix function
class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.m = MatrixOperations()

    def test_add(self):
        self.assertEqual(
            self.m.add("[[1,2],[3,4]]", "[[5,6],[7,8]]"),
            "[[6, 8], [10, 12]]"
        )

    def test_subtract(self):
        self.assertEqual(
            self.m.subtract("[[5,6],[7,8]]", "[[1,2],[3,4]]"),
            "[[4, 4], [4, 4]]"
        )

    def test_multiply(self):
        self.assertEqual(
            self.m.multiply("[[1,2],[3,4]]", "[[5,6],[7,8]]"),
            "[[19, 22], [43, 50]]"
        )

    def test_transpose(self):
        self.assertEqual(
            self.m.transpose("[[1,2,3],[4,5,6]]"),
            "[[1, 4], [2, 5], [3, 6]]"
        )

    def test_invalid_dimension(self):
        with self.assertRaises(ValueError):
            self.m.add("[[1,2]]", "[[1,2],[3,4]]")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.m.parse_matrix("invalid")

if __name__ == "__main__":
    unittest.main()
