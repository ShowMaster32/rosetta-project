import os
import subprocess
import numpy as np
import random
#from PIL import Image  # or you can use the keras one to load images

def generate_bash_cmd_courier(path, f, dest):
        return "cat \"" + path +"\" | convert -background white -density 196 -resample 72 -unsharp 0x.5 -font \"Courier\" text:- -trim +repage -bordercolor white -border 3 -resize 256x256\! " + dest + "/courier-"+ f +".png"

def generate_bash_cmd_times(path, f, dest):
        return "cat \"" + path +"\" | convert -background white -density 196 -resample 72 -unsharp 0x.5 -font \"Times-Roman\" text:- -trim +repage -bordercolor white -border 3 -resize 256x256\! " + dest + "/times-"+ f +".png"

def generate_bash_cmd_bookman(path, f, dest):
        return "cat \"" + path +"\" | convert -background white -density 196 -resample 72 -unsharp 0x.5 -font \"Bookman-Demi\" text:- -trim +repage -bordercolor white -border 3 -resize 256x256\! " + dest + "/bookman-"+ f +".png"

def generate_bash_cmd_avantgarde(path, f, dest):
        return "cat \"" + path +"\" | convert -background white -density 196 -resample 72 -unsharp 0x.5 -font \"AvantGarde-Book\" text:- -trim +repage -bordercolor white -border 3 -resize 256x256\! " + dest + "/avantgarde-"+ f +".png"

stream = os.popen("rm -rf dataset && mkdir dataset")
output = stream.read()

#elem_select = ["Averages-Pythagorean-means", "Fibonacci-sequence","Greatest-element-of-a-list", "Inheritance-Single", "Anagrams-Deranged-anagrams",  "Sort-an-integer-array", "A+B", \
#        "Loops-While", "Hello-world-Text", "Input-loop", "Temperature-conversion", "Palindrome-detection", "Tokenize-a-string", "Sum-digits-of-an-integer", "Sorting-algorithms-Quicksort",  \
#        "Sorting-algorithms-Merge-sort", "Sorting-algorithms-Bubble-sort", "Substring-Top-and-tail", "Roman-numerals-Encode", "Even-or-odd"]

elem_select = ["Loops-For", "Sort-an-integer-array", "Inheritance-Single", "Loops-While", "Hello-world-Text", "Temperature-conversion", \
        "Palindrome-detection", "Tokenize-a-string", "Roman-numerals-Encode", "Even-or-odd", "Arrays", "XML-XPath", "Sleep", "Create-a-file", "Check-that-file-exists"]       

'''
for elem in elem_select:
        stream = os.popen("cd dataset/training && mkdir "+ elem)
        output = stream.read()
        stream = os.popen("cd dataset/validation && mkdir "+ elem)
        output = stream.read()
        stream = os.popen("cd dataset/test && mkdir "+ elem)
        output = stream.read()
'''
list_of_files = []
for name in elem_select:
        for ins_folder in os.listdir("Task/" + name + "/"):
                path = "Task/" + name + "/" + ins_folder + "/"
                if os.path.isdir(path):
                        for f in os.listdir(path):
                                if os.path.isfile(path + f):
                                        list_of_files.append((path + f, path, f, ins_folder, name))

random.shuffle(list_of_files)
#train, validate, test = np.split(list_of_files, [int(len(list_of_files)*0.8), int(len(list_of_files)*0.9)])


for src, path, f, ins_folder, name in list_of_files:
        stream = os.popen(generate_bash_cmd_courier(src, f, "dataset/"))
        output = stream.read()
        print("courier-"+ f + ".png," + "courier" + "," + ins_folder + "," + name) 

for src, path, f, ins_folder, name in list_of_files:
        stream = os.popen(generate_bash_cmd_times(src, f, "dataset/"))
        output = stream.read()
        print("times-"+ f + ".png," + "times" + "," + ins_folder + "," + name)

for src, path, f, ins_folder, name in list_of_files:
        stream = os.popen(generate_bash_cmd_bookman(src, f, "dataset/"))
        output = stream.read()
        print("bookman-"+ f + ".png," + "bookman" + "," + ins_folder + "," + name)

for src, path, f, ins_folder, name in list_of_files:
        stream = os.popen(generate_bash_cmd_avantgarde(src, f, "dataset/"))
        output = stream.read()
        print("avantgarde-"+ f + ".png," + "avantgarde" + "," + ins_folder + "," + name)


        