def leap(a):
    if a > 0:
        if a % 400 == 0:
            return "Leap"
        elif a % 100 == 0:
            return "Leap"
        elif a % 4 == 0:
            return "Leap"
    return "Not Leap"


assert leap(2000) == "Leap"
assert leap(2004) == "Leap"
assert leap(2012) == "Leap"
assert leap(2019) == "Not Leap"
assert leap(1933) == "Not Leap"
