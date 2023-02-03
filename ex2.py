import unittest
def student_score(score):
    if score < 0:
        return "Invalid"
    elif score < 50:
        return "Failed"
    elif score < 65:
        return "Passed"
    elif score < 75:
        return "Good"
    elif score < 85:
        return "Very Good"
    elif score < 100:
        return "Excellent"
    else:
        return "Invalid"

class TestScore(unittest.TestCase):

    def test_below_0(self):
        result = student_score(-8)
        self.assertEqual(result, "Invalid")

    def test_between_0_and_50(self):
        result = student_score(30)
        self.assertEqual(result, "Failed")

    def test_between_50_and_65(self):
        result = student_score(50)
        self.assertEqual(result, "Passed")

    def test_between_65_and_75(self):
        result = student_score(70)
        self.assertEqual(result, "Good")

    def test_between_75_and_85(self):
        result = student_score(80)
        self.assertEqual(result, "Very Good")

    def test_between_85_and_100(self):
        result = student_score(90)
        self.assertEqual(result, "Excellent")

    def test_greater_100(self):
        result = student_score(140)
        self.assertEqual(result, "Invalid")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()

