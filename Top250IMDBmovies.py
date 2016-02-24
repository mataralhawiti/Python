#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
To-do :
# scrape Top250 list from IMDB using Requests&BS4 modules
# Store the data in MongoDB
# use pymongo module to mainpulate data
# use Pandas, NumPy to analyze & plot data
# use IPython
'''

__author__ = 'Matar'
import sys
import os
import re
import datetime
import requests
from bs4 import BeautifulSoup
import pymongo

top_movies_list_url = 'http://www.imdb.com/chart/top'
main_url = 'http://www.imdb.com'
movie_url = main_url+'/title/'
#movies_list = []

def make_request(url) :
	""" get top 250 movies list

	:parm url: main url for 
	:return: conent object
	"""
	try :
		r = requests.get(url)
	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit(1)

	return r.content



def get_movies_titleid(content) :
	""" exampl : tt0072684 

	:parm content: calling make_request()
	:return: a list that contains movies titles
	"""
	# make soup
	soup = BeautifulSoup(content, "lxml")
	titles = soup.find_all("div")

	titles_list = []

	for title in titles :
		if title.has_attr('data-titleid') : # check it div tag has att called "data-titleid"
			titles_list.append(title.get("data-titleid"))

	return titles_list


def get_movies_link(movies_titleid):
	""" get list of the full link for the movie page
		exampl : http://www.imdb.com/title/tt0072684

		:parm movies_titleid : list of all movies title id="titleYear
		return: list of movies links
	"""

	movies_links = []

	for movie in movies_titleid :
		movies_links.append(movie_url+movie)

	return movies_links

def get_movie_name(links_list):

	names = []

	for link in links_list :
		r = make_request(link)
		soup = BeautifulSoup(r, "lxml")
		name = soup.find_all("h1", {"itemprop":"name"})
		for n in name:
			names.append(n.text.encode('utf-8'))

	return names

def main():
	r = make_request(top_movies_list_url)
	mov_titls = get_movies_titleid(r)
	lks = get_movies_link(mov_titls)
	nms = get_movie_name(lks)

	# print movies links
	for i in nms :
		print(i)

if __name__ == "__main__" :
	main()

"""


#print(title.get("data-titleid"))
#movie_url+title.get("data-titleid")
#movies_list.append(movie_url+title.get("data-titleid"))

# rk = soup.find_all("span", {"name":"rk"})


def get_movies_url(titles) :
	for title in titles :
		if title.has_attr('data-titleid') :
			movies_list.append(movie_url+title.get("data-titleid"))
	return movies_list


def get_movie_detls(mov_lst) :
	mov_lst = get_movies_url(titles)

	for mov in mov_lst :
		r = requests.get(mov)
		mov_tilt = soup.find("h1", {"itemprop","name"}).text
		break



#m = requests.get('http://www.imdb.com/title/tt0111161/')
#soup = BeautifulSoup(m.content, "lxml")
#mov_tilt = soup.find_all("div", {"class","title_wrapper"})
#mov_tilt = soup.find_all("h1", {"itemprop":"name"})

#div class="title_wrapper"

#print(mov_tilt)
#print(len(mov_tilt))

#for i in mov_tilt :
	#print(i.text.encode('utf-8'))

ur = []
w = 1
def get_movies_url1(movies_list) :
	for mv in movies_list :
		m = requests.get(movie_url+mv)
		s = BeautifulSoup(m.content, "lxml")
		d = s.find_all("h1", {"itemprop":"name"})
		for i in d :
			a = i.text.encode('utf-8')
			a = a[:-9]
			ur.append(a)

		#print(d.text.encode('utf-8'))

get_movies_url1(movies_list)


for i in ur :
	print(i)
	#return movies_list



#<h1 itemprop="name" class="">The Shawshank Redemption&nbsp;<span id="titleYear">(<a href="/year/1994/?ref_=tt_ov_inf">1994</a>)</span>            </h1>

# ranking
# for movie in movies_list :
# 	print(movies_list.index(movie), movie)

# for r in rk:
# 	if r.has_attr("data-value") :
# 		print(r.get("data-value"))










#titles = soup.find_all("div", {"class":"data-titleid"})
#titles = soup.find_all("data-titleid")
#titles = soup.find_all("div").attrs
#for title in titles :
	#print(title)

#titles = soup.div
# i = 0
# for title in titles :
# 	a = title.get("data-titleid")
# 	if a is not None :
# 		print(a)
# print(i)

# for title in titles :
# 	if title.has_attr('data-titleid') :
# 		print(title.get("data-titleid"))





#titles = soup.div['class']

#titles = soup.div
#print(titles)


#print(titles.attrs['data-titleid'])
#attrs['data-lat']


'''
ur = []
w = 1
def get_movies_url1(movies_list) :
	for mv in movies_list :
		m = requests.get(movie_url+mv)
		s = BeautifulSoup(m.content, "lxml")
		d = s.find_all("h1", {"itemprop":"name"})
		for i in d :
			a = i.text.encode('utf-8')
			a = a[:-9]
			ur.append(a)

		#print(d.text.encode('utf-8'))

get_movies_url1(movies_list)


for i in ur :
	print(i)
	'''

"""