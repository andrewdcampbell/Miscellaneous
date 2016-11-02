#Approximate the value of pi using midpoint Riemann sum of f(x)=4/(1+x^2) from x=0 to x=1
#For some reason, the most accurate result is at 1 million
import math 
def function(x):
	return 4/(1+x**2)

number_of_rectangles = int(input("Number of rectangles: "))
increment = 1/number_of_rectangles

def sum_of_functions():
	answer = 0
	for n in range(1,number_of_rectangles+1):
		answer = answer + function((increment*n)-(0.5*increment))
	return answer

result = sum_of_functions()*increment

print ("Using", number_of_rectangles, "rectangles with increments of", increment)
print ("Result:",result)
print ("Actual:", math.pi)


