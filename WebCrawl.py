from urllib.request import urlopen
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
import re

# Sets up the GUI
gui = Tk()
gui.geometry("1400x400")

# Output text boxes for the visted pages and the page yous earch for 
outputLinks = Text(gui,height=20, width=80)
outputLinks.grid(column=1,row=1)
outputSearch = Text(gui, height=20, width=80)
outputSearch.grid(column=2, row=1)

tk.Label(gui, text="VISITED LINKS").grid(row=0, column=1)

# Enter the link to search for and place it on the GUI
# Also adds a title to the search box 
searchWord = tk.Entry(gui, width=50)
searchWord.grid(row=0, column=2)
searchWord.insert(0, "Search for a link! ex: gallery")

# Revoves the search title when the search box is clicked in
def some_callback(event): 
    searchWord.delete(0, "end")
    return None
searchWord.bind("<Button-1>", some_callback)

# Buttons to crawl the page and search the page 
tk.Button(gui, 
        text='Crawl page',height=5, width=10, command=lambda: crawl()).grid(row=1, column=0, 
        sticky=tk.W, pady=4)
tk.Button(gui, 
        text='Search',height=1, width=10, command=lambda: search()).grid(row=0, column=3, 
        sticky=tk.W, pady=4)
        
# Index url that is crawled and parsed. 
# Rootsite variable to concat the link with the .html link searched for
file = urlopen("http://citelms.net/Internships/Summer_2018/Fan_Site/index.html")
soup = BeautifulSoup(file, features="html.parser")
rootSite = "http://citelms.net/Internships/Summer_2018/Fan_Site/"

# Starts the crawl
def crawl():
    # Define variables for lists
    linksQueue = []
    visitedUrls = []
    links = []
    # Searches the index page for all a tags with an href, appends the hrefs that end in .html to the link variable 
    for link in soup.findAll('a', attrs={'href': re.compile(".html$")}):
        links.append(link.get('href'))
        # Extracts just the name of the HTML page. i.e "Index.html"
        cleanMatch = re.findall('"([^"]*)"', str(link))
        # Create the links queue and visited queue
        if cleanMatch not in visitedUrls and cleanMatch not in linksQueue:
            linksQueue.append(cleanMatch)
        else:
            visitedUrls.append(cleanMatch)
    # Checks to see if the links queue is empty or not
    # Removes the links from the links queue and adds them to the visited queue
    # LIFO approach 
    while len(linksQueue):
        visitedUrls.append(linksQueue.pop(0))
    outputLinks.insert(1.0, '\n'.join(map(str, visitedUrls)))

# Starts the search 
def search():
    # Gets the word enterd in the Entry box
    word = searchWord.get()
    # Dictionary 
    dictionary = {'name': ['index.html', 'programs.html', 'faculty.html', 'gallery.html', 'events.html', 'thetathon.html',
    'graphicstutorial.html', 'codingtutorials.html'] }
    # Loops through the dictionary to find the items in it
    for key, value in dictionary.items():
        # Starts a loop for the values to be searched
        for v in value:
            # If the word is in the dictionary, get it
            # Casefod() handles case sensitivity for the input
            if word.casefold() in v:
                url = rootSite + v 
                outputSearch.insert(1.0, url)

gui.mainloop()






