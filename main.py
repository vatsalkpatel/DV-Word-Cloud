import pdfparser
import stopwords
import cloud
import re
from nltk import *
from nltk.stem import WordNetLemmatizer
import sys
import webbrowser
import numpy 
from numpy import unicode




def process_text(text,excludewords):
        """Splits a long text into words, eliminates the stopwords.
        Parameters
        ----------
        text : string
            The text to be processed.
        Returns
        -------
        words : dict (string, int)
            Word tokens with associated frequency.
        ..versionchanged:: 1.2.2
            Changed return type from list of tuples to dict.
        Notes
        -----
        There are better ways to do word tokenization, but I don't want to
        include all those things.
        """

        stopwords = set([i.lower() for i in excludewords])
        regexp = r"\w[\w']+"
        words = re.findall(regexp, text)
        #print(words)
        # remove stopwords
        words = [word for word in words if word.lower() not in stopwords]
        # remove 's
        words = [word[:-2] if word.lower().endswith("'s") else word
                 for word in words]
        # remove numbers
        words = [word for word in words if not word.isdigit()]
        
        #removing all grammar
        for i,word in enumerate(words):
            if word.lower()[-3:] == 'ies':
                words[i] = word[:-3]+'y'
            if word.lower()[-1] == 's' and word.lower()[-2:] != 'ss':
                words[i] = word[:-1]
        #print(words[i])    

        #count the frequency
        words = FreqDist(sorted(words))
        words = sorted(words.items(), key=lambda x: x[1], reverse=True)
        print(words)
        return words



def main():

    # specify the name of the pdf. Ensure pdf is in same folder
    path = 'John_Smith_SWE_resume.01.pdf'

    # width of the picture
    WIDTH = 1280

    # height of the picture
    HEIGHT = 720

    # Number of words in the cloud
    NUM_OF_WORDS = 250

    # Name of the image
    image_file_name = 'my_word_cloud'

    # If you want to exclude certain words from the cloud,
    # you can add them as a new line to the file stopwords.txt
    # Currently stopwords.txt only contain Stop Words

    pdf_to_word = pdfparser.get_string_from_pdf(path)
    excludewords = stopwords.stopWords('stopwords.txt')
    process_text(pdf_to_word,excludewords)

if __name__ == '__main__':
    main()
# for website only   
f = open('helloworld.html','wb')
message = b"""<!DOCTYPE html>
<html>
 <head>
  <title>Word Cloud Chart</title>
  <style>
    html, body, #container {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    }
  </style> 
 </head>
  <body>
   <div id="container"></div>
    <script>
        <!-- chart code will be here -->
    </script>
  </body>
</html>"""
f.write(message)
f.close()
webbrowser.open_new_tab('helloworld.html')
# done for website



# // add an event listener
# chart.listen("pointClick", function(e){
#   var url = "https://en.wikipedia.org/wiki/" + e.point.get("x");
#   window.open(url, "_blank");
# });