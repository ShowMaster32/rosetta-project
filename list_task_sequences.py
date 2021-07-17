import os
import subprocess
import numpy as np
import random
#from PIL import Image  # or you can use the keras one to load images

#elem_select = ["Averages-Pythagorean-means", "Fibonacci-sequence","Greatest-element-of-a-list", "Inheritance-Single", "Anagrams-Deranged-anagrams",  "Sort-an-integer-array", "A+B", \
#        "Loops-While", "Hello-world-Text", "Input-loop", "Temperature-conversion", "Palindrome-detection", "Tokenize-a-string", "Sum-digits-of-an-integer", "Sorting-algorithms-Quicksort",  \
#        "Sorting-algorithms-Merge-sort", "Sorting-algorithms-Bubble-sort", "Substring-Top-and-tail", "Roman-numerals-Encode", "Even-or-odd"] 

#elem_select = ["Fibonacci-sequence", "Sort-an-integer-array", "A+B", "Loops-While", "Hello-world-Text", "Input-loop", "Temperature-conversion", \
#        "Palindrome-detection", "Tokenize-a-string", "Sorting-algorithms-Quicksort", "Substring-Top-and-tail", "Roman-numerals-Encode", "Even-or-odd"] 

elem_select = ["Loops-For", "Sort-an-integer-array", "Inheritance-Single", "Loops-While", "Hello-world-Text", "Temperature-conversion", \
        "Palindrome-detection", "Tokenize-a-string", "Roman-numerals-Encode", "Even-or-odd", "Arrays", "XML-XPath", "Sleep", "Call-a-function", "Check-that-file-exists"] 


list_of_files = []
for name in elem_select:
        for ins_folder in os.listdir("Task/" + name + "/"):
                path = "Task/" + name + "/" + ins_folder + "/"
                if os.path.isdir(path):
                        for f in os.listdir(path):
                                if os.path.isfile(path + f):
                                        list_of_files.append((path + f, path, f, ins_folder, name))

random.shuffle(list_of_files)

for src, path, f, ins_folder, name in list_of_files:
        print(src + "," + name)


