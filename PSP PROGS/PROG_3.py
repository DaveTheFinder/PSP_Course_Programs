"""
Program Assignment: Prog 3
Name: David Ernesto Saenz Saenz
Date: 09/07/2016
"""
"""
Listing Contents:
	Reuse instructions:
		NOT REUSABLE
			Class Main:
				Purpose: Main Class for the program 3
				Limitations: Not Reusable, just Base code
				Def Program3(self):
					Purpose: Execute the program 3 on the respective requirements described in the document.
					Limitations: Not reusable, just Base code.

	Reuse instructions:
			Class Regression_Correlation:
				Purpose: Holds the methods for the respective Regression and Correlation calculations 
				Limitations: For a better understanding, read about statistics subjects (Program 3 from PSP).
				Def Regression_Beta_0(self, avgY, Beta1, avgX):
					Purpose: Calculates Regression Beta 0 given the arguments of Average of Y, Beta 1, and Average of X
					Limitations: Must obtain Beta 1 first.
				Def Regression_Beta_1(self, xy, avgX, avgY, sumX2, num, avgX2):
					Purpose: Calculates Regression Beta 1 given the arguments of Sum of X and Y, Average of X, Average of Y, Sum of X Squared,
							the n number of elements, and the Average of X Squared.
					Limitations: Understand statistics concepts.
				Def Regression_Beta_1(self, xy, avgX, avgY, sumX2, num, avgX2):
					Purpose: Calculates Regression Beta 1 given the arguments of Sum of X and Y, Average of X, Average of Y, Sum of X Squared,
							the n number of elements, and the Average of X Squared.
					Limitations: Understand statistics concepts.
				Def Yk(self, Beta0, Beta1, xK):
					Purpose: Calculates the Linear Regression given the arguments of Beta 0, Beta 1, and proxy Size
					Limitations: Must calculate Beta 0 and Beta 1 first.
				Def Total_Sum(self, array):
					Purpose: Calculates the Total Sum from a list of elements
					Limitations: Only works with number formats. The Range is set manually.
				Def Correlation_rxy(self, xy, sumX, sumY, sumX2, sumY2):
					Purpose: Calculates the Correlation of rx,y given the arguments of Sum of X and Y, Sum of X, Sum of Y, Sum of X Squared, and Sum of Y Squared
							and the number of elements.
					Limitations: The number of elements is a float		
					
	Imports:
		os.path
		sys
		math

	Class declarations:
	Main:
	Regression_Correlation:

	Source code in .../<current_dir>/
		From Prog_1 
			=> Class Reader 
				=> Def read
			=> Class Statistics_Ops
				=> Def mean
			=> Class LinkedList
				=> Def addNode
				=> Def get_total_sum
				=> Def return_elements
"""

import math
import os.path
import sys
from PROG_1 import Reader, Statistics_Ops, LinkedList

class Regression_Correlation:
	#  For a better understandig, check the table of contents.

	#  Returns a number (float/int); use correct formats
	def Regression_Beta_0(self, avgY, Beta1, avgX):
		return (avgY - (Beta1 * avgX))

	# Returns a number (float)
	def Regression_Beta_1(self, xy, avgX, avgY, sumX2, num, avgX2):
		up = 0.0
		down = 0.0
		up = ((xy) - (num * avgX * avgY))
		down = ((sumX2) - (num * (avgX * avgX)))
		return (up / down)

	# Returns a number (float)
	def Yk(self, Beta0, Beta1, xK):
		return (Beta0 + (Beta1 * xK))

	# Returns a number (float)
	def Total_Sum(self, array):
		Sum = 0.0
		for x in xrange(len(array)):
			Sum += array[x]
		return Sum

	# Returns a number (float)
	def Correlation_rxy(self, xy, sumX, sumY, sumX2, sumY2, num):
		up = 0.0
		down = 0.0
		up = ((num * xy) - (sumX * sumY))
		down = math.sqrt( ((num * sumX2) - (sumX * sumX)) * ((num * sumY2) - (sumY * sumY)) )
		return (up / down)


class Main:
	#  For a better understandig, check the table of contents.

	def Program3(self):
	#  For a better understandig, check the table of contents.
		print "Starting Program 3..."
		print "Getting ready to read the file of the Test..."
		
		#  We create objects from the needed Classes
		Operations = Regression_Correlation()
		Stat_Operations = Statistics_Ops()
		read = Reader()

		#  We read the data from the Test file(s)
		self.data = read.read()
		array_1 = []
		array_2 = []

		#  We assign them to an array, to diferentiate them
		for x in range(10):
			array_1.append(self.data[x])

		for y in range(10, 20):
			array_2.append(self.data[y])

		#  Objects from Linked List Class
		X_Column = LinkedList()
		Y_Column = LinkedList()

		#  We create the Linked List with the given data
		for x in array_1:
			X_Column.addNode(float(x))

		for y in array_2:
			Y_Column.addNode(float(y))

		"""
		The next sections are code blocs to obtain the respective
		parameters to get the data asked in the Program 3 document.
		E X, SUM X, AVG X, SUM X2, AVG X2.
		So we do it for the section of Y.
		"""
		SumX_Column = X_Column.get_total_sum()
		nX_Column = X_Column.total_elm
		elementsX_Column = X_Column.return_elements()
		self.Avg_X = Stat_Operations.mean(SumX_Column, nX_Column)
		print "Column X: ", elementsX_Column

		elementsX_Square_Column = []
		for x in elementsX_Column:
			square = x*x
			elementsX_Square_Column.append(square)

		self.SumX_Square_Column = Operations.Total_Sum(elementsX_Square_Column)
		self.Avg_X_Square_Column = Stat_Operations.mean(self.SumX_Square_Column, float(len(elementsX_Square_Column)))

		#  Section Y. Same data as the previous code block
		SumY_Column = Y_Column.get_total_sum()
		nY_Column = Y_Column.total_elm
		elementsY_Column = Y_Column.return_elements()
		self.Avg_Y = Stat_Operations.mean(SumY_Column, nY_Column)
		print "Column Y: ", elementsY_Column

		elementsY_Square_Column = []
		for y in elementsY_Column:
			square = y*y
			elementsY_Square_Column.append(square)

		self.SumY_Square_Column = Operations.Total_Sum(elementsY_Square_Column)
		self.Avg_Y_Square_Column = Stat_Operations.mean(self.SumY_Square_Column, float(len(elementsY_Square_Column)))

		#  We obtain the XY data
		X_per_Y = []
		for value in range(10):
			xy = elementsX_Column[value] * elementsY_Column[value]
			X_per_Y.append(xy)
			xy = 0.0
		self.SumXY = Operations.Total_Sum(X_per_Y)


		#  We obtain the final data: Beta 1, Beta 0, r x,y, r2 (Squared) and the Linear Regression yK
		self.Beta_1 = Operations.Regression_Beta_1(self.SumXY, self.Avg_X, self.Avg_Y, self.SumX_Square_Column, 10.0, self.Avg_X_Square_Column)
		self.rxy = Operations.Correlation_rxy(self.SumXY, SumX_Column, SumY_Column, self.SumX_Square_Column, self.SumY_Square_Column, 10.0)
		R2 = self.rxy * self.rxy
		self.Beta_0 = Operations.Regression_Beta_0(self.Avg_Y, self.Beta_1, self.Avg_X)
		self.YK = Operations.Yk(self.Beta_0, self.Beta_1, 386.0)

		#  Finally, we print the results
		print "\nRESULTS:"
		print "\nBeta0: ", round(self.Beta_0, 4)
		print "Beta1: ", round(self.Beta_1, 4)
		print "r x,y: ", round(self.rxy, 4)
		print "r2: ", round(R2, 4)
		print "yk: ", round(self.YK, 4)
		print ""


#  Execute Main Program
if __name__ == "__main__": 
	main = Main()
	main.Program3()