import math #lets you use math module 
import unittest #unit test module helps us test small sections of code

def circleArea(radius): 
    return radius * radius * math.pi

def rectArea(base, height):
    return base * height

def trapArea(base1, base2, height):
    return height * (base1 + base2) / 2

def triArea(base,height):
    return 
    
	
class MyTest(unittest.TestCase): #using Testcase class from unittest module
    def testCircleArea(self):
        self.assertEqual(circleArea(5),25*math.pi)
        self.assertEqual(circleArea(2),4*math.pi)
    def testRectArea(self):
        self.assertEqual(rectArea(3,3),6*6)
        self.assertEqual(rectArea(6,6), 12*12)
    def testTrapArea(self):
        self.assertEqual(trapArea(5,6,7), 3 *(4+4)/2)
        self.assertEqual(trapArea(4,5,6), 4 *(5+5)/2)
    def testTriArea(self):
        self.assertEqual(triArea(4,5), 3*3)
        self.assertEqual(triArea(5,5), 4*4)
    