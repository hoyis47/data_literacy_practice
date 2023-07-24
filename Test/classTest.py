'''
class Calculator:
    def _init_(self):
        self.result = 0

    def add (self, num):
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print (cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(4))
'''


class FourCal():

    def __init__(self, first,second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    

a = MoreFourCal(4,5)
#a.setdata(1,2)
print(a.add())
print(a.pow())
