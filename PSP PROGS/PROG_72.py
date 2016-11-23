"""
Program Assignment: Prog 7
Name: David Ernesto Saenz Saenz
Date: 30/10/2016

Listing Contents:
	Reuse instructions:
			Class Main:
				Purpose: Main Class for the program 7
				Limitations: NOT REUSABLE, just Base code. 
				Def Program_Mode(self):
					Purpose: Set the function mode of the program.
					Limitations: Set to 1 and 2 Only. 1 For the Default Data, 2 for the Personal Data.
				Def Program_Default_Data(self):
					Purpose: Sets program Data with the Default Data (from the document)
					Limitations: Data must be numbers.
				Def Program_Personal_Data(self):
					Purpose: Sets program Data with the Personal Data (from the user's history)
					Limitations: Data must be numbers.
				Def Program_7(self, self, X_Column, Y_Column, xK, n):
					Purpose: Executes the main processes of the program 7.
					Limitations: Data must be correct.

	Reuse instructions:	
			Class Prediction_And_Significance():
				Purpose: Holds the methods to calculate the Prediction and the Significance for the Program 7
				Limitations: REUSABLE. Works with Float format numbers and only format numbers. 
							 Note: Everything returns a float number.
				Def Significance(self, rxy, n):
					Purpose: To calculate the Significance from the Correlation (X value)
					X
					Limitations: Returns a Float number
				Def Tail_Area(self, x, n):
					Purpose: Calculates the Tail Area with the t Distribution
					Limitations: Return a Float number.
				Def Range(self, n, yi, B0, B1, xi, xk, Avg_X):
					Purpose: Calculates the Prediction Interval (70%)
					Limitations: Returns a Float number.
				Def Standard_Deviation(self, n, yi, B0, B1, xi):
					Purpose: Calculates the Standard Deviation with the new formula with the given params.
					Limitations: Return a Float number.
								 
	Class declarations:
		Main():
		Prediction_And_Significance():
		
	Source code in .../<current_dir>/
		From Prog_1
			Class Node 
			Class Reader
				Def read
				Def Statistics_Ops
				Def LinkedList
		From Prog_3
			Class Regression_Correlation
				Def Regression_Beta_0
				Def Regression_Beta_1
				Def Yk
				Def Total_Sum
				Def Correlation_xry
		From Prog_5
			Class Integration_And_tDistribution
				Def Simpson
		From Prog_6
			Class Operations
				Def Calculation_X
"""

import math
from PROG_1 import Reader, Statistics_Ops, LinkedList
from Prog_3 import Regression_Correlation
from Prog_5 import Integration_And_tDistribution
from Prog_6 import Operations

class Prediction_And_Significance():
	#  For a better understanding, check the table of contents.
	def Significance(self, rxy, n):
		x = ((math.fabs(rxy)) * (math.sqrt(n - 2.0))) / (math.sqrt(1.0 - rxy**2.0))
		return x

	def Tail_Area(self, x, n):
		X_Calc = Integration_And_tDistribution()
		num_seg = 10.0
		leng = num_seg
		dof = (n - 2.0)
		E = 0.0000001

		#Using the Simpson Method

		while(True):
			self.Simpson1 = X_Calc.Simpson(x, num_seg, dof, leng)
			self.Simpson2 = X_Calc.Simpson(x, num_seg+10.0, dof, leng)
			if(math.fabs(self.Simpson1 - self.Simpson2) > E):
				num_seg = num_seg + 10.0
			elif (math.fabs(self.Simpson1 - self.Simpson2) < E):
				break

		tail_area = 1.0 - (2.0 * self.Simpson2)
		return tail_area

	def Range(self, n, yi, B0, B1, xi, xk, Avg_X):
		Ops = Operations()
		p = 0.35
		initial_X = 4.0
		dof = n - 2.0
		num_seg = 10.0
		leng = num_seg

		self.t_Int = Ops.Calculation_X(p, initial_X, dof, num_seg, leng)
		Standard_Dev = self.Standard_Deviation(n, yi, B0, B1, xi)

		Sum_X = 0.0
		for num in xrange(0, int(n)):
			Sum_X += ((xi[num] - Avg_X) ** 2.0)

		Square_Root = math.sqrt(1.0 + (1.0 / n) + (((xk - Avg_X) ** 2.0) / Sum_X))
		Range = self.t_Int * Standard_Dev * Square_Root
		return Range
	def Standard_Deviation(self, n, yi, B0, B1, xi):
		Sum_Op = 0.0
		for num in xrange (0, int(n)):
			Sum_Op += ((yi[num] - B0 - (B1 * xi[num])) ** 2.0)
		Stand_Dev = math.sqrt((1.0 / (n - 2.0)) * Sum_Op)




