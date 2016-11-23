"""
Program Assignment: Prog 8
Name: David Ernesto Saenz Saenz
Date: 11/15/2016

Listing Contents:
	Reuse instructions:
			Class Main:
				Purpose: Main Class for the program 8
				Limitations: NOT REUSABLE, just Base code. 
				Def Program_8(self):
					Purpose: Set up the data for program 8 specs.
							 Note: Some data is spec in the Range Class such as E, 
							 	   dof and num_seg. Be careful to consider this when you 
							 	   are going to reuse this parts of code.
					Limitations: The File to read MUST contain 24 numbers: 
								 First 6 are W data; then X, Y and Z.
								 Only prints the results.
	Reuse instructions:	
			Class Multiple_Regression_And_Equations():
				Purpose: Holds the methods for Gauss Regression Method and 
						 the Equations setup.
				Limitations: REUSABLE. Works with Float format numbers and 
							 only format numbers. 
							 Note: Everything returns a float number.
				Def Equation_1, Def Equation_2, Def Equation_3, Def Equation_4(self, Wi, Xi, Yi, Zi):
					Purpose: Sets up each of the 4 equations needed for the 
							 program's Gauss regression method.
					Limitations: Wi, Xi, Yi and Zi must be an array of float numbers.
								 Each returns an array of float numbers.
				Def Guass_Method(self, Equation_1, Equation_2, Equation_3, Equation_4):
					Purpose: Calculates the Beta 0, Beta 1, Beta 2, Beta 3 
							 params using the Gauss Elimination method. (W, X, Y, Z)
					Limitations: Equation_1, Equation_2, Equation_3, Equation_4 
								 must be arrays of float numbers.
								 Returns 4 float numbers in this order: 
								 Beta 0, Beta 1, Beta 2 and Beta 3.
				Def Standard_Deviation(self, Zi, Wi, Xi, Yi, B0, B1, B2, B3):
					Purpose: Calculates the Standard Deviation using the new formula 
							 with the new params.
					Limitations: Zi, Wi, Xi, Yi must be arrays of float numbers.
								 Returns a float number.
				Def Range(self, Wi, Xi, Yi, Zi, B0, B1, B2, B3, Wk, W_Avg, Xk, X_Avg, Yk, Y_Avg):
					Purpose: Calculates the Prediction Interval with the new Formula, 
							 using the new params.
					Limitation: Wi, Xi, Yi, Zi must be arrays of float numbers. 
								B0, B1, B2, B3, Wk, W_Avg, Xk, X_Avg, Yk and Y_Avg 
								must be float numbers.
								Returns a Float number.

	Class declarations:
		Multiple_Regression_And_Equations():
		Main():
		
	Source code in .../<current_dir>/
		From Prog_1 
			Class Reader
				Def read
			Class Statistics_Ops
				Def mean
		From Prog_3
			Class Regression_Correlation
				Def Total_Sum
		From Prog_6
			Class Operations
				Def Calculation_X
"""

"""
- math's sqrt to calculate the 
	Square Roots needed
- Prog_1's Reader, Statistics_Ops
	to read and manage the data, and 
	calculate the Average.
- Prog_3's Regression_Correlation 
	to get the Regression used to
	calculate the total Sum of elements.
- And Prog_6's Operations 
	to calculate the value of X, with a given
	P value.
"""

import math
from PROG_1 import Reader, Statistics_Ops
from PROG_3 import Regression_Correlation
from PROG_6 import Operations

class Multiple_Regression_And_Equations():
	#  For a better understandig, check the table of contents.
	def Equation_1(self, Wi, Xi, Yi, Zi):
		#  Equation 1: nB0 + B1SumWi + B2SumXi + B3SumYi = SumZi
		n = float(len(Wi))
		Sum_Wi = 0.0
		Sum_Xi = 0.0
		Sum_Yi = 0.0
		Sum_Zi = 0.0
		Eq_1 = []

		for num in xrange(0, len(Wi)):
			Sum_Wi += Wi[num]
			Sum_Xi += Xi[num]
			Sum_Yi += Yi[num]
			Sum_Zi += Zi[num]

		Eq_1.append(n)
		Eq_1.append(Sum_Wi)
		Eq_1.append(Sum_Xi)
		Eq_1.append(Sum_Yi)
		Eq_1.append(Sum_Zi)

		return Eq_1

	def Equation_2(self, Wi, Xi, Yi, Zi):
		#  Equation 1: B0SumWi + B1SumWi2 + B2SumWiXi + B3SumWiYi = SumWiZi
		Sum_Wi = 0.0
		Sum_Wi2 = 0.0
		Sum_WiXi = 0.0
		Sum_WiYi = 0.0
		Sum_WiZi = 0.0
		Eq_2 = []

		for num in xrange(0, len(Wi)):
			Sum_Wi += Wi[num]
			Sum_Wi2 += (Wi[num] ** 2.0)
			Sum_WiXi += (Wi[num] * Xi[num])
			Sum_WiYi += (Wi[num] * Yi[num])
			Sum_WiZi += (Wi[num] * Zi[num])

		Eq_2.append(Sum_Wi)
		Eq_2.append(Sum_Wi2)
		Eq_2.append(Sum_WiXi)
		Eq_2.append(Sum_WiYi)
		Eq_2.append(Sum_WiZi)

		return Eq_2

	def Equation_3(self, Wi, Xi, Yi, Zi):
		#  Equation 1: B0SumXi + B1SumWiXi + B2SumXi2 + B3SumXiYi = SumXiZi
		Sum_Xi = 0.0
		Sum_WiXi = 0.0
		Sum_Xi2 = 0.0
		Sum_XiYi = 0.0
		Sum_XiZi = 0.0
		Eq_3 = []

		for num in xrange(0, len(Wi)):
			Sum_Xi += Xi[num]
			Sum_WiXi += (Wi[num] * Xi[num])
			Sum_Xi2 += (Xi[num] ** 2.0)
			Sum_XiYi += (Xi[num] * Yi[num])
			Sum_XiZi += (Xi[num] * Zi[num])

		Eq_3.append(Sum_Xi)
		Eq_3.append(Sum_WiXi)
		Eq_3.append(Sum_Xi2)
		Eq_3.append(Sum_XiYi)
		Eq_3.append(Sum_XiZi)

		return Eq_3

	def Equation_4(self, Wi, Xi, Yi, Zi):
		#  Equation 1: B0SumYi + B1SumWiYi + B2SumXiYi + B3SumYi2 = SumYiZi
		Sum_Yi = 0.0
		Sum_WiYi = 0.0
		Sum_XiYi = 0.0
		Sum_Yi2 = 0.0
		Sum_YiZi = 0.0
		Eq_4 = []

		for num in xrange(0, len(Wi)):
			Sum_Yi += Yi[num]
			Sum_WiYi += (Wi[num] * Yi[num])
			Sum_XiYi += (Xi[num] * Yi[num])
			Sum_Yi2 += (Yi[num] ** 2.0)
			Sum_YiZi += (Yi[num] * Zi[num])

		Eq_4.append(Sum_Yi)
		Eq_4.append(Sum_WiYi)
		Eq_4.append(Sum_XiYi)
		Eq_4.append(Sum_Yi2)
		Eq_4.append(Sum_YiZi)

		return Eq_4

	def Guass_Method(self, Equation_1, Equation_2, Equation_3, Equation_4):
		Help_Eq_1 = Equation_1
		Help_Eq_2 = Equation_2
		Help_Eq_3 = Equation_3
		Help_Eq_4 = Equation_4

		for num in xrange(0, 4):
			if num == 0:
				pivot1 = Help_Eq_1[0]
				pivot2 = Help_Eq_2[0]
				pivot3 = Help_Eq_3[0]
				pivot4 = Help_Eq_4[0]

				for num_2 in xrange(0, 5):
					Help_Eq_1[num_2] = Help_Eq_1[num_2] / pivot1
					Help_Eq_2[num_2] = Help_Eq_2[num_2] - (pivot2 * Help_Eq_1[num_2])
					Help_Eq_3[num_2] = Help_Eq_3[num_2] - (pivot3 * Help_Eq_1[num_2])
					Help_Eq_4[num_2] = Help_Eq_4[num_2] - (pivot4 * Help_Eq_1[num_2])

			if num == 1:
				pivot2 = Help_Eq_2[1]
				pivot3 = Help_Eq_3[1]
				pivot4 = Help_Eq_4[1]

				for num_2 in xrange(0, 5):
					Help_Eq_2[num_2] = Help_Eq_2[num_2] / pivot2
					Help_Eq_3[num_2] = Help_Eq_3[num_2] - (pivot3 * Help_Eq_2[num_2])
					Help_Eq_4[num_2] = Help_Eq_4[num_2] - (pivot4 * Help_Eq_2[num_2])

			if num == 2:
				pivot3 = Help_Eq_3[2]
				pivot4 = Help_Eq_4[2]

				for num_2 in xrange(0, 5):
					Help_Eq_3[num_2] = Help_Eq_3[num_2] / pivot3
					Help_Eq_4[num_2] = Equation_4[num_2] - (pivot4 * Help_Eq_3[num_2])

			if num == 3:
				pivot4 = Help_Eq_4[3]

				for num_2 in xrange(0, 5):
					Help_Eq_4[num_2] = Help_Eq_4[num_2] / pivot4
				
		B3 = (Help_Eq_4[4] / (Help_Eq_4[3]))
		B2 = ((Help_Eq_3[4] - Help_Eq_3[3]*B3)) / Help_Eq_3[2]
		B1 = ((Help_Eq_2[4] - Help_Eq_2[3]*B3 - Help_Eq_2[2]*B2)) / Help_Eq_2[1]
		B0 = ((Help_Eq_1[4] - Help_Eq_1[3]*B3 - Help_Eq_1[2]*B2 - Help_Eq_1[1]*B1)) / Help_Eq_1[0]

		return B0, B1, B2, B3

	def Standard_Deviation(self, Zi, Wi, Xi, Yi, B0, B1, B2, B3):
		#  First we calculate the Variance, and then we get the Stand Dev.
		n = float(len(Wi))
		TotalSum = 0.0
		for num in xrange(0, 6):
			TotalSum += (Zi[num] - B0 - B1*Wi[num] - B2*Xi[num] - B3*Yi[num]) ** 2.0
		
		Variance = (1.0/(n-4.0)) * TotalSum
		Stand_Dev = math.sqrt(Variance)
		return Stand_Dev

	def Range(self, Wi, Xi, Yi, Zi, B0, B1, B2, B3, Wk, W_Avg, Xk, X_Avg, Yk, Y_Avg):
		"""  Range Formula = t(0.35, dof) * StandDev * SquareRoot[1 + 1/n 
																	+ ((Wk - WAvg)^2 / Sum(Wi - WAvg)) 
																	+ ((Xk - XAvg)^2 / Sum(Xi - XAvg)) 
																	+ ((Yk - YAvg)^2 / Sum(Yi - YAvg))] """
		Ops = Operations()
		p = 0.35
		inital_X = 4.0
		dof = float(len(Wi)) - 4.0
		num_seg = 10.0
		leng = num_seg
		
		self.t_Int = Ops.Calculation_X(p, inital_X, dof, num_seg, leng)
		Standard_Dev = self.Standard_Deviation(Zi, Wi, Xi, Yi, B0, B1, B2, B3)

		Sum_Wi = 0.0
		Sum_Xi = 0.0
		Sum_Yi = 0.0
		for num in xrange(0, len(Wi)):
			Sum_Wi += ((Wi[num] - W_Avg) ** 2.0)
			Sum_Xi += ((Xi[num] - X_Avg) ** 2.0)
			Sum_Yi += ((Yi[num] - Y_Avg) ** 2.0)

		Added = (Wk - W_Avg) ** 2.0
		Reused = (Xk - X_Avg) ** 2.0
		Mod = (Yk - Y_Avg) ** 2.0

		Square_Root = math.sqrt(1.0 + (1.0 / len(Wi)) + (Added/Sum_Wi) + (Reused/Sum_Xi) + (Mod/Sum_Yi))
		Range = self.t_Int * Standard_Dev * Square_Root
		return Range


class Main():
	#  For a better understandig, check the table of contents.
	def Program_8(self):
		#  Objects from the Classes we're going to use
		reader = Reader()
		Gauss = Multiple_Regression_And_Equations()
		Reg_Corr = Regression_Correlation()
		Stat_Ops = Statistics_Ops()

		print "Welcome to Program 8..."
		print "Starting..."

		reader = Reader()
		self.allData = reader.read()

		#  We set up the input data
		Wk = float(raw_input("LOC of Added Code (W): "))
		Xk = float(raw_input("LOC of Reused Code (X): "))
		Yk = float(raw_input("LOC of Mod Code (Y): "))

		array_W = []
		array_X = []
		array_Y = []
		array_Z = []

		#  We manage the data from the file
		for w in range(6):
			array_W.append(float(self.allData[w]))

		for x in range(6, 12):
			array_X.append(float(self.allData[x]))

		for y in range(12, 18):
			array_Y.append(float(self.allData[y]))

		for z in range(18, 24):
			array_Z.append(float(self.allData[z]))

		#  We calculate the the Sum of each Column...
		self.Total_W = Reg_Corr.Total_Sum(array_W)
		self.Total_X = Reg_Corr.Total_Sum(array_X)
		self.Total_Y = Reg_Corr.Total_Sum(array_Y)
		
		#  So we can calculate the Average
		self.Avg_W = Stat_Ops.mean(self.Total_W, len(array_W))
		self.Avg_X = Stat_Ops.mean(self.Total_X, len(array_X))
		self.Avg_Y = Stat_Ops.mean(self.Total_Y, len(array_Y))

		#  Then we set up the equations for the Gauss method
		self.Equation_1 = Gauss.Equation_1(array_W, array_X, array_Y, array_Z)
		self.Equation_2 = Gauss.Equation_2(array_W, array_X, array_Y, array_Z)
		self.Equation_3 = Gauss.Equation_3(array_W, array_X, array_Y, array_Z)
		self.Equation_4 = Gauss.Equation_4(array_W, array_X, array_Y, array_Z)

		#  We calculate the Beta's with the Gauss Regression Method, and calculate the remaining variables
		self.B0, self.B1, self.B2, self.B3 = Gauss.Guass_Method(self.Equation_1, self.Equation_2, self.Equation_3, self.Equation_4)
		self.Range = Gauss.Range(array_W, array_X, array_Y, array_Z, self.B0, self.B1, self.B2, self.B3, Wk, self.Avg_W, Xk, self.Avg_X, Yk, self.Avg_Y)
		Zk = self.B0 + Wk*self.B1 + Xk*self.B2 + Yk*self.B3
		UPI = Zk + self.Range
		LPI = Zk - self.Range

		#  Finally, we print the results
		print "\nBETA 0: ", round(self.B0, 5)
		print "BETA 1: ", round(self.B1, 5)
		print "BETA 2: ", round(self.B2, 5)
		print "BETA 3: ", round(self.B3, 5)
		print "Projected Hours: ", round(Zk, 2)
		print "UPI: ", round(UPI, 2)
		print "LPI: ", round(LPI, 2)

#  Execute Main Program
if __name__ == "__main__":
	main = Main()
	main.Program_8()
