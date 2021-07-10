import os
import subprocess
import numpy as np
import random
#from PIL import Image  # or you can use the keras one to load images

def generate_bash_cmd(path, f, dest):
        return "cat \"" + path +"\" | convert -background white -density 196 -resample 72 -unsharp 0x.5 -font \"Courier\" text:- -trim +repage -bordercolor white -border 3 -resize 256x256\! " + dest + "/"+ f +".png"


stream = os.popen("rm -rf dataset && mkdir dataset")
output = stream.read()

#stream = os.popen("rm -rf dataset && mkdir dataset && cd dataset && mkdir training && mkdir validation && mkdir test")
#output = stream.read()

elem_select = ["Averages-Pythagorean-means", "Fibonacci-sequence","Greatest-element-of-a-list", "Inheritance-Single", "Anagrams-Deranged-anagrams",  "Sort-an-integer-array", "A+B", \
        "Loops-While", "Hello-world-Text", "Input-loop", "Temperature-conversion", "Palindrome-detection", "Tokenize-a-string", "Sum-digits-of-an-integer", "Sorting-algorithms-Quicksort",  \
        "Sorting-algorithms-Merge-sort", "Sorting-algorithms-Bubble-sort", "Substring-Top-and-tail", "Roman-numerals-Encode", "Even-or-odd"]

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
train, validate, test = np.split(list_of_files, [int(len(list_of_files)*0.8), int(len(list_of_files)*0.9)])


for src, path, f, ins_folder, name in train:
        stream = os.popen(generate_bash_cmd(src, f, "dataset/"))
        output = stream.read()
        print(f + ".png," + "training" + "," + ins_folder + "," + name)

for src, path, f, ins_folder, name in validate:
        stream = os.popen(generate_bash_cmd(src, f, "dataset/"))
        output = stream.read()
        print(f +  ".png," + "validation" + "," + ins_folder + "," + name)

for src, path, f, ins_folder, name in test:
        stream = os.popen(generate_bash_cmd(src, f, "dataset/"))
        output = stream.read()
        print(f +  ".png," + "test" + "," + ins_folder + "," + name)
