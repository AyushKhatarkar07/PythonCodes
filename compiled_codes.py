import math
import string
import itertools
from operator import itemgetter
import re # regular expression
import random
import zlib
import datetime

''' 25, 46-53 To-do questions '''
req = int(input("Please enter a question number you want the solution of: \n"))

'''1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

if req == 1 :
    for num in range(2000, 3201):
        if num%7 == 0 and num%5 != 0 :
            print(num)
            

'''       
2.Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
def factorial(x):
    ret = 1
    for i in range(1,x+1):
        ret *= i
    return ret
    
if req == 2:
    nums = int(input("enter the total input number: \n"))
    list_nums = list()
    fact = list()
    for i in range(0, nums):
        x = int(input("Enter values of which you want the factorial: \n"))
        list_nums.append(x)
        fact.append(factorial(x))
    
    for factors in fact:
        print(factors, end=", ")
        
'''
3.With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''
if req == 3:
    n = int(input("Enter the number: \n"))
    ret = {}
    for i in range(1, n+1):
        ret.update({i: i*i})
    print(ret)
    
'''
4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
[' 34 ', ' 67 ', ' 55 ', ' 33 ', ' 12 ', ' 98 ']
(' 34 ', ' 67 ', ' 55 ', ' 33 ', ' 12 ', ' 98 ')

'''

if req == 4:
    string = input("enter the csv of numbers")
    ret = string.split(', ')
    print(ret)
    tup = tuple(ret)
    print(tup)


'''
5.Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

if req == 5:
    class String:
        # An attemp to simulate a string 
        def __init__(self):
            pass
        def getString(self):
            self.string = input("Enter a string: \n")
        
        def printString(self):
            print(self.string)
    
    myString = String()
    myString.getString()
    myString.printString()


'''
6.Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

'''

if req == 6:
    c = 50
    h = 30
    string = input("Enter the csv: \n")
    d = string.split(', ')
    for num in d:
        num = math.floor(float(num))
        val = math.sqrt((2*c*int(num))/h)
        print(math.floor(val),end=",")
    
'''
7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,..,Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

'''

if req == 7:
    x = int(input("enter rows"))
    y = int(input("enter cols"))
    arr = [[0 for i in range(y)] for j in range(x)]
    for i in range(x):
        for j in range(y):
            arr[i][j] = i*j
    print(arr)


'''
96.Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

x+y=35
4x+2y=94

'''

if req == 96:
    dic = {}
    for rabbits in range(0,36):
        if 4*rabbits+2*(35-rabbits) == 94 :
            dic.update({rabbits:35-rabbits})
    print(dic)


'''
95.Please write a program which prints all permutations of [1,2,3]
'''

if req == 95:
    lists = list(itertools.permutations([1,2,3]))
    print(lists)

'''
94.Please write a program which accepts a string from console and print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld
'''

if req == 94:
    String = input ("String input\n") 
    String = String[::2]
    print (String) 

'''
92.Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

'''

if req == 92:
    dic = dict()
    strs = input("String")
    for character in strs:
        if dic.get(character, 0) == 0:
            dic[character] = 1
        else:
            dic[character] += 1
        
    print(dic)

'''

8.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

'''
if req == 8:
    csv_string = input("Enter the csv to get the sorted csv: \n")
    str_list = csv_string.split(',')
    sort_list = sorted(str_list)
    sort_csv = ','.join(sort_list)
    print(sort_csv)
     

'''
9.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

if req == 9:
    lines = input("Enter the number of lines of input \n")
    out_list = list()
    for i in range(int(lines)):
        input_str = input("Enter a string containing multiple words:\n")
        input_str_upper = input_str.upper()
        out_list.append(input_str_upper)
    for string in out_list:
        print(string)

'''
10.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

'''
if req == 10:
    input_str = input("Enter the input string: \n")
    input_list = input_str.split(' ')
    list_set = set(input_list)
    input_list = list(list_set)
    input_list = sorted(input_list)
    out_str = ' '.join(input_list)
    print(out_str)

'''
11.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''

if req == 11:
    input_str = input("Enter the input csv string: \n")
    input_list = input_str.split(',')
    out_list = []
    ss = list()
    for string in input_list:
        out_list.append(int(string, 2))
    for i in range(0, len(out_list)):
        print(out_list[i], end = " ")
        if out_list[i]%5 == 0 :
            ss.append(input_list[i])
    out_str = ','.join(ss)
    print(out_str)

'''

12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

'''
# 1st method
if req == 12:
    import math
    output_list = list()
    for nums in range(2000, 2890):
        num = int(nums)
        flag = True
        while num > 0 :
            temp = int(num%10)
            if (temp)%2 != 0 :
                flag = False
                break
            num = int(math.floor(num/10))
        if flag == True :
            output_list.append(str(nums))
    output_str = ','.join(output_list)
    print(output_str)

'''

14.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

if req == 14:
    input_str = input("Enter a string which contains lowercase and uppercase letters: \n")
    lower_cnt , upper_cnt = 0, 0
    for char in input_str:
        if char.isalpha() == True :
            if char.upper() == char :
                upper_cnt += 1
            else :
                lower_cnt += 1
    print("UPPER CASE " + str(upper_cnt))
    print("LOWER CASE " + str(lower_cnt))

'''
13.Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
if req == 13 :
    letter, digit = 0, 0
    input_str = input("Enter the input sentence: \n")
    for char in input_str :
        if char.isalpha() == True :
            letter += 1
        elif char.isnumeric() == True :
            digit += 1
        else :
            continue
    print("LETTERS " + str(letter))
    print("DIGITS " + str(digit))

'''
15.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
if req == 15:
    x = str(input("Enter an integer between 0-9 \n"))
    summ = 0
    string = ''
    for i in range(4):
        string += x
        summ += int(string)
    print(summ)

'''

16.Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''
if req == 16:
    input_str = input("Enter a list of numbers in csv type : \n")
    input_list = input_str.split(',')
    output_list = input_list[::2]
    output_str = ','.join(output_list)
    print(output_str)
    
'''
17.Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
where,
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
if req == 17:
    tot_transact = int(input("Enter the total no. of transactions: \n"))
    final_sum = 0
    for num in range(tot_transact):
        val = input("Enter the details \n")
        if val[0:2] == "D ":
            final_sum += int(val[2:])
        elif val[0:2] == "W ":
            final_sum -= int(val[2:])
        else :
            continue
    print(final_sum)

'''
18.A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
if req == 18:
    input_str = input("Enter the passwords in csv type: \n")
    input_list = input_str.split(',')
    output_list = list()
    for password in input_list:
        small, full, num, special = 0, 0, 0, 0
        for char in password:
            if char.isnumeric() == True:
                num += 1
            elif char.isalpha()==True and char.isupper()==True:
                full += 1
            elif char.isalpha()==True and char.islower()==True:
                small += 1
            elif char == '@' or char == '#' or char == '$' :
                special += 1
            else :
                special = 0
                break
        if small!=0 and full!=0 and special!=0 and num!=0 :
            output_list.append(password)
    output_str = ','.join(output_list)
    print(output_str)
    
'''
19.You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''
if req == 19 :
    # Using itemgetter for multiple levels of sorting
    num_tuples = int(input("Please ebter the number of tuples \n"))
    input_list = list(tuple(map(str, input().split(','))) for r in range(num_tuples))
    input_list = sorted(input_list, key=itemgetter(0,1,2))
    print(input_list)
    
'''

20.Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''
if req == 20 :
    class itr(object):
    	def __init__(self, num) :
    		super(itr, self).__init__()
    		self.num = num
    		
    	def divide(self):
    		for i in range(0, self.num) :
    			if i%7 == 0 :
    				yield i
    
    num = int(input("Enter a number n: \n"))
    for nums in itr(num).divide():
    	print(nums)
    	
'''
21.A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
where,
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''

if req == 21:
    movements = int(input("Enter the number of movements: \n"))
    x,y = 0, 0
    for i in range(movements):
        string = input("enter the string in format; UP 4 : \n")
        ss, num = string.split(' ')
        if ss=='UP':
            y += int(num)
        elif ss=='DOWN':
            y -= int(num)
        elif ss=='LEFT':
            x -= int(num)
        elif ss=='RIGHT':
            x += int(num)
    val = math.sqrt(x*x + y*y)
    val = int(round(val))
    print(val)

'''
22.Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''
if req == 22:
    string = input("ENter a string: \n")
    input_list = string.split(' ')
    freq = dict()
    for word in input_list:
        if freq.get(word, 0) == 0:
            freq.update({word : 1})
        else :
            freq.update({word : int(freq.get(word))+1})
    print(freq)
    output_freq = sorted(freq, key=itemgetter(0))
    for word in output_freq:
        print(word + ':' + str(freq.get(word)))


'''

23.Write a method which can calculate square value of number

Hints:
    Using the ** operator
    
'''
if req == 23:
    num = int(input('Enter a number you want square of: \n'))
    print(num**2)

'''
24.Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function
    
Hints:
    The built-in document method is __doc__
'''
if req == 24:
    print(abs.__doc__)
    print(int.__doc__)
    print(input.__doc__)  # raw_input has been removed from python 3
    
'''
25. Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
'''

'''

26.Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.
;
'''
if req==26:
    # using lambda function 
    summation = lambda x,y: x+y
    x = int(input("Enter first number: \n"))
    y = int(input("Enter second number; \n"))
    print(summation(x,y))
    
'''
27.Define a function that can convert a integer into a string and print it in console.

Hints:

Use str() to convert a number to string.
'''
if req==27 :
    def string():
        val = int(input("Enter an integer: \n"))
        ss = '{}'.format(val)
        print(ss)
        
    string()

'''
28.Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
'''
if req==28:
    def summation():
        x = int(input("Enter first number: \n"))
        y = int(input("Enter second number: \n"))
        print(x+y)

    summation()
    
'''
29.Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:

Use + to concatenate the strings
'''
if req==29 :
    def concatenate():
        x = input("Enter first string: \n")
        y = input("Enter second string: \n")
        print(x+y)
    
    concatenate()
    
'''
30.Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string

'''
if req==30:
    def max_string():
        x = input("Enter first string: \n")
        y = input("Enter second string: \n")
        x_len = len(x)
        y_len = len(y)
        if x_len > y_len :
            print(x)
        elif y_len > x_len :
            print(y)
        else :
            print(x)
            print(y)
        
    max_string()
    
'''
31.Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.
'''
if req==31:
    def EvenOddParity():
        x = int(input("Enter a number: \n"))
        if x%2 == 0:
            print("It is an even number")
        else :
            print("It is an odd number")
    
    EvenOddParity()
            
'''
32.Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
'''
if req==32:
    def dict_power():
        power = dict()
        for i in range(1,4):
            power[str(i)] = i**2
        
        print(power)
    
    dict_power()
    
'''
33.Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
'''
if req==33:
    def dict_power():
        power = dict()
        for i in range(1,21):
            power[str(i)] = i**2
        
        print(power)
    
    dict_power()
'''
34.Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
'''
if req==34:
    def dict_power():
        power = dict()
        for i in range(1,21):
            power[str(i)] = i**2
        
        for val in power.values():
            print(val, end= " ")
    
    dict_power()

'''
35.Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
'''
if req==35:
    def squared_list():
        squares = list()
        for val in range(1,21):
            squares.append(val**2)
        
        print(squares)
    
    squared_list()
    
'''
36.Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list
'''
if req==36:
    def squared_list():
        squares = list()
        for val in range(1,21):
            squares.append(val**2)
        
        print(squares[:5])
    
    squared_list()
    
'''

37.Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use tuple() to get a tuple from a list.
'''
if req==37:
    def tups():
        tup = tuple(x**2 for x in range(1,21))
        print(tup[:5])
        
    tups()

'''
38.With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 

Hints:

Use [n1:n2] notation to get a slice from a tuple.
'''
if req==38:
    tup = tuple(x for x in range(1,11))
    print(tup[:5])
    print(tup[5:])

'''
39.Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

Hints:

Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.
'''
if req==39:
    tup = tuple(x for x in range(1,11))
    out_tup = tuple()
    for val in tup:
        if val%2 == 0:
            out_tup = out_tup + (val, )
    
    print(out_tup)

'''
40.Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.
'''
if req==40:
    input_str = input("Enter yes or no string: \n")
    if input_str.upper() == 'YES' :
        print("Yes")
    elif input_str.upper() == 'NO' :
        print("No")
    else :
        print("Invalid string")
    
'''

41.Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
'''
if req==41:
    result = filter(lambda x: x%2 == 0, [1,2,3,4,5,6,7,8,9,10])
    print(list(result))  # filter return type must be checked ..
    
'''

42.Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
'''
if req==42:
    result = map(lambda x: x**2, [1,2,3,4,5,6,7,8,9,10])
    print(list(result))
    
'''

43.Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
'''
if req==43:
    result = map(lambda x: x**2, list(filter(lambda x: x%2 == 0, [1,2,3,4,5,6,7,8,9,10])))
    print(list(result))

'''
44.Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:

Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
'''
if req==44:
    result = list(filter(lambda x: x%2 == 0, list(i for i in range(1,21))))
    print(result)
    
'''
45.Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
'''
if req==45:
    result = list(map(lambda x: x**2, list(i for i in range(1,21))))
    print(result)

'''
54.Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.
'''
if req==54:
    p = re.compile('\w+')
    tot_usernames = int(input("ENter the total number of usernames: \n"))
    for username in range(tot_usernames):
        print(p.findall(input("Enter the username one-by-one: \n"))[0])
    
'''
55.Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.
'''
if req==55:
    p = re.compile('\w+')
    tot_usernames = int(input("Enter the total number of usernames: \n"))
    for username in range(tot_usernames):
        print(p.findall(input("Enter the username one-by-one: \n"))[1])
        
'''
56.Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example:
If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use re.findall() to find all substring using regex.
'''
if req==56:
    p = re.compile('\d+')
    tot_strings = int(input("Enter the total number of string: \n"))
    for string in range(tot_strings):
        print(p.findall(input("Enter the username one-by-one: \n")))
        
'''
57.Print a unicode string "hello world".

Hints:

Use u'strings' format to define unicode string.
'''
if req==57:
    unicode_str = u'Hello World' #denotes that the string is unicode removed in python 3.0 -3.2, added in python 3.3
    print(unicode_str)
    
'''
58.Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:

Use unicode() function to convert.
'''
if req==58:
    string = input("Input an ASCII string to be encoded : \n")
    string_utf = string.encode()
    print("Encoded version is: ", string_utf)
    
'''
59.Write a special comment to indicate a Python source code file is in unicode.
'''
if req==59:
    print("If a comment in the first or second line of the Python script matches the regular expression coding[=:]\s*([-\w.]+) then it indicats that the python code in in unicode")
 # If a comment in the first or second line of the Python script matches the regular expression coding[=:]\s*([-\w.]+) then it indicats that the python code in in unicode

'''
60.Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:
'''
if req==60:
    summ = 0.0
    nums = int(input("ENter an integer greater than 0: \n"))
    for num in range(1, nums+1):
        summ += (num/(num+1))
        
    print(summ)
    
'''
61.Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.
'''
if req==61:
    def recursive_add(num):
        if num == 0:
            return 1
        return recursive_add(num-1) + 100
        
    num = int(input("Enter an integer: \n"))
    print(recursive_add(num))
    
'''
62.The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.
'''
if req==62:
    def recursive_fib(num):
        if num==0 or num==1 :
            return num
        return recursive_fib(num-1) + recursive_fib(num-2)
        
    num = int(input("Enter an integer greater than 2: \n"))
    print(recursive_fib(num))

'''
63.The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13
'''
if req==63:
    fib = list()
    def iterative_fib(num):
        fib.extend([0,1])
        for i in range(num-1):
            fib.append(int(fib[-1])+int(fib[-2]))

    num = int(input("Enter an integer greater than 2: \n"))
    temp = iterative_fib(num)
    print(fib)

'''
64.Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.
'''
if req==64:
    def generator(num):
        itr = 0
        for itr in range(num+1):
            if itr%2 == 0:
                yield itr
    
    num = int(input("ENter an integer : \n"))
    for i in generator(num):
        print(i, end=',')
            
'''
65.Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70
'''
if req==65:
    def generator(num):
        itr = 0
        for itr in range(num+1):
            if itr%35 == 0:   # LCM of 5 and 7 is 35 XD
                yield itr
    
    num = int(input("ENter an integer : \n"))
    for i in generator(num):
        print(i, end=',')
    
'''
66.Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints:
Use "assert expression" to make assertion.
'''
if req==66:
    for num in [2,4,6,8]:
        assert num%2==0
        
'''
67. Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example:
If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38

Hints:
Use eval() to evaluate an expression.

'''
if req==67:
    expression = input("Enter a mathematical expression: \n")
    print(eval(expression))
    
'''
68.Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions.

'''
if req==68 or req==69:
    def binary_search(lists, target):
        l=0
        r=len(lists)-1
        while l<=r :
            mid = l + math.floor((r-l)/2 )
            if int(lists[mid]) == target :
                return mid
            elif int(lists[mid]) > target :
                r = mid-1
            else :
                l = mid+1
            
        return None
            
    input_str = input("ENter the input elements in csv format: \n")
    target = int(input("Enter the number ot be searched"))
    lists = input_str.split(',')
    index = binary_search(lists, target)
    print(index)
    
'''
70.Please generate a random float where the value is between 10 and 100 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].
'''
if req==70:
    num = random.uniform(10,100)
    print(num)
        
'''

71.Please generate a random float where the value is between 5 and 95 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].
'''
if req==71:
    num = random.uniform(5, 95)
    print(num)
    
'''
72.Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

Hints:
Use random.choice() to a random element from a list.
'''
if req==72:
    nums = list(x for x in range(11))
    nums = nums[::2]
    num = random.choice(nums)
    print(num)
    
'''
73.Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

Hints:
Use random.choice() to a random element from a list.
'''
if req==73:
    nums = list(x for x in range(100) if x%5==0 and x%7==0)
    num = random.choice(nums)
    print(num)
    
'''
74.Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.
'''
if req==74 or req==75:
    nums = random.sample(range(100,201), 5)
    print(nums)
    
'''76.Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

Hints:
Use random.sample() to generate a list of random values.
'''
if req==76:
    lists = list(x for x in range(1,1001) if x%35==0 )
    nums = random.sample(lists,5)
    print(nums)
    
'''77.Please write a program to randomly print a integer number between 7 and 15 inclusive.

Hints:
Use random.randrange() to a random integer in a given range.
'''
if req==77:
    num = random.randrange(7,16)
    print(num)

'''
78.Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
'''
if req==78:
    string = "hello world!hello world!hello world!hello world!"
    ss = bytes(string, 'utf-8')
    decomp_str = zlib.compress(ss)
    print(decomp_str)
    decomp_str = zlib.decompress(decomp_str)
    print(decomp_str)
    
'''79.Please write a program to print the running time of execution of "1+1" for 100 times.

Hints:
Use timeit() function to measure the running time.
'''
if req==79:
    first_time = datetime.datetime.now()
    for i in range(100):
        i = 1+1
    second_time = datetime.datetime.now()
    print((second_time - first_time))

'''

80.Please write a program to shuffle and print the list [3,6,7,8].

Hints:
Use shuffle() function to shuffle a list'''
if req==80 or req==81:
    nums = [3,6,7,8]
    random.shuffle(nums)
    print(nums)
    
'''
82.Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.
'''
if req==82:
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey","Football"]
    for sub in subjects:
        for verb in verbs:
            for obj in objects:
                print(sub + " " + verb + " " + obj)
    
'''
83.Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.
'''
if req==83:
    nums = [5,6,77,45,22,12,24]
    numbers = list(filter(lambda x: x%2!=0, nums))
    print(numbers)
    
'''
84.By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
'''
if req==84:
    nums = [12,24,35,70,88,120,155]
    numbers = list(filter(lambda x: x%35!=0, nums))
    print(numbers)
    
'''
85.By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.
'''
if req==85:
    nums = [12,24,35,70,88,120,155]
    nums = nums[::2]
    print(nums)
        
'''86.By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

Hints:
Use list comprehension to make an array.
'''
if req==86: 
    nums = [[[0 for z in range(8)] for y in range(5)] for x in range(3)]
    print(nums)
    
'''
87.By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.
'''
if req==87:
    nums = [12,24,35,70,88,120,155]
    indices = [0,4,5]
    num = [val for idx, val in enumerate(nums) if idx not in indices ]
    print(num)
    
'''
88.By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

Hints:
Use list's remove method to delete a value.
'''
if req==88:
    nums = [12,24,35,24,88,120,155]
    cnt = nums.count(24)
    for i in range(cnt):
        nums.remove(24)
    print(nums)
 
'''
89.With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

Hints:
Use set() and "&=" to do set intersection operation.
'''
if req==89:
    list1 = [1,3,6,78,35,55]
    list2 = [12,24,35,24,88,120,155]
    first = set(list1)
    second = set(list2)
    print(first & second)
    
'''

90.With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.
'''
if req==90:
    list1 = [12,24,35,24,88,120,155,88,120,155]
    nums = set(list1)
    print(nums)
    
'''
91.Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.
'''
if req==91:
    class Person():
        def __init__(self):
            pass
        
        def getGender(self):
            print("None")
            
    class Male(Person):
        def getGender(self):
            print("Male")
    
    class Female(Person):
        def getGender(self):
            print("Female")
            
    boy = Male()
    boy.getGender()
    girl = Female()
    girl.getGender()
    
'''
 Only question 25, 51-53 left //
'''
'''
46.Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.
'''
if req==46:
    # method1:
    
    class American():
        def __init__(self, country = 'America'):
            self.country = country
            
        def printNationality(self):
            print(self.country)
         
    person = American('USA')
    person.printNationality()
    
'''
47.Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.
'''
if req==47:
    class American():
        def __init__(self, country = 'America'):
            self.country = country
            print(self.country)
            

    class NewYorker(American):
        def __init__(self, country = 'NewYork'):
            self.country = country
            print(self.country)
            
    
    american_person = American()
    newyorker_person = NewYorker()
    
    print(american_person)

'''
48.Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.
'''
if req==48:
    class Circle():
        def __init__(self, radius = 0.0):
            self.radius = radius
            
        def Area(self):
            return 3.14*(self.radius**2)
            
    radii = float(input("ENter the radius of the circle: \n"))
    myCircle = Circle(radii)
    print(myCircle.Area())

'''
49.Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.
'''
if req==49:
    class Rectangle():
        def __init__(self, length = 0.0, breadth = 0.0):
            self.length = length
            self.breadth = breadth
            
        def Area(self):
            return self.length * self.breadth
            
    length = float(input("ENter the length of the Rectangle: \n"))
    breadth = float(input("ENter the breadth of the Rectangle: \n"))
    myRectangle = Rectangle(length, breadth)
    print(myRectangle.Area())
    
'''
50.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.
'''
if req==50:
    class Shape(object):
        def __init__(self):
            pass
            
        def Area(self):
            print(0)
            
    class Square(Shape):
        def __init__(self, length):
            Shape.__init__(self)
            self.length = length
            
        def Area(self):
            print(self.length * self.length)
    
    length = float(input("Enter the length of square: \n"))
    sq_object = Square(length)    
    sq_object.Area()
    
 '''
  4 questions left 25,51,52,53 (To be updated)
 '''
