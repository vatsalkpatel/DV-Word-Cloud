import subprocess
 
command = "pip install PyDictionary" #command to be executed
res = subprocess.call(command, shell = True)

command = "pip install nltk" #command to be executed
res = subprocess.call(command, shell = True)

command = "pip install numpy" #command to be executed 
res = subprocess.call(command, shell = True)

command = "pip install PyPDF2" #command to be executed
res = subprocess.call(command, shell = True)

command = "pip install PySimpleGUI" #command to be executed 
res = subprocess.call(command, shell = True)

#the method returns the exit code

command = "python GUI.py " #command to be executed
res = subprocess.call(command, shell = True)