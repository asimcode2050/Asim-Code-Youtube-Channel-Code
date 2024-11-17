import unittest


def add(a, b):
    return a + b


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add(-3, -5)  # Call the function with two negative numbers
        self.assertEqual(result, -8)

    def test_add_positive_and_negative(self):
        result = add(10, -3)
        self.assertEqual(result, 7)

    def test_add_with_zero(self):
        result = add(0, 5)
        self.assertEqual(result, 5)  # Check if the result is 5 (0 + 5 = 5)

    def test_add_zero_and_negative(self):
        result = add(0, -5)
        self.assertEqual(result, -5)  # Check if the result is -5 (0 + -5 = -5)


if __name__ == '__main__':
    unittest.main()
