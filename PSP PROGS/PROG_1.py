"""
Program Assignment: Prog 1
Name: David Ernesto Saenz Saenz
Date: 08/17/2016
"""
"""
Listing Contents:
	Reuse instructions:
			Class Node:
				Purpose: To create Nodes with given elements: Number or Text
				Limitations: Previously secify what type of element you are going to add: Number or Text.
				Avoid adding Null elements

			Class LinkedList:
				Purpose: To create a LinkedList with given Nodes
				Limitations: Avoid adding void/Null Nodes, and Nodes of different type, unless that's what you need
				Def addNode(self, content):
					Purpose: To add a node to the Linked List
					Limitations: Avoid adding void/Null Nodes, and Nodes of different type, unless that's what you need
				Def get_total_sum(self):
					Purpose: Returns the total summation of all elements from the Linked List
					Limitations: Works only with number formats (Floats)
				Def return_elements(self):
					Purpose: Return all the elements into an array
					Limitations: Must have an array declarated first

			Class Statistics_Ops:
				Purpose: To make the statistics operations: Mean and Standard Deviation
					Def mean(self, Sum, TotalElements):
						Purpose: Calculates and returns the mean of a given set of values (total sum of the 'n' numbers) and their 'n' number of elements
					Def standard_deviation(self, xi, xAvg, n):
						Purpose: Calculates the standard deviation
						Limitations: receives the Xi, the average of X (mean), and the n (total number of elements)
						Tip: Read about Standard Deviation in Statistics references. 

			Class Reader:
				Purpose: To Read a File				
				Def read(self):
					Purpose: To read a file and return an array with it's content
					Limitations: Returns exactly as it comes in the file (spaces) 

	Imports:
		os.path
		sys
		math

	Class declarations:
	Node:
	LinkedList:
	Reader:
	Statistics_Ops
	Main:

	Source code in .../<current_dir>/
		No source code used in thos program:
"""

import os.path
import sys
import math

class Node:
	#  For a better understandig, check the table of contents.
	def __init__(self, content):
		self.content = content
		self.next = None
		self.behind = None


class LinkedList:
	#  For a better understandig, check the table of contents.

	def __init__(self):
		self.head = None
		self.total_elm = 0.0

	#  To add a node, and also create it
	def addNode(self, content):
		node = Node(content)	
		if self.head == None:
			self.head = node
			self.total_elm += 1.0
		else:
			node.next = self.head
			node.next.behind = node
			self.head = node
			self.total_elm += 1.0

	"""
	To get the sum of all elements (content)
	CAREFUL: Only works with number formats
	"""
	def get_total_sum(self):
		Sum = 0.0
		current_node = self.head
		if current_node != None:
			while current_node != None:
				Sum += current_node.content
				current_node = current_node.next
		return Sum

	#  Return the elements of the linked list into and array
	def return_elements(self):
		List = []
		current_node = self.head
		if current_node != None:
			while current_node != None:
				List.append(current_node.content)
				current_node = current_node.next
		return List


class Reader:
	#  For a better understandig, check the table of contents.	
	def read(self):
		allData = []
		file_name = raw_input("Welcome. Introduce the name of the file to read: ")
		with open (file_name, 'r') as the_file:
			for lines in the_file:
				for data in lines.strip().split('\n'):
					if data != "":
						allData.append(data)
		return allData


class Statistics_Ops:
	#  For a better understandig, check the table of contents.	

	def mean(self, Sum, TotalElments):
		mean = (Sum / TotalElments)
		return mean 

	def standard_deviation(self, xi, xAvg, n):
		inter_valu = 0.0
		stand_var = 0.0
		
		for x in range(int(n)):
			inter_valu += (xi[x] - xAvg) ** 2

		standard_deviation = math.sqrt(inter_valu/float(n-1.0))
		return standard_deviation


class Main:
	#  Why 66? - Main method of the Main Class
	def Order_66(self):
		print "\nHello! Starting program..."
		print "We will pass you to the file reader now"

		#  Reader initialization to read the file
		reader = Reader()

		#  We obtain the data from the file
		self.allData = reader.read()
		firstArray = []
		secondArray = []

		#  Then, we assign the values to their respective arrays
		for x in range(10):
			firstArray.append(self.allData[x])

		for y in range(10,20):
			secondArray.append(self.allData[y])

		print "\nFile read correctly! Proccesing data now...\n"
		
		#  Objects initialization Linked List and Operations Class
		Column_One = LinkedList()
		Column_Two = LinkedList()
		Operations = Statistics_Ops()

		#  Creating each Linked List
		for num in firstArray:
			Column_One.addNode(float(num))

		for num in secondArray:
			Column_Two.addNode(float(num))
		
		"""
		We begin to get the corresponding data for the Mean of Column 1,
		and then, calculat it.
		"""
		totalColOne = Column_One.get_total_sum()
		totalElemOne = Column_One.total_elm
		meanTotalOne = Operations.mean(totalColOne, totalElemOne)
		print "Mean Column 1: ", meanTotalOne

		"""
		We begin to get the corresponding data for the Mean of Column 2,
		and then, calculat it.
		"""
		totalColTwo = Column_Two.get_total_sum()
		totalElemTwo = Column_Two.total_elm
		meanTotalTwo = Operations.mean(totalColTwo, totalElemOne)
		print "Mean Column 2: ", meanTotalTwo

		#  Obtaining the Xi for each Column
		xi_colm_one = Column_One.return_elements()
		xi_colm_two =  Column_Two.return_elements()
		
		#  Finally, we proceed with the calculation for the Standard Deviation for Column 1
		standDeviationColOne = Operations.standard_deviation(xi_colm_one, meanTotalOne, totalElemOne)
		print "Standard Variation Column 1: ", round(standDeviationColOne, 2)

		#  Finally, we proceed with the calculation for the Standard Deviation for Column 1
		standDeviationColTwo = Operations.standard_deviation(xi_colm_two, meanTotalTwo, totalElemTwo)
		print "Standard Variation Column 2: ", round(standDeviationColTwo, 2)

#  Execute Main Class
if __name__ == "__main__": 
	main = Main()
	main.Order_66()