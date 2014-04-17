# -*- coding: utf-8 -*-
import os

from wekeypedia.importer.wkp_api import WeKeyApi

from wekeypedia.wikipedia_page import WikipediaPage as Page
from wekeypedia.wikipedia_page import url2title, url2lang

from multiprocessing.dummy import Pool as ThreadPool

import json

api = WeKeyApi()

def get_page_info(url, length, index):
 #  print ""

	# print url

	title = url2title(url)
	lang = url2lang(url) 

	print "[%s] %s (%s/%s)" % (lang, title, index, length)

	wp = Page()

#	print wp

	r = wp.fetch_from_api_title(title, lang=lang)

#	print r

	data = {
		"edits": wp.get_all_editors(),
		"langs": wp.get_langlinks()
	}

#	print data

	file = "dataset/%s.info.json" % (wp.page_id)
#	print file

	with open(file, "w") as out:
		json.dump(data, out)

	# print "edits: %s" % (len(wp.get_all_editors()))
	# print "langs: %s" % (len(wp.get_langlinks()))  

def main():
	print "create initial dataset directory: [./dataset]"

	directory = "dataset"

	if not os.path.exists(directory):
		os.makedirs(directory)

	pages = []

	pages = api.get_pages()
	# pages = pages[0:50]

	pool = ThreadPool(8)

	l = len(pages)
	i = 0

	for p in pages:
		x = pool.apply_async(get_page_info, args=(p["url"], l, i, ))
		x.get()
		i = i + 1

	pool.close()
	pool.join()

main()