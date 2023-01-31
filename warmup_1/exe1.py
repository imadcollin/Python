### Sleep in example 
def sleep_in(weekday, vacation):
    if ( weekday & (not vacation)): 
      return False; 
    else: 
      return True;

def sleep_in_2(weekday, vacation): 
    return (not weekday or vacation); 


assert sleep_in(True, True)==True;
assert sleep_in(False, False)==True;
assert sleep_in(False, False) == True
assert sleep_in(True, False) ==False
assert sleep_in(False, True)== True

assert sleep_in_2(True, True)==True;
assert sleep_in_2(False, False)==True
assert sleep_in_2(False, False) == True
assert sleep_in_2(True, False) ==False
assert sleep_in_2(False, True)== True