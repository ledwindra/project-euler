import unittest
from project_euler import Problems

class TestProblemOne(unittest.TestCase):
    project_euler = Problems()

    def test_problem_one(self):
        answer = self.project_euler.problem_one(1000)

        self.assertEqual(answer, 233168)

    def test_problem_two(self):
        answer = self.project_euler.problem_two(4000000)

        self.assertEqual(answer, 4613732)

    def test_problem_three(self):
        answer = self.project_euler.problem_three(600851475143)

        self.assertEqual(answer, 6857)

    def test_problem_eight(self):
        answer = self.project_euler.problem_eight(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)

        self.assertEqual(answer, 23514624000)

    def test_problem_thirteen(self):
        answer = self.project_euler.problem_thirteen()

        self.assertEqual(answer, 5537376230)

    def test_problem_twenty_two(self):
        answer = self.project_euler.problem_twenty_two()

        self.assertEqual(answer, 871198282)

    def test_problem_twenty_five(self):
        answer = self.project_euler.problem_twenty_five(1000)

        self.assertEqual(answer, 4782)

    def test_problem_thirty_six(self):
        answer = self.project_euler.problem_thirty_six()

        self.assertEqual(answer, 872187)

    def test_problem_thirty_seven(self):
        answer = self.project_euler.problem_thirty_seven()

        self.assertEqual(answer, 748317)

    def test_problem_thirty_nine(self):
        answer = self.project_euler.problem_thirty_nine()

        self.assertEqual(answer, 840)
    
    def test_problem_forty_three(self):
        answer = self.project_euler.problem_forty_three()

        self.assertEqual(answer, 16695334890)

    def test_problem_forty_six(self):
        answer = self.project_euler.problem_forty_six()

        self.assertEqual(answer, 5777)

    def test_problem_forty_seven(self):
        answer = self.project_euler.problem_forty_seven()

        self.assertEqual(answer, 134043)

    def test_problem_ninety_nine(self):
        answer = self.project_euler.problem_ninety_nine()

        self.assertEqual(answer, 709)

if __name__ == "__main__":
    unittest.main()
