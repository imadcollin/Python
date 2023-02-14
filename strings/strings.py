def hello_name(name):
    return "Hello " + name +"!"

assert hello_name('Bob') == 'Hello Bob!'
assert hello_name('Alice') == 'Hello Alice!'
assert hello_name('X') == 'Hello X!'


def make_abba(a, b):
    return a + b +b +a ; 


assert make_abba('Hi', 'Bye') == 'HiByeByeHi'
assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo'
assert make_abba('What', 'Up') == 'WhatUpUpWhat'


def make_tags(tag, word):
    return "<"+ tag+">" + word + "</"+tag +">" 


assert make_tags('i', 'Yay') == '<i>Yay</i>'
assert make_tags('i', 'Hello') == '<i>Hello</i>'
assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'


def make_out_word(out, word):
    return out[0]+out[1] + word + out[2]+out[3]

assert make_out_word('<<>>', 'Yay') =='<<Yay>>'
assert make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>'
assert make_out_word('[[]]', 'word') =='[[word]]'


def extra_end(str):
    x= ""
    for i in range(3):
        if(len(str)==2): 
            x= x+str[0] +str[1]
        else: 
            x=x+ str[len(str)-2] + str[len(str)-1]
    return x

assert extra_end('Hello') == 'lololo'
assert extra_end('ab') == 'ababab'
assert extra_end('Hi') =='HiHiHi'


def extra_end_2(str):
    end = str[-2:]
    return end + end + end


assert extra_end_2('Hello') == 'lololo'
assert extra_end_2('ab') == 'ababab'
assert extra_end_2('Hi') =='HiHiHi'


def first_two(str):
    if(len(str) >= 2):
        return str[:2]
    else: 
        return str

assert first_two('Hello') == 'He'
assert first_two('abcdefg') =='ab'
assert first_two('ab') =='ab'

def first_half(str):
    if(len(str)>1):
        mid= len(str)/2
        return str[:int(mid)]
    else:
        return str


assert first_half('WooHoo') == 'Woo'
assert first_half('HelloThere') == 'Hello'
assert first_half('abcdef') =='abc'


def without_end(str):
    return str[1:len(str)-1]

assert without_end('Hello') == 'ell'
assert without_end('java') == 'av'
assert without_end('coding') == 'odin'
