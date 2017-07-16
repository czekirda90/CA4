import unittest

from CA4_calculator_Iwona_Czekirda import *

# test the calculator functionality


class TestCalculator(unittest.TestCase):


	def setUp(self):
	
		self.c1 = Calculator()

#create function testing factorial 

	def testfactorial(self): 
		self.assertEqual([120,1,2,24,"inf"], self.c1.factorial([5,1,2,4,-3]))
		

#create function testing add

	def testadd(self):
		self.assertEqual([6,-3,0,10,4], self.c1.add ([2,1,-2,5,6],[4,-4,2,5,-2]))
		

#create function testing substraction

	def testsubstraction(self):
		self.assertEqual([120,55,0,0,60], self.c1.substraction([140,88,2,-50,-20],[20,33,2,-50,-80]))
		
		
#create function testing multiply
	
	def testmultiply(self): 
		self.assertEqual([0,20,0,45,-35], self.c1.multiply([2,10,0,9,-7],[0,2,3,5,5]))
		

#create function testing divide
		
	def testdivide(self):
	
		self.assertEqual([-4,5, 3, -5, 9], self.c1.divide([-2,15,9,-1230,-81],[0.5,3,3,246,-9]))

		
#create function testing esponent

	def testexponent(self):
	
		self.assertEqual([1,625,0.01, 0, 0.125], self.c1.exponent([3,5,-10,0,2], [0,4,-2,246,-3]))

		
#create function testing square
		
	def testsquare(self): 
		
		self.assertEqual([0,1,225,484,0.000009], self.c1.square([0,1,-15,22,0.003]))

		
#create function testing square root
	
	def testsquareroot(self): 
	
		self.assertEqual([0,2,9,33.2,0.8], self.c1.squareroot([0,4,81,1102.24,0.64]))
	
	
#create function testing cube
		
	def testcube(self): 
	
		self.assertEqual([64,-27,1000,0.125,1771.561], self.c1.cube([4,-3,10,0.5,12.1]))
		
		
#create function testing hypot 
		
	def testhypot(self):
	
		self.assertEqual([5, 17, 17.8], self.c1.hypot([4,15,16],[3,8,7.8]))
		
		
#create function testing is_even

	def testis_even(self):
		
		self.assertEqual([4,6,70,88], self.c1.is_even([4,6,-49,70,15,88]))

		
#create function testing max

	def testmax(self):
		self.assertEqual([123,100,-12,245,199], self.c1.max([34,22,153,-120,100], [123,100,-12,245,199]))
		
		
	
if __name__ == '__main__':
	unittest.main()