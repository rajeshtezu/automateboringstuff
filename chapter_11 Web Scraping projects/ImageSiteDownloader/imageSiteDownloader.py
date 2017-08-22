#! /usr/bin/python3

'''
A program that goes to a photo-sharing site Flickr, searches for a category of photos, and then downloads all 
the resulting images.
'''

import requests, bs4
import sys, os

url = 'https://www.flickr.com/search/?text='

if len(sys.argv) < 2:
	sys.exit('Usage: python imageSiteDownloader.py <search item>')

else:
	searchItem = sys.argv[1] 
	os.makedirs(searchItem, exist_ok=True)

	url += searchItem
	res = requests.get(url)
	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text, 'html5lib')
	imageElem = soup.select('.photo-list-photo-view')
	#print(len(imageElem))

	# Find image Urls and download all images
	for i in range(min(10,len(imageElem))):
		# Get Urls
		imageUrl = (imageElem[i].attrs)['style']
		imageUrl = (imageUrl.split(';')[-1]).split(':')[1]
		imageUrl = imageUrl.split('(')
		imageUrl = imageUrl[1].split(')')[0]
		imageUrl = 'http:' + imageUrl
		#print(imageUrl)

		try:
			res = requests.get(imageUrl)
			res.raise_for_status()
		except:
			continue
		# save the image to folder searchItem
		imageFile = open(os.path.join(searchItem, os.path.basename(imageUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()



















