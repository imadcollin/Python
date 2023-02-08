def string_times(str, n):
    x= ""
    for i in range(n): 
        x= x+str;
    return x

assert string_times('Hi', 2) == 'HiHi'
assert string_times('Hi', 3) == 'HiHiHi'
assert string_times('Hi', 1) == 'Hi'


def front_times(str, n):      
    x= str[:3]
    temp =""
    for i in range(n): 
        temp+= x; 
    return temp


assert front_times('Chocolate', 2) == 'ChoCho'
assert front_times('Chocolate', 3) == 'ChoChoCho'
assert front_times('Abc', 3) == 'AbcAbcAbc'

def string_bits(str):
    s= ""
    for i in range(len(str)):
        if(i%2==0): 
            s+=str[i];
    return s; 

assert string_bits('Hello') == 'Hlo'
assert string_bits('Hi') =='H'
assert string_bits('Heeololeo') == 'Hello'


def string_splosion(str):
    if(len(str) == 1): 
        return str
    if (len(str) ==2): 
        return str[:1] + str
    s= ""
    for i in range (len(str)): 
        s=s+ str[:i+1]; 
    return s; 


def string_splosion_2(str):
    s = ""
    for i in range (len(str)): 
        s=s+ str[:i+1]; 
    return s; 


assert string_splosion_2('Code') == 'CCoCodCode'
assert string_splosion_2('abc') == 'aababc'
assert string_splosion_2('ab') =='aab'
