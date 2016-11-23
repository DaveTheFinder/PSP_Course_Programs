"""
Program Assignment: Prog 2
Name: David Ernesto Saenz Saenz
Date: 08/29/2016
"""
"""
Listing Contents:
			Class Main:
				Purpose: Main Class for the Counting program
				Limitations: Not Reusable
				Def MainProgram(self):
					Purpose:
					Limitations: The last 4 lines of all programs should always be the ones to initialize the Main Class 
								and Method plus a one line desc
	Reuse instructions:
		NOT REUSABLE

	Imports:
		os.path
		sys

	Class declarations:
	Main:

	Source code in .../<current_dir>/
		From Prog_1 
			=> Class Reader 
				=> Def read
"""
from PROG_1 import Reader
import os.path
import sys

class Main:
	"""
	Main Class for the LOC Program
	It cointains only one Method, since it is not
	needed for reuse later
	"""
	def LOC(self):
		"""
		LOC Method: Here lies all the operations to calculate the 
		number of lines of code, corresponding with the Program 2
		"""
		"\nWelcome. Starting LOC Program..."

		#  First, we declare the object from Class Reader 
		reader = Reader()
		#  We obtain the full content of the file we read
		self.file_content = reader.read()

		#  With the content of the file, we can know the Total No. Lines of Code
		total_lines_of_code = len(self.file_content)

		#  We will use this variable to count the Classes
		Class_counter = 0
		#  And this array to save the Position where each Class is located 
		array_of_Classes = []

		"""
		These operations serve to save the location where each Class start.
		An If condition is used to exclude itself when counting the Classes,
		since a string 'Class' resides within the If.
		"""
		for x in xrange(0, len(self.file_content)):
			if "class" in self.file_content[x] and "if" not in self.file_content[x]:
				Class_counter += 1
				array_of_Classes.append(x)


		"""
		An array of Methods is used to save the amount of methods within a Class.
		We use an array, to map each Method with its corresponding Class.
		A counter is used to determine how many Methods each Class possess.
		"""
		array_Def_in_Class = []
		Def_counter = 0
		for x in xrange(0, len(array_of_Classes)-1):
			for y in xrange(array_of_Classes[x], array_of_Classes[x+1]):
				if "def" in self.file_content[y] and "if" not in self.file_content[y]:
					Def_counter += 1

			array_Def_in_Class.append(Def_counter)
			Def_counter = 0

		"""
		This specific operation is to calculate the same as above, just for the last Class
		of each program. This was taken in consideration becuase of the logic implemented for
		program, because of an Index Out of Range exception.
		"""
		for z in xrange(array_of_Classes[(len(array_of_Classes)-1)], len(self.file_content)):
			if "def" in self.file_content[z] and "if" not in self.file_content[z]:
				Def_counter += 1

		array_Def_in_Class.append(Def_counter)
		Def_counter = 0

		"""
		The next operations serve to calculate the lines of code per Class.
		- The first case is only for programs with one Class within, since
		they are taken with differently logic.
		- The second case is for every other case.
		They also take in consideration a condition for the last 4 lines
		of code in the program, since they will always be the same to run each
		program, and to be reusable for other programs. 
		"""
		array_lines_in_Class = []
		counter_lines_in_Class = 0

		if len(array_of_Classes) == 1:
			for c in xrange(array_of_Classes[0], len(self.file_content)):
				counter_lines_in_Class += 1
				if (len(self.file_content) - c) <= 4:
					counter_lines_in_Class -= 1
		else:
			for a in xrange(0, len(array_of_Classes)-1):
				for b in xrange(array_of_Classes[a], array_of_Classes[a+1]):
					counter_lines_in_Class += 1
				array_lines_in_Class.append(counter_lines_in_Class)
				counter_lines_in_Class = 0

			"""  
			Calculation of the LOC for the last Class of each Program: 
			From where the Class starts, to the last line of code.
			Excluding the necessary execution and the condition
			to make it portable.
			"""
			for c in xrange(array_of_Classes[(len(array_of_Classes)-1)], len(self.file_content)):
				counter_lines_in_Class += 1
				if (len(self.file_content) - c) <= 4:
					counter_lines_in_Class -= 1

		#  We append the data of the last Class to the array, so it can be mapped
		array_lines_in_Class.append(counter_lines_in_Class)
		counter_lines_in_Class = 0

		"""
		Finally, we print the result obtained
		in a legible and user-friendly way.
		"""
		print "Program Lines Counted: "
		for z in xrange(0, len(array_of_Classes)):
			print "\n\tPart Name: ", self.file_content[array_of_Classes[z]]
			print "\tNumber of Items: ", array_Def_in_Class[z]
			print "\tPart Size: ",array_lines_in_Class[z]
		print "\n\tTotal lines of code: ", total_lines_of_code

#  Execute Main Class
if __name__ == "__main__": 
	main = Main()
	main.LOC()
