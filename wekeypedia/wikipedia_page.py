# -*- coding: utf-8 -*-
import sys

import wikipedia
import urllib

from colorama import Fore


def url2title(url):
  title = url.split("/")

  if(len(title) > 4):
    title = title[4]
    title = title.replace("_", " ")
    title = urllib.unquote(title) #.decode("utf8")
    #title = title.encode("utf-8")
  else:
    title = title[3]

  return title

def url2lang(url):
  lang = url.split("/", 3)[2]
  lang = lang.split(".")[0]
  
  return lang

class WikipediaPage:
  def __init__(self, title):
    self.ready = False
    self.query = None
    self.page = None
    self.problem = None

    title = title.strip()

    try:
      self.page = wikipedia.page(title)
      self.ready = True

      print "wikipedia page: %s" % self.page.title.encode("utf8")
      print "\r"

    except wikipedia.exceptions.DisambiguationError:
      self.problem = "ambiguity"
      print Fore.YELLOW + "ambiguity"
    except wikipedia.exceptions.PageError:
      self.problem = "no match"
      print Fore.YELLOW + "no match"

  def parse_url(self):
    title = url2title(self.page.url)

  def links(self):
    links = []

    if (self.ready == True):
      links = self.page.links

    return links