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


##More initializers 
class C4:
    def __init__(self,name,age,city):
        self._name=name
        self._age=age
        self._city=city

    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_city(self):
        return self._city

test=C4("Bob",33, "ALEPPO")
print "details:{}\t{}\t{} ".format(test.get_age(),test.get_name(),test.get_city())



#################################################
##Using class as new type 
#################################################
class School:
    def __init__(self,name,numberOfStudents,teachers):
        self._name=name
        self._numberOfStudents=numberOfStudents
        self._teachers=teachers

    def show(self):
        print "School: {}  \t students: {} \t teacher salary: {}".format(self._name ,
        self._numberOfStudents,
        self._teachers.salary())


class Teachers:
    def __init__(self,tName,tCity):
        self._name=tName
        self._tCity=tCity

    def salary(self):
        return 200


t=Teachers("Mano","Dams")
s=School("Uppsala",500,t)
s.show()