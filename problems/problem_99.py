import requests
from math import log

def largest_exponential():
    "Helpful resource: https://math.stackexchange.com/questions/8308/working-with-large-exponents/8310"
    
    url = "https://projecteuler.net/project/resources/p099_base_exp.txt"
    response = requests.get(url)
    n = n.split('\n')
    n = [x.split(',') for x in n]
    n = [[int(x[0]), int(x[1])] for x in n]
    max_log = max([x[1] * log(x[0]) for x in n])
    answer = n.index([x for x in n if x[1] * log(x[0]) == max_log][0])
    answer += 1
    
    return answer
    
if __name__ == '__main__':
    print(largest_exponential())
