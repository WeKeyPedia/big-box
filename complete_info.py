# -*- coding: utf-8 -*-

from wekeypedia.importer.wkp_api import WeKeyApi

from wekeypedia.wikipedia_page import WikipediaPage as Page
from wekeypedia.wikipedia_page import url2title, url2lang

from multiprocessing.dummy import Pool as ThreadPool

api = WeKeyApi()

def get_page_info(url):
  print ""

	print url

	title = url2title(url)
	lang = url2lang(url) 

	print "[%s] %s" % (lang, title)

	wp = Page()
	r = wp.fetch_from_api_title(title, lang=lang)

	print "edits: %s" % (len(wp.get_all_editors()))

	print "langs: %s" % (len(wp.get_langlinks()))  

def main():
  pages = api.get_pages()

  pool = ThreadPool(8)


  for p in pages:
    pool.apply_async(get_page_info, args=(p["url"],))

  pool.close()
  pool.join()


main()