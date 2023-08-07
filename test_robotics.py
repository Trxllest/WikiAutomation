import unittest
from robotics import Robot
import datetime

class RobotTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case by creating a Robot instance.
        """
        self.robot = Robot("TestBot")

    def test_extract_info(self):
        """
        Test the extract_info method of the Robot class.
        """
        self.robot.open_webpage(["Albert Einstein"])
        info = self.robot.extract_info()
        self.assertIsNotNone(info)
        self.assertEqual(len(info), 4)
        self.assertIsInstance(info[0],  datetime.date)  # Birth date
        self.assertIsInstance(info[1], datetime.date)  # Death date
        self.assertIsInstance(info[2], str)  # First paragraph
        self.assertIsInstance(info[3], (int, str))  # Age

    def test_get_date(self):
        """
        Test the get_date method of the Robot class.
        """
        date = self.robot.get_date("//td[@class='infobox-data']")
        self.assertIsNotNone(date)

    def test_open_webpage(self):
        """
        Test the open_webpage method of the Robot class.
        """
        self.robot.open_webpage(["Marie Curie"])
        self.assertEqual(len(self.robot.summaries), 1)

if __name__ == '__main__':
    unittest.main()
