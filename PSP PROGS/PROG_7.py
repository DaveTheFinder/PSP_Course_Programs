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
					Limitations: Set to 1 and 2 Only. 1 For the Default Data, 
					2 for the Personal Data. 
					Default Data is the data given by the document's table.
					The Personal Data is the data from Prog 3-6
				Def Program_Default_Data(self):
					Purpose: Sets program Data with the Default Data 
							(From the document)
							This method is exclusively for the First and the
							Second Test.
					Limitations: Data must be numbers.
				Def Program_Personal_Data(self):
					Purpose: Sets program Data with the Personal Data 
							(From the user's history).
							This method is exclusively for the Third and 
							Fourth Test.
					Limitations: Data must be numbers.
				Def Program_7(self, self, X_Column, Y_Column, xK, n):
					Purpose: Executes the main processes of the program 7.
					Limitations: Data must be correct. 
								 It uses base code from the program 3, to 
								 calculate everything related with the regression. 
								 It can be reused only as base code, but take 
								 consideration that it's already base code from program 3

	Reuse instructions:	
			Class Prediction_And_Signyficance():
				Purpose: Holds the methods to calculate the Prediction and the 
						 Significance for the Program 7
				Limitations: REUSABLE. Works with Float format numbers and only 
							 format numbers. 
							 Note: Everything returns a float number.
				Def Signyficance(self, rxy, n):
					Purpose: To calculate the Significance from the Correlation 
							 (X value) to be used in the Tail Area.
							 X = (ABS|rxy|SquareRoot[n - 2]) / SquareRoot[1 - (rxy*rxy)]
					Limitations: Returns a Float number
				Def Tail_Area(self, x, n):
					Purpose: Calculates the Tail Area with the t Distribution
					Limitations: Return a Float number.
				Def Range(self, n, yi, B0, B1, xi, xk, Avg_X):
					Purpose: Calculates the Prediction Interval (70%)
					Limitations: Returns a Float number.
								 Range = t(0.35, dof) * StandardDeviation *
								 		 SquareRoot[1 + 1/n + ((Xk - Xavg)^2 / 
								 		 			Sum[(Xi - Xavg)^2] )] 
				Def Standard_Deviation(self, n, yi, B0, B1, xi):
					Purpose: Calculates the Standard Deviation with the new formula 
							 with the given params.
							 d = SquareRoot[(1 / (n -2)) * Sum[Yi - B0 - B1Xi]]
					Limitations: Return a Float number.
								 
	Class declarations:
		Main():
		Prediction_And_Signyficance():
		
	Source code in .../<current_dir>/
		From Prog_1 
			Class Reader
				Def read
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

"""
- Prog_1's Reader, Statistics_Ops and LinkedList 
	to read and manage the data.
- Prog_3's Regression_Correlation 
	to get the Regression used to
	calculate the Significance.
- Prog_5's Integration_And_tDistribution 
	to calculate P with the Simpson method.
- And Prog_6's Operations 
	to calculate the value of X, with a given
	P value.
"""
import math
from PROG_1 import Reader, Statistics_Ops, LinkedList
from PROG_3 import Regression_Correlation
from PROG_5 import Integration_And_tDistribution
from PROG_6 import Operations

class Prediction_And_Signyficance():
	#  For a better understandig, check the table of contents.
	def Signyficance(self, rxy, n):
		x = ((math.fabs(rxy)) * (math.sqrt(n - 2.0))) / (math.sqrt(1.0 - rxy**2.0))
		return x

	def Tail_Area(self, x, n):
		X_Calc = Integration_And_tDistribution()
		num_seg = 10.0
		leng = num_seg
		dof = (n - 2.0)
		E = 0.0000001

		while(True):
			self.Simpson_1 = X_Calc.Simpson(x, num_seg, dof, leng)
			self.Simpson_2 = X_Calc.Simpson(x, num_seg+10.0, dof, leng)
			if(math.fabs(self.Simpson_1 - self.Simpson_2) > E):
				num_seg = num_seg + 10.0
			elif(math.fabs(self.Simpson_1 - self.Simpson_2) < E):
				break

		tail_area = 1.0 - (2.0 * self.Simpson_2)
		return tail_area

	def Range(self, n, yi, B0, B1, xi, xk, Avg_X):
		Ops = Operations()
		p = 0.35
		inital_X = 4.0
		dof = n - 2.0
		num_seg = 10.0
		leng = num_seg
		
		self.t_Int = Ops.Calculation_X(p, inital_X, dof, num_seg, leng)
		Standard_Dev = self.Standard_Deviation(n, yi, B0, B1, xi)

		Sum_X = 0.0
		for num in xrange(0, int(n)):
			Sum_X += ((xi[num] - Avg_X) ** 2.0)

		Square_Root = math.sqrt(1.0 + (1.0 / n) + ( ((xk - Avg_X)** 2.0) / (Sum_X)) )
		Range = self.t_Int * Standard_Dev * Square_Root
		return Range

	def Standard_Deviation(self, n, yi, B0, B1, xi):
		Sum_Op = 0.0
		for num in xrange(0, int(n)):
			Sum_Op += ((yi[num] - B0 - (B1 * xi[num])) ** 2.0)

		Stand_Dev = math.sqrt((1.0 / (n - 2.0)) * (Sum_Op))
		return Stand_Dev


class Main():
	#  For a better understandig, check the table of contents.
	def Program_Mode(self):
		print "Starting Program 7..."
		Mode = raw_input("Introduce the mode of the program.\n1) To Program Data\n2) For Personal Data\nInput: ")

		if Mode == "1":
			self.Program_Default_Data()
		elif Mode == "2":
			self.Program_Personal_Data()
		else:
			print "\nInvalid mode. Exiting now. Peace and prosper."

	def Program_Default_Data(self):
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

		X_Column = LinkedList()
		Y_Column = LinkedList()

		try:
			#  We create the Linked List with the given data
			for x in array_1:
				X_Column.addNode(float(x))

			for y in array_2:
				Y_Column.addNode(float(y))

			xK = 386.0
			n = 10.0

			self.Program_7(X_Column, Y_Column, xK, n)

		except ValueError as e:
			print "\nError: ", e, "\nData is incorrect: Check and correct the .txt file.\n"

	def Program_Personal_Data(self):
		read = Reader()
		self.data = read.read()
		array_1 = []
		array_2 = []

		for x in range(4):
			array_1.append(self.data[x])

		for y in range(4, 8):
			array_2.append(self.data[y])

		X_Column = LinkedList()
		Y_Column = LinkedList()

		try:
			for x in array_1:
				X_Column.addNode(float(x))

			for y in array_2:
				Y_Column.addNode(float(y))

			xK = 379.11
			n = 4.0

			self.Program_7(X_Column, Y_Column, xK, n)

		except ValueError as e:
			print "\nError: ", e, "\nData is incorrect: Check and correct the .txt file.\n"


	def Program_7(self, X_Column, Y_Column, xK, n):
		print "Getting ready to read the file of the Test..."
		
		Operations = Regression_Correlation()
		Stat_Operations = Statistics_Ops()
		Pred_Sign = Prediction_And_Signyficance()

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

		X_per_Y = []
		for value in range(int(n)):
			xy = elementsX_Column[value] * elementsY_Column[value]
			X_per_Y.append(xy)
			xy = 0.0
		self.SumXY = Operations.Total_Sum(X_per_Y)


		#  We obtain the final data: Beta 1, Beta 0, r x,y, r2 (Squared) and the Linear Regression yK
		self.Beta_1 = Operations.Regression_Beta_1(self.SumXY, self.Avg_X, self.Avg_Y, self.SumX_Square_Column, n, self.Avg_X_Square_Column)
		self.rxy = Operations.Correlation_rxy(self.SumXY, SumX_Column, SumY_Column, self.SumX_Square_Column, self.SumY_Square_Column, n)
		R2 = self.rxy * self.rxy
		self.Beta_0 = Operations.Regression_Beta_0(self.Avg_Y, self.Beta_1, self.Avg_X)
		self.YK = Operations.Yk(self.Beta_0, self.Beta_1, xK)
		self.X_Value = Pred_Sign.Signyficance(self.rxy, n)
		self.Tail_Area = Pred_Sign.Tail_Area(self.X_Value, n)
		self.Range = Pred_Sign.Range(n, elementsY_Column, self.Beta_0, self.Beta_1, elementsX_Column, xK, self.Avg_X)
		UPI = self.YK + self.Range
		LPI = self.YK - self.Range

		print "\nRESULTS"
		print "\nBeta0: ", round(self.Beta_0, 9)
		print "Beta1: ", round(self.Beta_1, 9)
		print "r x,y: ", round(self.rxy, 9)
		print "r2: ", round(R2, 9)
		print "yk: ", round(self.YK, 9)
		print "Tail Area: ", round(self.Tail_Area, 10)
		print "Range: ", round(self.Range, 8)
		print "UPI (70%): ", round(UPI, 7)
		print "LPI (70%): ", round(LPI, 7)


#  Execute Main Program
if __name__ == "__main__": 
	main = Main()
	main.Program_Mode()