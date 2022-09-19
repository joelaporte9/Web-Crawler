from urllib.request import urlopen
from bs4 import BeautifulSoup
import re



# urls to read 

file = urlopen("http://citelms.net/Internships/Summer_2018/Fan_Site/index.html")

# pase the HTML on the index page

soup = BeautifulSoup(file, features="html.parser")
rootSite = "http://citelms.net/Internships/Summer_2018/Fan_Site/"

#start the crawl
def crawl():
    linksQueue = []
    visitedUrls = []
    links = []

    #Searches the index page for all a tags with an href, appends the hrefs to the link variable 

    for link in soup.findAll('a', attrs={'href': re.compile(".html$")}):
        links.append(link.get('href'))

        #Extracts just the name of the HTML page. i.e "Index.html"

        cleanMatch = re.findall('"([^"]*)"', str(link))
        print(f'Crawling: {cleanMatch}')

        #create the Links Queueu and visited queue

        if link not in visitedUrls and link not in linksQueue:
            linksQueue.append(link)
        else:
            visitedUrls.append(link)
    while len(linksQueue):
        visitedUrls.append(linksQueue.pop(0))
    print("VISITED LINKS")
    print(str(visitedUrls) + '\n')

# start search 

def search(rootSite):
    searchWord = input("Search for a link!: ")
    myDict = {'name': ["index.html", 'programs.html', 'faculty.html', 'gallery.html', 'events.html', 'thetathon.html',
    'graphicstutorial.html', 'codingtutorials.html'] }
    
    #searches for the values searched for in the dictionary 

    for key, value in myDict.items():
        for v in value:
            if searchWord in v:
                url = rootSite + v 
                print(f'found {url}')

crawl()
search(rootSite)
