import unittest
from project_euler import ProjectEuler

class TestProblemOne(unittest.TestCase):
    project_euler = ProjectEuler()

    def test_problem_one(self):
        answer = self.project_euler.problem_one(1000)

        self.assertEqual(answer, 233168)

    def test_problem_two(self):
        answer = self.project_euler.problem_two(4000000)

        self.assertEqual(answer, 4613732)

    def test_problem_three(self):
        answer = self.project_euler.problem_three(600851475143)

        self.assertEqual(answer, 6857)

if __name__ == "__main__":
    unittest.main()
