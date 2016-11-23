"""
Program Assignment: Prog 5
Name: David Ernesto Saenz Saenz
Date: 10/10/2016

Listing Contents:
	Reuse instructions:
			Class Main:
				Purpose: Main Class for the program 5
				Limitations: NOT REUSABLE, just Base code. 
				Def Program_5(self):
					Purpose: Set up the mode for program 5 specifications
					Limitations: The File to read MUST contain 3 numbers: X, dof, and the Num Seg.
			
			Class Integration_And_tDistribution:
				Purpose: Holds the methods for the Integration by Simpson Method and t Distribution operations
				Limitations: REUSABLE. Works with Float format numbers and only format numbers. (!) Everything returns a float number.
				Def Simpson(self, xi, num_seg, dof):
					Purpose: Calculates the integration by Simpson rule (Concepts about Simpson Rule) Clculates W each time, so if it needs more than one iteration.
				Def t_Distribution(self, xi, dof):
					Purpose: Calculates F(x) for the t Distribution needed for the Simpson method by Parts: 1, 2 and 3: 2nd * 3rd part. See Below.
				Def t_First_Part(self, xi, dof):
					Purpose: Calculates first part for the operation of t Distribution: 1 + (xi^2 / dof)
				Def t_Second_Part(self, FP, dof):
					Purpose: Calculates second part for the operation of t Distribution: First Part -> pow(-(dof+1)/2)
				Def t_Third_Part(self, dof):
					Purpose: Calculates third part for the operation of t Distribution: Gamma((dof+1)/2) / ((dof * pi)pow(1/2) * Gamma(dof/2))

	Imports: math. Note: Gamma is native of Python 2.7

	Class declarations:
		Main:
		Integration_And_tDistribution:
		
	Source code in .../<current_dir>/
		From Prog_1 => Class Reader => Def read
		From Prog_3 => Class Regression_Correlation => Def Total_Sum
"""

import math
from PROG_1 import Reader
from PROG_3 import Regression_Correlation

class Integration_And_tDistribution():
	
	#  Read the table of contents to understand the function of each part of this Class
	def Simpson(self, xi, num_seg, dof, leng):
		#  Object needed to calculate the total Sum of the P results
		Sum_Op = Regression_Correlation()
		Terms = []
		Multiplier = 0.0
		Xi_Op = xi / leng 
		#  print "\nNum Seg: ", num_seg
		W = xi / num_seg
		#  print "W: ", W

		#  This loop will help us to perform each calculation of the Simpson method and also to determine the Multipler used on each part
		for num in xrange(0, (int(num_seg) + 1)):
			if(num == 0 or num == int(num_seg)):
				Multiplier = 1.0
			elif (num % 2 == 0 and num > 0 and int(num_seg)):
				Multiplier = 2.0
			elif (num % 2 != 0 and num > 0 and int(num_seg)):
				Multiplier = 4.0

			#  We calculate each F(x) for the Simpson Method
			Fx = self.t_Distribution((Xi_Op - (xi/leng)), dof)
			# Then we calculate each P result from the Simpson Method
			p = (W/3) * Multiplier * Fx
			Terms.append(p)
			Xi_Op += W

		#  print "\nTerms: ", Terms
		Result = Sum_Op.Total_Sum(Terms)
		return Result

	#  See the Table of Contents for an explanation of this section
	def t_Distribution(self, xi, dof):
		First_Part = self.t_First_Part(xi, dof)
		Second_Part = self.t_Second_Part(First_Part, dof)
		Third_Part = self.t_Third_Part(dof)

		Function = Second_Part * Third_Part
		return Function

	def t_First_Part(self, xi, dof):
		part_1 = 1.0 + ((xi ** 2.0) / dof)
		return part_1

	def t_Second_Part(self, FP, dof):
		power = ((dof + 1.0) / 2.0)
		part_2 = math.pow(FP, -power)
		return part_2

	def t_Third_Part(self, dof):
		up = math.gamma((dof + 1.0) / 2.0)
		down = (math.pow((dof * math.pi), 0.5)) * (math.gamma(dof / 2.0))
		part_3 = up / down
		return part_3


class Main():
	#  Read the table of contents to understand the function of each part of this Class
	def Program_5(self):
		print "Welcome to Program 5..."
		print "Starting..."

		#  We read the data from the file
		read = Reader()
		self.allData = read.read()

		#  Set the data to the needed variables
		x = float(self.allData[0])
		dof = float(self.allData[1])
		num_seg = float(self.allData[2])
		length_seg = num_seg

		print "\nX: ", x
		print "Dof: ", dof

		#  The Error margin for comparison
		E = 0.00001

		#  Object with which we will use to calculate the integration
		integration = Integration_And_tDistribution()

		#  An infinite loop, set to calculate the integration until it reaches the condition we are looking for
		while(True):
			self.Simpson_1 = integration.Simpson(x, num_seg, dof, length_seg)
			print "\nSimpson 1: SUM of P: ", self.Simpson_1
			self.Simpson_2 = integration.Simpson(x, num_seg+10, dof, length_seg)
			print "\nSimpson 2: SUM of P: ", self.Simpson_2

			#  Are we over the Error Margin or below?
			if((self.Simpson_1 - self.Simpson_2) > E):
				num_seg = num_seg + 10
				print "\nIntegration 1 - Integration 2 = ", (self.Simpson_1 - self.Simpson_2), ". \nIs not less than E. Iterate again."
			elif((self.Simpson_1 - self.Simpson_2) < E):
				print "\nIntegration 1 - Integration 2 = ", (self.Simpson_1 - self.Simpson_2), ". \nIs less than E. Success!"
				break

		#  If we are below, we print the final result
		print "\nResult P: ", round(self.Simpson_2, 5), "\n"

#  Execute Main Program
if __name__ == "__main__":
	main = Main()
	main.Program_5()