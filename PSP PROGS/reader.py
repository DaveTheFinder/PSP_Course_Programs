import os.path

arr = []



with open('reader.py', 'r') as myFile:
	for lines in myFile:
		for data in lines.strip().split('\n'):
			if data != "":
				arr.append(data)

for line in arr:
	print line
"""
"""

if arr[9] != "":
	print "Hello"
