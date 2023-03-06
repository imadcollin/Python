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

def palind(n): 
    rev, temp = 0,n
    while temp !=0: 
        rev= rev*10 + temp%10
        temp= temp//10 
    return rev==n

assert palind(22322) ==True
assert palind(55544555) ==True
assert palind(22) ==True
assert palind(21) ==False
assert palind(65) ==False
