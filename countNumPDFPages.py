import PyPDF2
import os
import sys

n = len(sys.argv)
# print("\nArguments passed:", end = " ")
# for i in range(1, n):
    #print(sys.argv[i], end = " ")
     

sumDir = [-1] * n
directory = [-1] * n

# assign directory
for i in range(1, n):
	sum = 0
	directory[i] = sys.argv[i]
	
	if os.path.exists(directory[i]):
		# iterate over files in directory
		for filename in os.listdir(directory[i]):
	    		f = os.path.join(directory[i], filename)
	    		if f.endswith('.pdf'):
	    			file = open(f, 'rb')
	    			readpdf = PyPDF2.PdfReader(file)
	    			sum += len(readpdf.pages)
	    			sumDir[i] = sum
	else:
		print("L'argomento numero", i, "non è un percorso esistente")

filtered_array = [x for x in sumDir if x != -1]
print(filtered_array)
