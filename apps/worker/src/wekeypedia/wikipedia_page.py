# -*- coding: utf-8 -*-
import sys

import wikipedia
import urllib

import requests

from colorama import Fore


def url2title(url):
  title = url.split("/")

  if(len(title) > 4):
    title = title[4]
    title = title.encode("ASCII")
    title = urllib.unquote(title).decode("utf8")
    title = title.replace("_", " ")
  else:
    title = title[3]

  return title

def url2lang(url):
  lang = url.split("/", 3)[2]
  lang = lang.split(".")[0]
  
  return lang

class WikipediaPage:
  def __init__(self, title=None):
    self.ready = False
    self.query = None
    self.page = None
    self.problem = None

    self.lang = "en"

    if (title):
      title = title.strip()

      r = self.fetch_from_title(title)

      if (r["problem"] != None):
        self.problem = r["problem"]
      else:
        self.page = r["page"]
        self.ready = True


  def fetch_from_title(self, title):
    response = { "page": None, "problem": None, }

    try:
      response["page"] = wikipedia.page(title)

      print "wikipedia page: %s" % response["page"].title.encode("utf8")
      print "\r"

    except wikipedia.exceptions.DisambiguationError:
      response["problem"] = "ambiguity"
      print Fore.YELLOW + "ambiguity"
    except wikipedia.exceptions.PageError:
      response["problem"] = "no match"
      print Fore.YELLOW + "no match"

    return response

  def fetch_from_api_title(self, title, opt_params={ "prop": "info", "inprop": "url" }, lang="en"):
    url = "http://%s.wikipedia.org/w/api.php" % (lang)

    params = {
      "format": "json",
      "action": "query",
      "titles": unicode(title)
      # "rvprop": "content",
      # "redirects": ""
    }

    params = dict(params.items() + opt_params.items())

    r = requests.get(url, params=params)
    # print r.json()

    pages = r.json()["query"]["pages"]

    self.page_id = pages.keys()[0]
    self.title = pages[ self.page_id ]["title"]
    self.lang = lang
    self.url = pages[ self.page_id ]["fullurl"]

    # print r.url
    # print r.text

    return r.json()

  def get_all_editors(self):
    url = "http://%s.wikipedia.org/w/api.php" % (self.lang)

    params = {
      "format": "json",
      "action": "query",
      "titles": self.title,
      "prop": "revisions",
      "rvprop": "user|userid|timestamp|size|ids|sha1",
      "rvlimit": "max",
      "redirects": "",
      "continue": ""
    }

    last = dict()
    revisions = []

    while True:
      current = params.copy()
      current.update(last)

      r = requests.get(url, params=current).json()

      pages = r["query"]["pages"]

      if ("revisions" in pages[ pages.keys()[0] ]):
        # print pages[ pages.keys()[0] ]["revisions"]
        revisions = revisions + pages[ pages.keys()[0] ]["revisions"]

      if 'continue' not in r: break

      last = r["continue"]

    return revisions

  def get_revisions(self, extra_params={}):
    url = "http://%s.wikipedia.org/w/api.php" % (self.lang)

    params = {
      "format": "json",
      "action": "query",
      "titles": self.title,
      "prop": "revisions",
      "rvprop": "user|userid|timestamp|size|ids|sha1|comment|content",
      "rvlimit": "max",
      "redirects": ""
      # ,
      # "continue": ""
    }

    params.update(extra_params)

    # print params

    revisions = []

    while True:
      r = requests.get(url, params=params).json()
      
      # print r
      pages = r["query"]["pages"]
      page = pages[ pages.keys()[0] ]

      revisions += page["revisions"]
      
      if "continue" in r:
        params.update(r["continue"])
      else:
        break

    return revisions

  def get_langlinks(self):
    langlinks = []

    url = "http://%s.wikipedia.org/w/api.php" % (self.lang)

    params = {
      "format": "json",
      "action": "query",
      "titles": self.title,
      "prop": "langlinks",
      "lllimit": 500
    }

    r = requests.get(url, params=params).json()

    # print r

    page = r["query"]["pages"][ r["query"]["pages"].keys()[0] ]

    if ("langlinks" in page):
      langlinks += page["langlinks"]

    return langlinks


  def links(self):
    links = []

    if (self.ready == True):
      links = self.page.links

    return links