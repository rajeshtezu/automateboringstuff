#! /usr/bin/python3

# Simply type a search term on the command line and computer automatically open a browser with all the top 
# search results in new tabs.

import requests, sys, bs4, webbrowser

if len(sys.argv) > 1:
    print('Googling...')
    res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
    res.raise_for_status()
    
    # TODO: Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text, 'html5lib')

    # TODO: Open a browser tab for each result.
    linkElems = soup.select('.r a')
    numOpen = min(5, len(linkElems))    # we will open max 5 top link
    for i in range(numOpen):
        webbrowser.open('http://google.com' + linkElems[i].get('href'))
        #print('http://google.com' + linkElems[i].get('href'))
else:
    sys.exit('Usage: python lucky.py <search string>')













