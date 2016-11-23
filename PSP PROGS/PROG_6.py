"""
Program Assignment: Prog 6
Name: David Ernesto Saenz Saenz
Date: 17/10/2016

Listing Contents:
	Reuse instructions:
			Class Main:
				Purpose: Main Class for the program 6
				Limitations: NOT REUSABLE, just Base code. 
				Def Program_6(self):
					Purpose: Set up the data for program 5 specifications.
							 Note: Some data is specified in the Operations Classm such as E, d
							 	   Be careful to consider this if you are going to reuse this
							 	   parts of code.
					Limitations: The File to read MUST contain 3 numbers: 
								 Expected P, Dof, and the Num Seg.
								 These three data must be specified in Float formats.
	Reuse instructions:	
			Class Operations:
				Purpose: Holds the methods for the Integration by Simpson Method and t Distribution operations
				Limitations: REUSABLE. Works with Float format numbers and only format numbers. 
							 Note: Everything returns a float number.
				Def Calculation_X(self, expected_P, inital_X, dof, num_seg, leng):
					Purpose: Calculates the original value of X performing an integration with an 
							 initial value if X, comparing the result with a previously given result 
							 of P. If the obtaiend P is equals to the Expected P, then the X used to 
							 calculate the integration is the Result X. If not, X is reiterated.
					Limitations: Consider properly the value initial_X (X): 
								 The shorter the value, the MORE iterations and operations it takes to 
								 calculate the result.
								 Note: Be careful to consider the decimal numbers for the evaluation, 
								 since it uses a float format of number. It can take some time to evualuate 
								 each condition and throw big 'big' results.

	Class declarations:
		Main():
		Operations():
		
	Source code in .../<current_dir>/
		From Prog_1 
			Class Reader
				Def read
		From Prog_5
			Class Integration_And_tDistribution
				Def Simpson
"""

"""
Consider the printing of the Termns array
from the Simpson method of Integration_And_tDistribution.
The more calculations and iterations it takes, deppending
on the X value, the Dof and the acceptance error, 
the more memory and times it takes to finish the execution
of the program.
"""
from PROG_5 import Integration_And_tDistribution
from PROG_1 import Reader

class Operations():

	#  Read the table of contents to understand the function of each part of this Class
	def Calculation_X(self, expected_P, inital_X, dof, num_seg, leng):
		integration = Integration_And_tDistribution()
		#  We set an initial value for d and E, and initialize the Result variable
		E = 0.00001
		d = 0.5
		Result = 0.0

		while(True):
			#  We perform the first integration
			self.Simpson_1 = integration.Simpson(inital_X, num_seg, dof, leng)
			#  print "\nX: ", inital_X
			#  print "Simpson 1: ", self.Simpson_1

			#  Is this the desired Result?
			if (self.Simpson_1 == expected_P):
				Result = inital_X
				break
			elif (self.Simpson_1 < expected_P):
				inital_X += d
			elif (self.Simpson_1 > expected_P):
				inital_X -= d

			#  We perform the second integration
			self.Simpson_2 = integration.Simpson(inital_X, num_seg+10.0, dof, leng)
			#  print "\nX: ", inital_X
			#  print "Simpson 2: ", self.Simpson_2

			#  print "\nSimpson 1 - Simpson 2 = ", (self.Simpson_1 - self.Simpson_2)
			if ((self.Simpson_1 - self.Simpson_2) == E):
				Result = inital_X
				break
			#  If the sign of the difference is different than the one of the Error, we recalculate d
			elif((self.Simpson_1 - self.Simpson_2) < 0):
				d = d / 2.0

			num_seg = num_seg + 10

		return Result


class Main():

	#  Read the table of contents to understand the function of each part of this Class
	def Program_6(self):
		print "Welcome to Program 6..."
		print "Starting..."

		#We read the data from the file
		reader = Reader()
		self.allData = reader.read()

		try:
			#  We set and parse the data to the respective variables
			P = float(self.allData[0])
			Dof = float(self.allData[1])
			num_seg = float(self.allData[2])
			Leng = num_seg

			print "\nP: ", P
			print "Dof: ", Dof
			print "Num Seg: ", num_seg

			#  We set an initial value of X: We choose 4 to reduce the number of operations performed by the program
			X = 4.0

			#  We perform the Calculation of X with the given data
			Ops = Operations()
			self.Result = Ops.Calculation_X(P, X, Dof, num_seg, Leng)

			print "\nResult X: ", round(self.Result, 5) , "\n"
		
		except ValueError as e:
			print "\nError: ", e, "\nData is incorrect: Check and correct the .txt file.\n"

#  Execute Main Program
if __name__ == "__main__":
	main = Main()
	main.Program_6()