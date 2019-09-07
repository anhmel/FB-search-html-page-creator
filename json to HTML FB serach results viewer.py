"""

This python script reads json search result file, sort results by time/date,
creates links to posts and puts the links together with corresponding messages
and images in an html file. Then the program opens the html file in a default browser. 

1. After getting results of url FB search by the method of T-Rekt, save the 
results page as a json file on your comptuer disk (graphSearch.json). 
2. Run this script. The file open dialog will appear.
3. Locate and open the graphSearch.json file. Result page with clickable links 
will appear in your default browser.


"""
from tkinter.filedialog import askopenfilename
import json
import webbrowser
import os


filename = askopenfilename()
#File = open(filename, encoding = 'utf-8') #encoding = 'utf-8' parameter works most of the time
File = open(filename, errors = 'ignore') #Use this parameter if you get "UnicodeEncodeError: 'charmap' codec can't encode character.."
content = json.load(File)
File.close()
l = content['data'].get('result')
st = ''
lsorted  = sorted(l, key=lambda i: i['creation_time'],reverse = True)
for j in lsorted:
    link = 'https://www.facebook.com/'+ (j.get('actor')).get('id')+'/posts/' \
    + j.get('id')
    hlink = '<a href='+'"'+link+'"' + '>'+link+'</a>'    
    
    imageLink = j.get('image')
    
    if type(imageLink) == str:       
        imhLink = '<img src='+'"'+imageLink+'"' + '>'       
        st = st + hlink + '<br/>'+'<br/>' + imhLink + '<br/>'+'<br/>'
    else:
        st = st + hlink + '<br/>'+'<br/>'
        
    message = j.get('message')
    
    if type(message) == str:
        st = st + message+ '<br/>'+'<br/>'+'<br/>'
    #print (st)

msg = '<html><head></head><body><p>'+st+'</p></body></html>'

File = open('graphSearch.html', 'w')
File.write(msg)
File.close

#lines below change path according to file location
filename = 'file:///'+os.getcwd()+'/' + 'graphSearch.html'
webbrowser.open_new_tab(filename)
