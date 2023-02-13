#https://projecteuler.net/problem=23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
def intsNotMadeFromAbundants():
    from itertools import compress

    abundants = []
    for i in range(12,28123):
        factor = 0
        for j in range(2,int((i)**0.5)+1):
            if i%j == 0:
                factor+= j + i//j
                if j == (i**0.5):
                    factor -= j
        if factor>i:
            abundants.append(i)
    num_list = [True]*28123
    k = 0
    for i in abundants:
        for j in abundants[k:]:
            if(i+j>28123): break
            num_list[i+j-1] = False
        k+=1
    return sum(compress(range(1,28124),num_list))
print(intsNotMadeFromAbundants())




#https://projecteuler.net/problem=20
#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!
def sumOfDigitsOfFactoring(number):
    n = 1
    for partOfFactor in range(number,0,-1): n*=partOfFactor
    return sum(int(digits) for digits in str(n))
print(sumOfDigitsOfFactoring(10))




#https://projecteuler.net/problem=18
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#    3
#   7 4
#  2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:
#                75
#               95 64
#             17 47 82
#            18 35 87 10
#           20 04 82 47 65
#          19 01 23 75 03 34
#         88 02 77 73 07 63 67
#        99 65 04 28 06 16 70 92
#       41 41 26 56 83 40 80 70 33
#      41 48 72 33 47 32 37 16 94 29
#     53 71 44 65 25 43 91 52 97 51 14
#    70 11 33 28 77 73 17 78 39 68 17 57
#   91 71 52 38 17 14 91 43 58 50 27 29 48
#  63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
# note: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
try:
    with open('triangleDataFile.txt') as data:
        numberIndex=0
        previousNumber=data.readline().rstrip().split()
        summary=int(previousNumber[0])
        for line in data:
            numberSet=line.rstrip().split()
            if numberIndex > 0:
                previousNumber=max(numberSet[numberIndex-1],numberSet[numberIndex],numberSet[numberIndex+1])
                if numberSet[numberIndex-1] == previousNumber: numberIndex-=1
                elif numberSet[numberIndex+1] == previousNumber: numberIndex+=1
            elif numberIndex == 0:
                previousNumber=max(numberSet[numberIndex],numberSet[numberIndex+1])
                if numberSet[numberIndex+1] == previousNumber: numberIndex+=1
            summary+=int(previousNumber)
        print(summary)
except FileNotFoundError:
    print('File Not Found.')




#https://projecteuler.net/problem=17
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
def numbersToWords(number):
    '''
    Positive natural numbers up to (Quintilliard - 1) == (10^33 - 1) 
    '''
    #strings at index 0 and 1, are to make array indexing simple - not used
    #so we will not see "zero zero zero three four two" for 342
    if number == 0: return 'zero'
    ones=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens=['','','twenty ','thirty ','forty ','fifty ','sixty ','seventy ','eighty ','ninety ']

    def helpingFunction(number,addition):
        nString=''
        if number>19:
            #example for 21:  str(21//10=2  +  21%10=1)=twentyone 
            nString+= tens[number//10] + ones[number % 10]
        else:
            nString+= ones[number]
        #checks if number is not 0
        if (number):
            nString+=addition
        return nString

    cout=''
    if len(str(number)) >= 11:
        cout+=helpingFunction(((number//10**31)%10),' hundred ')
        if ((number//10**31)%10) > 0 and ((number//10**30)%100) == 0 and ((number//10**30)%10) == 0: cout+='quintillion '
        cout+=helpingFunction(((number//10**30)%100),' quintillion ')
        cout+=helpingFunction(((number//10**28)%10),' hundred ')
        if ((number//10**28)%10) > 0 and ((number//10**27)%100) == 0 and ((number//10**27)%10) == 0: cout+='quadrilliard '
        cout+=helpingFunction(((number//10**27)%100),' quadrilliard ')
        cout+=helpingFunction(((number//10**26)%10),' hundred ')
        if ((number//10**26)%10) > 0 and ((number//10**24)%100) == 0 and ((number//10**24)%10) == 0: cout+='quadrillion '
        cout+=helpingFunction(((number//10**24)%100),' quadrillion ')
        cout+=helpingFunction(((number//10**23)%10),' hundred ')
        if ((number//10**23)%10) > 0 and ((number//10**21)%100) == 0 and ((number//10**21)%10) == 0: cout+='triliard '
        cout+=helpingFunction(((number//10**21)%100),' triliard ')
        cout+=helpingFunction(((number//10**20)%10),' hundred ')
        if ((number//10**20)%10) > 0 and ((number//10**18)%100) == 0 and ((number//10**18)%10) == 0: cout+='trilion '
        cout+=helpingFunction(((number//10**18)%100),' trilion ')
        cout+=helpingFunction(((number//10**17)%10),' hundred ')
        if ((number//10**17)%10) > 0 and ((number//10**15)%100) == 0 and ((number//10**15)%10) == 0: cout+='biliard '
        cout+=helpingFunction(((number//10**15)%100),' biliard ')
        cout+=helpingFunction(((number//10**14)%10),' hundred ')
        if ((number//10**14)%10) > 0 and ((number//10**12)%100) == 0 and ((number//10**12)%10) == 0: cout+='bilion '
        cout+=helpingFunction(((number//10**12)%100),' bilion ')
        cout+=helpingFunction(((number//10**11)%10),' hundred ')
        if ((number//10**11)%10) > 0 and ((number//10**9)%100) == 0 and ((number//10**9)%10) == 0: cout+='miliard '
    cout+=helpingFunction(((number//10**9)%100),' miliard ')
    cout+=helpingFunction(((number//10**8)%10),' hundred ')
    if ((number//10**8)%10) > 0 and ((number//10**6)%100) == 0 and ((number//10**6)%10) == 0: cout+='milion '
    cout+=helpingFunction(((number//10**6)%100),' milion ')
    cout+=helpingFunction(((number//10**5)%10),' hundred ')
    if ((number//10**5)%10) > 0 and ((number//10**3)%100) == 0 and ((number//10**3)%10) == 0: cout+='thousand '
    cout+=helpingFunction(((number//10**3)%100),' thousand ')
    cout+=helpingFunction(((number//10**2)%10)," hundred ")

    if number > 100 and number % 100:
        cout+='and '
    cout+=helpingFunction((number%100),'')
    return cout
def amountOfLettersOfRangeOfNumbersAfterConversionToWords(fromWhere,toWhere):
    placeholder=''
    for i in range(fromWhere,toWhere+1): placeholder+=numbersToWords(i).strip()
    return len(placeholder)
print(amountOfLettersOfRangeOfNumbersAfterConversionToWords(1,1000))




#https://projecteuler.net/problem=16
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?
def sumOfDigitsOfPoweredNumber(numberToPower, powerForNumber):
    return sum(int(digits) for digits in str((numberToPower**powerForNumber)))
print(sumOfDigitsOfPoweredNumber(2,1000))




#https://projecteuler.net/problem=15
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?
def latticePathsOfSquaredGrids(gridLength):
    setElements = gridLength*2
    n = 1
    k = 1
    for i in range(gridLength,0,-1):
        k*=i
    for j in range(setElements,0,-1):
        n*=j
    return int(n/(k*k))
print(latticePathsOfSquaredGrids(20))




#https://projecteuler.net/problem=14
#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#note: Once the chain starts the terms are allowed to go above one million.
def longestCollatzSequence(rangeOfScope):
    length = 0
    for x in range(1, rangeOfScope+1):
        tmpLength = 1
        while x != 1:
            if x % 2 == 0: x/=2
            elif x % 2 == 1: (x:=x*3+1)
            tmpLength += 1
        if length < tmpLength: length = tmpLength
    return length
print(longestCollatzSequence(999999))




#https://projecteuler.net/problem=12
#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#Let us list the factors of the first seven triangle numbers:
#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.
#What is the value of the first triangle number to have over five hundred divisors?
def firstTriangularNumberToHaveOverGivenDivisors(amountOfDivisors):
    #loop for making triangular numbers
    from itertools import count
    tn=0
    divisors=[]
    for i in count(1):
        tn+=i
        for j in range(1,int((tn**0.5)+1)):
            if (tn/int(j))%1 == 0:
                divisors.append(j)
                divisors.append(int(tn/j))
        if len(divisors) > amountOfDivisors:
            return tn
        else:
            divisors.clear()
print(firstTriangularNumberToHaveOverGivenDivisors(500))




#https://projecteuler.net/problem=10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
def isprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def sumOfPrimesBelowThreshold(threshold):
    allPrimesBelowThreshold = []
    for i in range(2,threshold):
        if isprime(i):
            allPrimesBelowThreshold.append(i)
    return sum(allPrimesBelowThreshold)
print(sumOfPrimesBelowThreshold(10))




#https://projecteuler.net/problem=9
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 3^2 + 4^2 = 5^2      9 + 16 = 25
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
for b in range(1, 500):
    if 1000*(500-b) % (1000-b) == 0:
        print(b)
'''
it gives 200 and 375 as a result for b, so a is one of it too
and you get c by from 1000 substracting 200+375
'''




#https://projecteuler.net/problem=8
#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
data = '''73167176531330624919225119674426574742355349194934
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
71636269561882670428252483600823257530420752963450'''.replace("\n","")
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
def adjacentNumbers(adj):
    maxProduct = 0
    maxSet = 0
    startFrom = 0
    while startFrom < len(data)-adj:
        adjSet = data[startFrom:startFrom+adj]
        if "0" in adjSet:
            startFrom+= 1
        else:
            product = 1
            for i in adjSet: 
                product *= int(i)
            if maxProduct < product:
                maxProduct = product
                product = 1
                if maxSet != adjSet:
                    maxSet = adjSet
            startFrom+= 1
    return maxSet
print(adjacentNumbers(13))




#https://projecteuler.net/problem=7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
def isprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def desiredPrimeNumber(number):
    from itertools import count
    listOfPrimes = []
    counter = 0
    for i in count(2):
        if isprime(i) == True: 
            listOfPrimes.append(i)
            counter+=1
            if counter == number:
                return listOfPrimes[-1]
print(desiredPrimeNumber(10001))




#https://projecteuler.net/problem=6
#The sum of the squares of the first ten natural numbers is, $$1^2 + 2^2 + ... + 10^2 = 385$$
#The square of the sum of the first ten natural numbers is, $$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def sumSquareDifferences(number): #how many first natural numbers
    squaredEach = 0
    for i in range(number+1):
        squaredEach += i**2
    return sum(range(number+1))**2 - squaredEach
print(sumSquareDifferences(100))




#https://projecteuler.net/problem=5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def lcm(theMaxNumber): #like from 1 to 10(theMaxNumber)       #with 20 the output will be too long to display
    found = False
    i = theMaxNumber
    while found==False:
        c = 0    # c checks if the number is the one im looking for
        for x in range(1,theMaxNumber+1):
            if i%x==0:
                c = c + 1
        if c==theMaxNumber: # if c == theMaxNumber then its the number im looking for
            print(i)
            found = True
        i = i + 1
lcm(10)




#https://projecteuler.net/problem=4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
def highestPalindrome():
    for i in range(999,900,-1):
        for j in range(999,900,-1):
            number = j*i
            if f"{number}" == f"{number}"[::-1]:
                return number
print(highestPalindrome())




# https://projecteuler.net/problem=2
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def fibonacci(maxValue):
    n1=1;n2=2;sum=n2
    while True:
        new= n1 + n2
        if new > maxValue:
            break
        if new % 2 == 0:
            sum += new
        n1=n2;n2=new
    return sum
print(fibonacci(4000000))




# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def multiples(number): 
    summary = 0
    for i in range(number):
        if i % 3 ==0 or i % 5 ==0:
            summary += i
    return summary
print(multiples(1000))