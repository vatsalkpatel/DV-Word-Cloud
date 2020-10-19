import pdfparser
import stopwords
import re
from PyDictionary import PyDictionary 
from nltk import *
import sys
import webbrowser
import numpy 
from numpy import unicode
import random




def process_text(text,excludewords):
       
        stopwords = set([i.lower() for i in excludewords])
        regexp = r"\w[\w']+"
        words = re.findall(regexp, text)
        #print(words)
        # remove stopwords
        words = [word.capitalize() for word in words if word.lower() not in stopwords]
        # remove 's
        words = [word[:-2] if word.lower().endswith("'s") else word
                 for word in words]
        # remove numbers
        words = [word for word in words if not word.isdigit()]
        
        #removing all grammar
        for i,word in enumerate(words):
            if word.lower()[-3:] == 'ies':
                words[i] = word[:-3]+'y'
            if word.lower()[-2] == '\'s':
                words[i] = word[:-2]
            if word.lower()[-1] == 's' and word.lower()[-2:] != 'ss':
                words[i] = word[:-1]
            
        #print(words[i])    

        #count the frequency
        words = FreqDist((words))
        words = sorted(words.items(), key=lambda x: x[1], reverse=True)
        #print(words)
        return words



def main(string_of_words):
    # specify the name of the pdf. Ensure pdf is in same folder
    path = string_of_words
    # width of the picture
    WIDTH = 1280

    # height of the picture
    HEIGHT = 720

    # Number of words in the cloud
    NUM_OF_WORDS = 250

    # If you want to exclude certain words from the cloud,
    # you can add them as a new line to the file stopwords.txt
    # Currently stopwords.txt only contain Stop Words

    excludewords = stopwords.stopWords('stopwords.txt')
    return process_text(string_of_words,excludewords)

if __name__ == '__main__':
    dictionary=PyDictionary()
    print("Which of the following you want to do: \n 1) Use pdf file \n 2) Use text file \n 3) want to enter text.\n Enter your input 1 or 2 or 3: ")
    option = input("") 
    if option == '1':
        path = input("give me the whole path of file : ")
        pdf_to_word = pdfparser.get_string_from_pdf(path)
        words = main(pdf_to_word)
    elif option == '2':
        path = input("give me the whole path of file : ")
        f = open(path, "r")
        txt_to_word = f.read()
        words = main(txt_to_word)
    else:
        strings = input("Enter your text :- ")
        words = main(strings)
    # for website only   
    f = open('helloworld.html','w')
    f.write("""<!DOCTYPE html>
    <html>
    <head lang="en">
    <title>Word Cloud Chart</title>
    <style>
        .word{
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black;
        }

        .word .tooltiptext {
        visibility: hidden;
        width: 300px;
        background-color: black;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px 0;
        font-size: 10px;

        /* Position the tooltip */
        position: absolute;
        z-index: 1;
        }

        .word:hover .tooltiptext {
        visibility: visible;
        }

        html, body, #container {
        text-align: center;
        vertical-align: middle;
        font-family: arial;
        background-color:black; 
        width: 100%;
        border:1px solid black;
        height: 100%;
        margin: 0;
        padding: 0;
        }
        html, body, #container, #rest{
        transform : rotate(90);
        font-size: 20px;
        float:left;
        }
        html, body, #container, #small{
        font-size: 40px;
        float:left;
        }
        html, body, #container, #medium{
        transform : rotate(90);
        font-size: 60px;
        float:left;
        }
        html, body, #container, #big{
        font-size: 80px;
        float:left;
        }
        html, body, #container, #huge{
        transform : rotate(90);
        font-size: 100px;
        float:left;
        }
    </style> 
    </head>
    <body>
    <div id="container" >
    """)
    
    for word in words[:50]:
        colour_code = str(int(random.random() * 255))
        colour_code_1 = str(int(random.random() * 255))
        colour_code_2 = str(int(random.random() * 255))
        if word[1]==2:
            f.write("""<div class="word" style="color:rgb(""" +colour_code+","+colour_code_1+","+colour_code_2+""");" id="small"><span class="tooltiptext">Frequency:"""+str(word[1])+"""<p>Meaning:"""+str(dictionary.meaning(word[0]))+"""</p></span>"""+word[0]+"""</div>""")
        elif word[1]>=5:
            f.write("""<div class="word" style="color:rgb(""" +colour_code+","+colour_code_1+","+colour_code_2+""");" id="huge"><span class="tooltiptext">Frequency:"""+str(word[1])+"""<p>Meaning:"""+str(dictionary.meaning(word[0]))+"""</p></span>"""+word[0]+"""</div>""")
        elif word[1]>=4:
            f.write("""<div class="word" style="color:rgb(""" +colour_code+","+colour_code_1+","+colour_code_2+""");" id="big"><span class="tooltiptext">Frequency:"""+str(word[1])+"""<p>Meaning:"""+str(dictionary.meaning(word[0]))+"""</p></span>"""+word[0]+"""</div>""")
        elif word[1]>=3:
            f.write("""<div class="word" style="color:rgb(""" +colour_code+","+colour_code_1+","+colour_code_2+""");" id="medium"><span class="tooltiptext">Frequency:"""+str(word[1])+"""<p>Meaning:"""+str(dictionary.meaning(word[0]))+"""</p></span>"""+word[0]+"""</div>""")
        else:
            f.write("""<div class="word" style="color:rgb(""" +colour_code+","+colour_code_1+","+colour_code_2+""");" id="rest"><span class="tooltiptext">Frequency:"""+str(word[1])+"""<p>Meaning:"""+str(dictionary.meaning(word[0]))+"""</p></span>"""+word[0]+"""</div>""")
    f.write("""
    </div>
        <script>
            
        </script>
    </body>
    </html>""")
    f.close()
    webbrowser.open_new_tab('helloworld.html')
    # done for website