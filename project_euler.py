import itertools
import numpy as np
import re
import requests
import string
from math import log
from mpmath import mp

class Problems:

    def problem_one(self, n):
        """
        If we list all the natural numbers below 10 that are multiples of 3 or 5,
        we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of
        all the multiples of 3 or 5 below 1000.
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
    
    def problem_two(self, n):
        """
        Each new term in the Fibonacci sequence is generated by adding the
        previous two terms. By starting with 1 and 2, the first 10 terms will
        be:
        
        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
        
        By considering the terms in the Fibonacci sequence whose values do not
        exceed four million, find the sum of the even-valued terms.
        """
        # set intial fibonacci numbers
        fibonacci = [0, 1]
        while fibonacci[-1] < n:
            fibonacci.append(fibonacci[-2] + fibonacci[-1])
        
        # use list comprehension to even select fibonacci numbers
        # then add all of them
        even = [x for x in fibonacci if x % 2 == 0]
        even = sum(even)
        
        return even

    def problem_three(self, n):
        """
        The prime factors of 13195 are 5, 7, 13 and 29.

        What is the largest prime factor of the number 600851475143?
        """
        # n is the number whose prime factors we would like to search for
        # in this case, it's either 13195 or 600851475143
        # we don't want to iterate all over from 0 to n to get the primes
        # instead, we stop until the square root of n (it's enough, and faster)
        sqrt_n = int(n ** 0.5)
        def is_prime(x):
            """
            Returns whether a number is a prime or not
            """
            sqrt_n = int(x ** 0.5)
            for i in range(2, sqrt_n + 1):
                if x % i == 0:
                    return False
            return True
        
        # use list comprehension to find the largest prime factors of n
        answer = [x for x in range(2, sqrt_n) if is_prime(x) == True and n % x == 0]
        answer = max(answer)

        return answer
    
    def problem_eight(self, digit):
        """
        The four adjacent digits in the 1000-digit number that have the greatest
        product are 9 × 9 × 8 × 9 = 5832.

        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450

        Find the thirteen adjacent digits in the 1000-digit number that have the
        greatest product. What is the value of this product?
        """
        digit = str(digit)
        four = [digit[x : (x + 13)] for x in range(len(digit))]
        multiplier = []
        i = 0
        while i < len(four):
            m = 1
            for j in four[i]:
                m *= int(j)
            multiplier.append(m)
            i += 1
        max_multiplier = max(multiplier)
        for i in range(len(four)):
            m = 1
            for j in four[i]:
                m *= int(j)
                if m == max_multiplier:
                    return max_multiplier

    def problem_twelve(self):
        def is_prime(x):
            sqrt_n = int(x ** 0.5)
            for i in range(2, sqrt_n + 1):
                if x % i == 0:
                    return False
            return True

        def prime_list():
            pl = [x for x in range(100000) if is_prime(x) == True][2:]
            print("Calculating prime list: DONE")

            return pl

        def seq(n):
            var = 1
            _ = [n]
            while (n - var) != 0:
                _.append((n - var))
                var += 1
            
            return sum(_)

        def prime_factor(n, pl):
            i = 0
            p = pl[i]
            f = []
            while n != 1:
                if n % p == 0:
                    f.append(p)
                    n /= p
                else:
                    i += 1
                    p = pl[i]
            
            return f

        def divisor(n):
            l = prime_factor(n, pl)
            sl = list(set(l))
            sl = [l.count(x) for x in sl]
            result = [x + 1 for x in sl]
            result = np.prod(np.array(result))

            return result

        pl = prime_list()
        for i in range(10000, 20000):
            s = seq(i)
            d = divisor(s)
            print(i, s, d)
            if d > 500:
                print(i, s, d)
                break

    def problem_thirteen(self):
        """
        Work out the first ten digits of the sum of the following one-hundred
        50-digit numbers.
        """
        digit = """
        37107287533902102798797998220837590246510135740250
        46376937677490009712648124896970078050417018260538
        74324986199524741059474233309513058123726617309629
        91942213363574161572522430563301811072406154908250
        23067588207539346171171980310421047513778063246676
        89261670696623633820136378418383684178734361726757
        28112879812849979408065481931592621691275889832738
        44274228917432520321923589422876796487670272189318
        47451445736001306439091167216856844588711603153276
        70386486105843025439939619828917593665686757934951
        62176457141856560629502157223196586755079324193331
        64906352462741904929101432445813822663347944758178
        92575867718337217661963751590579239728245598838407
        58203565325359399008402633568948830189458628227828
        80181199384826282014278194139940567587151170094390
        35398664372827112653829987240784473053190104293586
        86515506006295864861532075273371959191420517255829
        71693888707715466499115593487603532921714970056938
        54370070576826684624621495650076471787294438377604
        53282654108756828443191190634694037855217779295145
        36123272525000296071075082563815656710885258350721
        45876576172410976447339110607218265236877223636045
        17423706905851860660448207621209813287860733969412
        81142660418086830619328460811191061556940512689692
        51934325451728388641918047049293215058642563049483
        62467221648435076201727918039944693004732956340691
        15732444386908125794514089057706229429197107928209
        55037687525678773091862540744969844508330393682126
        18336384825330154686196124348767681297534375946515
        80386287592878490201521685554828717201219257766954
        78182833757993103614740356856449095527097864797581
        16726320100436897842553539920931837441497806860984
        48403098129077791799088218795327364475675590848030
        87086987551392711854517078544161852424320693150332
        59959406895756536782107074926966537676326235447210
        69793950679652694742597709739166693763042633987085
        41052684708299085211399427365734116182760315001271
        65378607361501080857009149939512557028198746004375
        35829035317434717326932123578154982629742552737307
        94953759765105305946966067683156574377167401875275
        88902802571733229619176668713819931811048770190271
        25267680276078003013678680992525463401061632866526
        36270218540497705585629946580636237993140746255962
        24074486908231174977792365466257246923322810917141
        91430288197103288597806669760892938638285025333403
        34413065578016127815921815005561868836468420090470
        23053081172816430487623791969842487255036638784583
        11487696932154902810424020138335124462181441773470
        63783299490636259666498587618221225225512486764533
        67720186971698544312419572409913959008952310058822
        95548255300263520781532296796249481641953868218774
        76085327132285723110424803456124867697064507995236
        37774242535411291684276865538926205024910326572967
        23701913275725675285653248258265463092207058596522
        29798860272258331913126375147341994889534765745501
        18495701454879288984856827726077713721403798879715
        38298203783031473527721580348144513491373226651381
        34829543829199918180278916522431027392251122869539
        40957953066405232632538044100059654939159879593635
        29746152185502371307642255121183693803580388584903
        41698116222072977186158236678424689157993532961922
        62467957194401269043877107275048102390895523597457
        23189706772547915061505504953922979530901129967519
        86188088225875314529584099251203829009407770775672
        11306739708304724483816533873502340845647058077308
        82959174767140363198008187129011875491310547126581
        97623331044818386269515456334926366572897563400500
        42846280183517070527831839425882145521227251250327
        55121603546981200581762165212827652751691296897789
        32238195734329339946437501907836945765883352399886
        75506164965184775180738168837861091527357929701337
        62177842752192623401942399639168044983993173312731
        32924185707147349566916674687634660915035914677504
        99518671430235219628894890102423325116913619626622
        73267460800591547471830798392868535206946944540724
        76841822524674417161514036427982273348055556214818
        97142617910342598647204516893989422179826088076852
        87783646182799346313767754307809363333018982642090
        10848802521674670883215120185883543223812876952786
        71329612474782464538636993009049310363619763878039
        62184073572399794223406235393808339651327408011116
        66627891981488087797941876876144230030984490851411
        60661826293682836764744779239180335110989069790714
        85786944089552990653640447425576083659976645795096
        66024396409905389607120198219976047599490197230297
        64913982680032973156037120041377903785566085089252
        16730939319872750275468906903707539413042652315011
        94809377245048795150954100921645863754710598436791
        78639167021187492431995700641917969777599028300699
        15368713711936614952811305876380278410754449733078
        40789923115535562561142322423255033685442488917353
        44889911501440648020369068063960672322193204149535
        41503128880339536053299340368006977710650566631954
        81234880673210146739058568557934581403627822703280
        82616570773948327592232845941706525094512325230608
        22918802058777319719839450180888072429661980811197
        77158542502016545090413245809786882778948721859617
        72107838435069186155435662884062257473692284509516
        20849603980134001723930671666823555245252804609722
        53503534226472524250874054075591789781264330331690
        """
        digit = [x for x in digit.split('\n')]
        digit = [x.replace(' ', '') for x in digit]
        digit = [x for x in digit if x != '']
        digit = [int(x) for x in digit]
        digit = sum(digit)
        digit = str(digit)[:10]
        digit = int(digit)
        
        return digit
    
    def problem_twenty_two(self):
        """
        Using names.txt (right click and 'Save Link/Target As...'), a 46K text
        file containing over five-thousand first names, begin by sorting it into
        alphabetical order. Then working out the alphabetical value for each
        name, multiply this value by its alphabetical position in the list to
        obtain a name score.

        For example, when the list is sorted into alphabetical order, COLIN,
        which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
        So, COLIN would obtain a score of 938 × 53 = 49714.

        What is the total of all the name scores in the file?
        """
        url='https://projecteuler.net/project/resources/p022_names.txt'
        res = requests.get(url)
        alphabet = [x for x in string.ascii_uppercase]
        alphabet = [(alphabet[x], alphabet[x].replace(alphabet[x], str(x+1))) for x in range(len(alphabet))]
        alphabet = dict(alphabet)
        names = res.text.split(',')
        names = [re.sub(r'[^\w\s]','', x) for x in names]
        names = sorted(names)
        # convert alphabet to its numeric position for each name
        scores = []
        for name in names:
            scores.append([int(alphabet[x]) for x in name])
        # sum the score for each name
        scores = [sum(x) * (scores.index(x) + 1) for x in scores]
        answer = sum(scores)

        return answer

    def problem_twenty_five(self, n):
        """
        The Fibonacci sequence is defined by the recurrence relation:

            Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

        Hence the first 12 terms will be:

            F1 = 1
            F2 = 1
            F3 = 2
            F4 = 3
            F5 = 5
            F6 = 8
            F7 = 13
            F8 = 21
            F9 = 34
            F10 = 55
            F11 = 89
            F12 = 144

        The 12th term, F12, is the first term to contain three digits.

        What is the index of the first term in the Fibonacci sequence to contain
        1000 digits?
        """
        fibonacci = [0, 1]
        while len(str(fibonacci[-1])) < n:
            fibonacci.append(fibonacci[-2] + fibonacci[-1])
        fibonacci = len(fibonacci[1:])

        return fibonacci

    def problem_twenty_six(self):
        mp.dps = 200
        for i in range(2, 1000):
            div = mp.fdiv(1, i)
            d = str(div).split(".")[1]
            _ = d[:100]
            if len(_) == 100:
                c = d.count(_)
                if c > 1:
                    print(i, _, d)

    def problem_thirty_six(self):
        """
        The decimal number, 585 = 10010010012 (binary), is palindromic in both
        bases. Find the sum of all numbers, less than one million, which are
        palindromic in base 10 and base 2. (Please note that the palindromic
        number, in either base, may not include leading zeros.)
        """
        # make a tuple that consists of base-10 and base-2 numbers < 1 million
        array = [(x, bin(x)[2:]) for x in range(1, 1000000)]
        # a function that detects whether or not a number is palindromic
        is_palindrome = lambda x: str(x) == str(x)[::-1]
        # list comprehension to get palindromes and sum them up
        palindrome = [x[0] for x in array if is_palindrome(x[0]) == True and is_palindrome(x[1]) == True]
        answer = sum(palindrome)

        return answer

    def problem_thirty_seven(self):
        """
        The number 3797 has an interesting property. Being prime itself, it is
        possible to continuously remove digits from left to right, and remain
        prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
        right to left: 3797, 379, 37, and 3. Find the sum of the only eleven
        primes that are both truncatable from left to right and right to left.
        NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
        """
        def is_prime(n):
            # returns True if prime and n > 1
            if n > 1:
                sqrt_n = int(n ** 0.5)
                for i in range(2, sqrt_n + 1):
                    if n % i == 0:
                        return False
                return True
            return False

        def truncate_prime(n, index):
            str_n = str(n)
            len_n = len(str_n)
            i = 0
            while i < len_n:
                list_n = [x for x in str_n]
                if not is_prime(int(str_n)):
                    break
                # index is either 0 or -1
                # 0 = truncate from left
                # -1 = truncate from right
                list_n.pop(index)
                str_n = ''.join(list_n)
                i += 1
            
            return str_n

        truncate = []
        n = 11
        while len(truncate) != 11:
            if is_prime(n):
                if truncate_prime(n, 0) == '' and truncate_prime(n, -1) == '':
                    truncate.append(n)
            n += 1

        answer = sum(truncate)

        return answer
    
    def problem_thirty_nine(self):
        """
        If p is the perimeter of a right angle triangle with integral length
        sides, {a,b,c}, there are exactly three solutions for p = 120.

        {20,48,52}, {24,45,51}, {30,40,50}

        For which value of p ≤ 1000, is the number of solutions maximised?
        """
        # a^2 + b^2 = c^2
        # a + b + c = p
        # c^2 = (p - a - b)^2 
        p = 1
        maximized = []
        while p <= 1000:
            # halving and finding the root of p so that we don't iterate all of its numbers
            half_p = int(p / 2)
            sqrt_p = int(p ** 0.5)
            equation = lambda x, y, p: (x ** 2) + (y ** 2) == (p - x - y) ** 2
            solutions = []
            for a in range(sqrt_p, half_p):
                for b in range(sqrt_p, half_p):
                    if equation(a, b, p) and sorted([a, b]) not in solutions:
                        solutions.append([a, b])
            maximized.append((str(p), len(solutions)))
            p += 1
        max_value = max(dict(maximized).values())
        answer = int([x[0] for x in maximized if x[1] == max_value][0])

        return answer

    def problem_forty_three(self):
        """
        The number, 1406357289, is a 0 to 9 pandigital number because it is made
        up of each of the digits 0 to 9 in some order, but it also has a rather 
        interesting sub-string divisibility property.

        Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way,
        we note the following:

            d2d3d4=406 is divisible by 2
            d3d4d5=063 is divisible by 3
            d4d5d6=635 is divisible by 5
            d5d6d7=357 is divisible by 7
            d6d7d8=572 is divisible by 11
            d7d8d9=728 is divisible by 13
            d8d9d10=289 is divisible by 17

        Find the sum of all 0 to 9 pandigital numbers with this property.
        """
        # find all possible numbers composed from 0 to 9, each must have 10 digits
        digit = string.digits
        permutation = list(itertools.permutations(digit, len(digit)))
        def is_prime(n):
            # returns True if prime and n > 1
            if n > 1:
                sqrt_n = int(n ** 0.5)
                for i in range(2, sqrt_n + 1):
                    if n % i == 0:
                        return False
                return True
            return False

        def pandigital_number(num):
            # find the first 7 prime numbers
            prime = [x for x in range(18) if is_prime(x) == True]
            for i in range(1, 8):
                meet_condition = int(num[i]+num[i+1]+num[i+2]) % prime[i-1] == 0
                if not meet_condition:
                    return False
            return True

        # use list comprehension to find pandigital number that meets the condition
        # then sum all of them
        answer = [x for x in permutation if pandigital_number(x) == True]
        answer = sum([int(''.join(x)) for x in answer])

        return answer
    
    def problem_forty_five(self):
        t = lambda n: n * (n + 1) / 2
        p = lambda n: n * ((3 * n) - 1) / 2
        h = lambda n: n * ((2 * n) - 1)

        for i in range(286, 1000):
            for j in range(166, 500):
                for k in range(144, 500):
                    if t(i) == p(j) == h(k):
                        print(t(i))

    def problem_forty_six(self, n=6000):
        """
        Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first
        ten pentagonal numbers are:

        1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

        It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their
        difference, 70 − 22 = 48, is not pentagonal.

        Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
        difference are pentagonal and D = |Pk − Pj| is minimised; what is the
        value of D?
        """
        def is_prime(n):
            # returns True if prime and n > 1
            if n > 1:
                sqrt_n = int(n ** 0.5)
                for i in range(2, sqrt_n + 1):
                    if n % i == 0:
                        return False
                return True
            return False

        odd_composite = [x for x in range(9, n+1) if is_prime(x) == False and x % 2 != 0]
        composites = []
        for odd in odd_composite:
            primes = [x for x in range(odd) if is_prime(x) == True]
            i = 0
            while i < len(primes):
                for j in range(1, int(odd ** 0.5)):
                    equation = primes[i] + (2 * (j ** 2))
                    if equation == odd:
                        composites.append(odd)
                i += 1
        answer = [x for x in odd_composite if x not in set(composites)][0]

        return answer

    def problem_forty_seven(self, i=0, n=4):
        """
        The first two consecutive numbers to have two distinct prime factors
        are:

        14 = 2 × 7
        15 = 3 × 5

        The first three consecutive numbers to have three distinct prime factors
        are:

        644 = 2² × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19.

        Find the first four consecutive integers to have four distinct prime
        factors each. What is the first of these numbers?
        """
        def is_prime(n):
            # returns true if prime
            sqrt_n = int(n ** 0.5)
            for i in range(2, sqrt_n + 1):
                if n % i == 0:
                    return False
            return True

        def prime_factors(n, distinct_prime):
            # count how many primes given n
            primes = [x for x in range(2, int(n/2)+1) if n % x == 0 and is_prime(x) == True]
            # check if total primes is equal to expected distict prime
            if len(primes) == distinct_prime:
                while n != 1:
                    if n % primes[0] == 0:
                        n /= primes[0]
                    else:
                        primes.pop(0)

            # end result should return 1
            return n
        
        consecutive = []
        # as long as the length is not as expected
        while len(consecutive) != n:
            # check prime factor of n, append to list if it meets condition
            if not is_prime(i) and prime_factors(i, n) == 1:
                consecutive.append(i)
                # if list has reached the expected length
                # check the delta of its max and min
                # if the delta doesn't equal n - 1, remove its first element
                if len(consecutive) == n and abs(consecutive[0] - consecutive[-1]) != (n-1):
                    consecutive.pop(0)
            i += 1
        
        # the list should contain consecutive numbers
        # the answer should return its first element
        answer = consecutive[0]
        return answer

    def problem_ninety_nine(self):
        """
        Comparing two numbers written in index form like 211 and 37 is not
        difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

        However, confirming that 632382518061 > 519432525806 would be much more 
        difficult, as both numbers contain over three million digits.

        Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K
        text file containing one thousand lines with a base/exponent pair on
        each line, determine which line number has the greatest numerical value.

        NOTE: The first two lines in the file represent the numbers in the
        example given above.
        """
        # helpful resource: https://math.stackexchange.com/questions/8308/working-with-large-exponents/8310
        url='https://projecteuler.net/project/resources/p099_base_exp.txt'
        response = requests.get(url)
        n = response.text.split('\n')
        n = [x.split(',') for x in n]
        n = [[int(x[0]), int(x[1])] for x in n]
        max_log = max([x[1] * log(x[0]) for x in n])
        answer = n.index([x for x in n if x[1] * log(x[0]) == max_log][0])
        answer += 1
        
        return answer
