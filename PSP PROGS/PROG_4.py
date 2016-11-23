"""
Program Assignment: Prog 4
Name: David Ernesto Saenz Saenz
Date: 09/16/2016

Listing Contents:
	Reuse instructions:
			Class Main:
				Purpose: Main Class for the program 4
				Limitations: NOT REUSABLE, just Base code
				Def Program4(self):
					Purpose: Set up the mode for both different options of the program: Must input 1 or 2; 1 for Test 1, 2 for Test 2
				Def Loc_Mode(self):
					Purpose: Set up the data for the Test 1 mode or Class LOC mode
				Def Other_Mode(self):
					Purpose: Set up the data for the Test 2 mode or any other regular mode
				Def SetUpAndExecution(self, data):
					Purpose: Set up and execute the instructions to get the Code Size estimates: VS, S, M, L, VL
			
			Class Log_Ops_And_Size_Calculations:
				Purpose: Holds the methods for the Logarithmic Operations and Code Size Calculations
				Limitations: REUSABLE. Works with Float format numbers and only format numbers.
				Def ln(self, x):
					Purpose: Calculates the Log Normal for every value of a given array of values
					Limitations: Returns an array of values.
				Def Variance(self, arrayLnx, avg):
					Purpose: Calculates the Variance from a given array of Ln values(x) and the Average of the Ln(x): It's calculated based on the Standard Variation formula.
					Limitations: Returns a float format number.
				Def Calc_VS / Def Calc_S / Def Calc_M / Def Calc_L / Def Calc_VL (self, avg, Stand_Dev): 
					Purpose: Calculates the Very Small, Small, Medium, Large, Very Large size from the given Average of Ln(x) and the Standard Deviation
					Limitations: Returns an float format number
	Imports:
		math
		numpy as np

	Class declarations:
		Main:
		Log_Ops_And_Size_Calculations:
		
	Source code in .../<current_dir>/
		From Prog_1 
			=> Class Reader 
				=> Def read
			=> Class Statistics_Ops
				=> Def mean
				=> Def standard_deviation
		From Prog_3
			=> Class Regression_Correlation
				=> Def Total_Sum
"""

import math
import numpy as np
from PROG_1 import Reader, Statistics_Ops
from PROG_3 import Regression_Correlation

class Log_Ops_And_Size_Calculations:
	#  Read the table of contents to understand the function of each part of this Class
	#  Needed for the Standard Deviation calculation: to get the Variance
	Reg_Cor = Regression_Correlation()

	def ln(self, x):
		ln = []
		for n in xrange(len(x)):
			log = np.log(x[n])
			ln.append(log)
		return ln

	def Variance(self, arrayLnx, avg):
		Stat_Ops = Statistics_Ops()
		Standard_Deviation = Stat_Ops.standard_deviation(arrayLnx, avg, len(arrayLnx))
		return (Standard_Deviation ** 2)

	def Calc_VS(self, avg, Stand_Dev):
		ln_VS = avg - (2*Stand_Dev)
		VS = np.exp(ln_VS)
		return VS

	def Calc_S(self, avg, Stand_Dev):
		ln_S = avg - (Stand_Dev)
		S = np.exp(ln_S)
		return S

	def Calc_M(self, avg, Stand_Dev):
		ln_M = avg
		M = np.exp(ln_M)
		return M

	def Calc_L(self, avg, Stand_Dev):
		ln_L = avg + (Stand_Dev)
		L = np.exp(ln_L)
		return L

	def Calc_VL(self, avg, Stand_Dev):
		ln_VL = avg + (2*Stand_Dev)
		VL = np.exp(ln_VL)
		return VL

class Main:
		#  Read the table of contents to understand the function of each part of this Class
	def Program4(self):
		print "Welcome to the Program 4..."
		print "Starting..."

		#  MUST input a working value: 1 or 2
		mode = raw_input("Which test is it going to be? \n1 for LOC_Mode Test \n2 for the Regular Mode Test: \n")

		read = Reader()
		self.allData = read.read()

		#  1 will set of the mode for the Test 1
		if mode == "1":
			self.LOC_Mode(self.allData)
		#  2 will set up the mode for the Test 2
		elif mode == "2":
			self.Other_Mode(self.allData)
		#  Anything else will be discarded
		else:
			print "Wrong mode. Terminating now. Bye!"

	def LOC_Mode(self, allData):
		Stat_Ops = Statistics_Ops()

		#  Two arrays to calculate the Average between the Class LOC and the number of Methods
		array_ClassLoc = []
		array_nMethods=[]

		#  Each data is set to their respective array
		for x in xrange(0, (len(allData))/2):
			array_ClassLoc.append(float(allData[x]))

		for x in xrange(((len(allData))/2) , len(allData)):
			array_nMethods.append(float(allData[x]))

		#  We calculate the Average, which will be the data used to calculate the Sizes
		data = []
		for x in xrange(len(array_ClassLoc)):
			self.n = Stat_Ops.mean(array_ClassLoc[x], array_nMethods[x])
			data.append(self.n)

		#  We execute the operations to calculate the Sizes
		self.SetUpAndExecute(data)


	def Other_Mode(self, allData):
		data = []
		for x in xrange(0, len(allData)):
			data.append(float(allData[x]))
		
		#  We execute the operations to calculate the Sizes
		self.SetUpAndExecute(data)

	def SetUpAndExecute(self, data):
		#  We initiallize the objects needed from the Classes to calculate the data
		LOG_OPS = Log_Ops_And_Size_Calculations()
		Reg_Cor = Regression_Correlation()
		Stat_Ops = Statistics_Ops()

		#  We calculate Ln(x)
		self.ln_array = LOG_OPS.ln(data)
		print "Ln(x): ", self.ln_array

		#  We then get the Sum of Ln(x)
		self.Sum_ln_array = Reg_Cor.Total_Sum(self.ln_array)
		print "Sum Ln(x): ", self.Sum_ln_array

		#  We calculate the Average of Ln(x)
		self.AvgX = Stat_Ops.mean(self.Sum_ln_array, len(self.ln_array))
		print "AVG X: ", self.AvgX

		#  Then, we obtain the Variance
		self.Vari = LOG_OPS.Variance(self.ln_array, self.AvgX)
		print "Variance: ", self.Vari

		#  Eassly, we can get the Standard Deviation from the Variance
		Stand_Dev = math.sqrt(self.Vari)
		print "Standard Deviation: ", Stand_Dev

		#  We then calculate the sizes from the given data
		self.VS = LOG_OPS.Calc_VS(self.AvgX, Stand_Dev)
		self.S = LOG_OPS.Calc_S(self.AvgX, Stand_Dev)
		self.M = LOG_OPS.Calc_M(self.AvgX, Stand_Dev)
		self.L = LOG_OPS.Calc_L(self.AvgX, Stand_Dev)
		self.VL = LOG_OPS.Calc_VL(self.AvgX, Stand_Dev)

		#  Finally, we print the results on screen
		print "\nVS: ", round(self.VS, 4)
		print "S: ", round(self.S, 4)
		print "M: ", round(self.M, 4)
		print "L: ", round(self.L, 4)
		print "VL: ", round(self.VL, 4), "\n"

#  Execute Main Program
if __name__ == "__main__": 
	main = Main()
	main.Program4()		