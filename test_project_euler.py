import unittest
from project_euler import ProjectEuler

class TestProblemOne(unittest.TestCase):
    project_euler = ProjectEuler()

    def test_problem_one(self):
        answer = self.project_euler.problem_one(1000)

        self.assertEqual(answer, 233168)

if __name__ == "__main__":
    unittest.main()