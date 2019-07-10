from bs4 import BeautifulSoup


r = '<div class="txt-block"><h4 class="inline">Runtime:</h4><time itemprop="duration" datetime="PT142M">142 min</time></div>'

#rr= '<div class="subtext"><meta itemprop="contentRating" content="R">R<span class="ghost">|</span><time itemprop="duration" datetime="PT142M">2h 22min</time><span class="ghost">|</span><a href="/genre/Crime?ref_=tt_ov_inf"><span class="itemprop" itemprop="genre">Crime</span></a>, <a href="/genre/Drama?ref_=tt_ov_inf"><span class="itemprop" itemprop="genre">Drama</span></a><span class="ghost">|</span><a href="/title/tt0111161/releaseinfo?ref_=tt_ov_inf" title="See more release dates">14 October 1994 (USA)<meta itemprop="datePublished" content="1994-10-14"></a>            </div>'

soup = BeautifulSoup(r)

#name = soup.find("div", {"class":"inline"}).text

a = name = soup.find("div", {"class":"txt-block"}).find(itemprop="duration").text

print(name)

# import tweepy 
# import json
# import csv
# import sys


# consumer_key = 'dqFXbqLXD6Rm7fzoYh6Ra3Zos'
# consumer_secret = 'yJv27ak1nXck4pXIMZkBe0fVa8x800426PeciLXEWOtrG9wAXX'
# access_token = '957474764-WRlLbe6j0h93JA6jfZ5d1cPPeEdSEqvNQzUoOwtI'
# access_token_secret = 'sR9b576wXlmh7wgUR3oUvfApsz7aegdDwG9KHVpt60py1'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# usr = api.get_user('mataralhawiti').screen_name

# #print(usr)

# fav = api.favorites(usr,1)

# for f in fav:
# 	print(f.text)
# 	print('--------------------')




# 	--


# 	PATH=/home/matar/anaconda2/bin to PATH in /home/matar/.bashrc
# A backup will be made to: /home/matar/.bashrc-anaconda2.bak




# https://rstudio-pubs-static.s3.amazonaws.com/118060_fcdc77aa7ffb452bb4cc8b67021d973a.html