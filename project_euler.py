class ProjectEuler:

    def problem_one(self, n):
        """
        If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
        """
        # set initial numbers
        i = 0
        answer = 0
        # as long as i is below N (10, 1000, etc)
        # if it's divisible by 3 or 5
        # add that number with the answer
        while i < n:
            if i % 3 == 0 or i % 5 == 0:
                answer += i
            i += 1

        return answer
