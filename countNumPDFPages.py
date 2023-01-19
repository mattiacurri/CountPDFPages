import PyPDF2
import os
import sys

n = len(sys.argv)
sumDir = [-1] * n
directory = [-1] * n

for i in range(1, n):
    print()
    print("Path number", i)
    sum = 0
    directory[i] = sys.argv[i]

    if os.path.exists(directory[i]):
        for filename in os.listdir(directory[i]):
            f = os.path.join(directory[i], filename)
            if f.endswith('.pdf'):
                file = open(f, 'rb')
                readpdf = PyPDF2.PdfReader(file)
                sum += len(readpdf.pages)
                print("File:", f.replace(directory[i] + "\\", ""), "Num pages:", len(readpdf.pages))
                sumDir[i] = sum
    else:
        print("Argument number", i, "not found")

filteredSum = [x for x in sumDir if x != -1]
print(filteredSum)
