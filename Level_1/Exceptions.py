"""This file contains some techniques for exception raise and handle"""

#Simple function 
def increment(x):
    """Increase the number by two """
    num=int(x)
    return num+2

test=increment(4)
print test
#test=increment("somedata")
print test


##Add exception 
def increment_exp(x):
    """Using exceptions """
    try:
        num=int(x)
    except ValueError:
        return "something wrong"
    return num
test=increment_exp(4)
print test
test=increment_exp("somedata")
print test


##Type Error 
def decrement(x):
    try:
        min=int(x)
    except ValueError:      ##int strings 
        return "not integer"
    except TypeError:       ##Lists or tuples so on 
        return "type is not correct "
    return min
test=decrement(10)
print test
test=decrement([1,2,3,4])
print test


#################################################
#Using SYS error exceptions  
#################################################
import sys
def detect(x):
    """Detecting errors from sys lib  """
    try:
        return int(x)
    except(ValueError,TypeError) as e:
        print "failed:{}".format(str(e))
    return -1
test=detect(4)
print test
test=detect("hhhhh")


##Division by Zero 
def divide(x,y):
    try:
        a=int(x)
        b=int(y)
        return a/b
    except ZeroDivisionError:
        return "Not allow ro divide by zero"
    return -1
test=divide(10,5)
print test
test=divide(10,0)
print test