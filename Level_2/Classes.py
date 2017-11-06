"""This file contains basic usage of class in Python"""
class C:
    pass
test=C()
print type(test)


#Method
class C1:
        def fn(self): ##Needed!!!! self is an arg 
            return "hello"
test=C1()
print type(test)
print test.fn()


#Initializer 
class C2:
    def __init__(self,num):
        self._num=num

    def get_num(self): ##Needed!!!! self is an arg 
        return self._num
test=C2(100)
print test.get_num()



#Example
class C3:
    def __init__(self,str):
        if not str[:2].isalpha():
            raise ValueError("is alpha")

        self._str=str

    def get_str(self):
        return self._str
    
test=C3("string")
print test.get_str()