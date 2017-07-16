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

#1.factorial

factorial_a<- function(a) {
   factorial(a)
}

factorial_a(5)

#2.addition
addition <- function(a,b) { 
    sum(a,b)
}

#3.substraction 
substraction <- function(a,b){
    a - b
}

#4.multiply
multiply <- function(a,b){
    a * b
}

#5.divide 
divide <- function(a,b){
    a / b
}

#6.exponent
exponent <- function(a,b){
    a ** b
}

#7.square
square <- function(a){
    a * a
}

#8.square root 
square_root <- function(a){
    sqrt(a)
}

#9.cube
cube <- function(a){
    a ** 3.0
}

#10.hypotenuse
hypot <-function(a,b){
    (a*a + b*b) ** 0.5
}


#TestCases

factorial_a(5)
factorial_a(1)
addition(3,6)
addition(-2,2)
substraction(5,7)
substraction(-100,-200)
multiply(3,4)
multiply(15,-4)
divide(7,8)
divide(10,5)
exponent(-25,5)
exponent(27,3)
square(4)
square(-9)
square_root(125)
square_root(1080)
cube(6)
cube(5)
hypot(5,6)
hypot(13,5)

