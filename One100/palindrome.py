def palindrome(n): 
    flag = False
    if (n<9): return True
    list = []
    while (n > 0):
        x= n%10
        list.append(x)
        n= n //10 
    l = len(list)
    for i in range (l): 
        last =(len(list)-1) -i 
        if(list[i]== list[last]):
            flag = True
        else:
            flag =False
    return flag    


assert palindrome(22322) ==True
assert palindrome(55544555) ==True
assert palindrome(22) ==True
assert palindrome(21) ==False
assert palindrome(65) ==False
    