import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        hum1 = runner.Runner('Степаныч')
        for i in range(10):
            hum1.walk()

        self.assertEqual(hum1.distance, 50)

    def test_run(self):
        hum1 = runner.Runner('Степаныч')
        for i in range(10):
            hum1.run()

        self.assertEqual(hum1.distance, 100)

    def test_challenge(self):
        hum1 = runner.Runner('Степаныч')
        hum2 = runner.Runner('Петрович')
        for i in range(10):
            hum1.walk()
            hum2.run()

        self.assertNotEqual(hum1.distance, 150)

if __name__ == '__main__':
    unittest.main()
