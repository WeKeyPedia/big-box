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

  def fetch_from_api_title(self, title, opt_params={ "prop": "info" }, lang="en"):
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

    # print r.url
    # print r.text

    return r.json()

  def links(self):
    links = []

    if (self.ready == True):
      links = self.page.links

    return links