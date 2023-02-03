
import unittest

def car_speed(speed):
    if speed < 0:
        return "Invalid"
    elif 0 <= speed < 40:
        return "Low"
    elif 40 <= speed < 120:
        return "Normal"
    elif 120 <= speed < 200:
        return "High"
    elif 200 <= speed < 220:
        return "V.High"
    elif 220 < speed:
        return "Invalid"

class TestCarSpeed(unittest.TestCase):

    def test_invalid_speed(self):
        result = car_speed(-8)
        self.assertEqual(result, "Invalid")

    def test_low_speed(self):
        result = car_speed(20)
        self.assertEqual(result, "Low")

    def test_normal_speed(self):
        result = car_speed(80)
        self.assertEqual(result, "Normal")

    def test_high_speed(self):
        result = car_speed(160)
        self.assertEqual(result, "High")

    def test_vhigh_speed(self):
        result = car_speed(210)
        self.assertEqual(result, "V.High")

    def test_exceed_speed(self):
        result = car_speed(300)
        self.assertEqual(result, "Invalid")

if __name__ == '__main__':
    unittest.main()
