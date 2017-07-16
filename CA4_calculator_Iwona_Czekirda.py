
#Write a Calculator program with 10 functions. 


#Chosen functions:
#factorial
#add
#substraction
#multiply
#divide
#exponent 
#square
#squareroot
#cube
#hypot

import string

#Functions

class Calculator(object):

#factorial

	
	def factorial_def(self,x):
		
		if x == 0:
			return 1
		if x < 0:
			return "inf"
		
		return x * self.factorial_def(x - 1)
		 
	def factorial(self,x): 
		
		return map(self.factorial_def, x)		
			
						
#add


	def add(self, x, y):
		
		return map(lambda a,b: a +b, x,y)
		
		
#substraction


	def substraction(self, x, y): 
		
		return map(lambda a,b: a-b, x,y)
			
		
#multiply


	def multiply(self, x, y):
		
				
			if x!=0 or y!=0:
				return map(lambda a,b: a*b, x,y)
			if x== 0:
			
				return "nan"
				

#divide 


	def divide(self,x,y): 	
				
		if x != 0 and y !=0:
			return map(lambda a,b: a/b, x,y)
		else:
			return "nan"
		

#exponentiation


	def exponent(self,x,y): 
		
		if x != 0 and y !=0:
			return map(lambda a,b: a**b, x,y)
		else: 
			return "nan"
		
#square


	def square(self,x): 
		
		if x != 0:
			return map(lambda a: a * a, x)
		else: 
			return "nan"
		
#squareroot


	def squareroot(self,x): 
		
		if x > 0:
			return map(lambda a:a ** 0.5, x)
		else: 
			return "nan"

#cube


	def cube(self,x):
		
		if x != 0:
			return map(lambda a: a ** 3.0, x)
		else: 
			return "nan"

#hypotenuse

	def hypot(self, x,y): 
		
		if x > 0 and y > 0:
			return map(lambda a,b: (a*a + b*b) ** 0.5, x,y)
		else: 
			return "nan"

#even numbers
		
	def is_even(self,x):
		
		return filter(lambda x: x%2==0, x)
		
			
#even numbers
		
	
	def max(self,x,y):
		
		return reduce(lambda a,b: a if (a>b) else b, x,y) 
 

		
#RESULTS
#MAIN VALIDATIONS 

def main():

#print the menu with choices
	
	print "\nC A L C U L A T O R\n\nChoose one of the following:\n\n1.factorial\n2.sum\n3.substraction\n4.multiplication\n5.division\n6.exponentiation\n7.square\n8.squareroot\n9.cube\n10.hypotenuse\n11.even numbers\n12.max"

#choice validation
#set the loop to 1 so it executes

	invalid = 1
	
	while invalid == 1: 
		invalid = 0 
		
		userinput = raw_input("\nPlease enter your choice: \n")
		
		z = ["1","2","3","4","5","6","7","8","9","10","11","12"]
		
		if userinput not in z:
			invalid = 1
			print "Please choose option 1-10"
			
			ex= raw_input("Do you want to exit? ")
			if ex == "yes" or ex == "Yes":
				print "Bye!" 
				raise SystemExit
					
			
#factorial validation 
			
		calc = Calculator()
		
		if userinput == "1":

			valid=0
			while valid==0:
				try:
					x = input("Please enter the numbers: \n")
				except:
					print "Numbers only"
					continue
				valid=1
			
			print "The result is",(calc.factorial(x))
			print "Thank you for using CALCULATOR"

#add validation

		if userinput == "2":
			
			valid=0
			while valid==0:
				try:
					x = input("Please enter the number: \n")
					y = input("Please enter the second number: \n")
				except:
					print "Numbers only"
					continue
				valid=1
											
			print "The result is ",(calc.add(x,y))
			print "Thank you for using CALCULATOR"

#substraction validation
		
		if userinput == "3":
		
			valid=0
			while valid==0:
				try:
					x = input("Please enter the number: \n")
					y = input("Please enter the second number: \n")
				except:
					print "Numbers only"
					continue
				valid=1
			
			print "The result is ",(calc.substraction(x,y))
			print "Thank you for using CALCULATOR"

#multiply validation

		if userinput == "4":
			
			valid=0
			while valid==0:
				try:
					x = input("Please enter the number: \n")
					y = input("Please enter the second number: \n")
				except:
					print "Numbers only"
					continue
				valid=1
							
			print "The result is ",(calc.multiply(x,y))
			print "Thank you for using CALCULATOR"

#divide validation
		
		if userinput == "5":
			
			valid=0
			while valid==0:
				try:
					x = input("Please enter the first number: \n")
					y = input("Please enter the second number: \n")
				except:
					print "Numbers only"
					continue
				valid=1
				
			print "The result is ",(calc.divide(x,y))
			print "Thank you for using CALCULATOR"

#exponent validation

		if userinput == "6":

			valid=0
			while valid==0:
				try:
					x = input("Please enter the first number: \n")
					y = input("Please enter the second number: \n")
				except:
					print "Numbers only"
					continue
				valid=1
			
			print "The result is ",(calc.exponent(x,y))
			print "Thank you for using CALCULATOR"

#square validation
		
		if userinput == "7":

			valid=0
			while valid==0:
				try:
					x = input("Please enter the numbers: \n")
				except:
					print "Numbers only"
					continue
				valid=1
			
			print "The result is ",(calc.square(x))
			print "Thank you for using CALCULATOR"
			
#square root validation
			
		if userinput == "8":

			valid=0
			while valid==0:
				try:
					x = input("Please enter the numbers: \n")
				except:
					print "Numbers only"
					continue
				valid=1
			
			print "The result is ",(calc.squareroot(x))
			print "Thank you for using CALCULATOR"

#cube validation 

		if userinput == "9":

			valid=0
			while valid==0:
				try:
					x = input("Please enter the numbers: \n")
				except:
					print "Numbers only"
					continue
				valid=1
			
			print "The result is ",(calc.cube(x))
			print "Thank you for using CALCULATOR"

#hypot validation

		if userinput == "10":

			valid=0
			while valid==0:
				try:
					x = input("Please enter the first length: \n")
					y = input("Please enter the second length: \n")
				except:
					print "Numbers only"
					continue
				valid=1
			
			print "The result is ",(calc.hypot(x,y))

#even numbers validation

		if userinput == "11":

			valid=0
			while valid==0:
				try:
					x = input("Please enter the numbers: \n")
				except:
					print "Numbers only"
					continue
				valid=1
			
			print "The result is ",(calc.is_even(x))

		if userinput == "12":

					valid=0
					while valid==0:
						try:
							x = input("Please enter the first number: \n")
							y = input("Pleae enter the second number:\n")
						except:
							print "Numbers only"
							continue
						valid=1
					
					print "The result is ",(calc.max(x,y))
		
main()


