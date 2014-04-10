# -*- coding: utf-8 -*-
import sys

import wikipedia

from colorama import Fore

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

  def links(self):
    links = []

    if (self.ready == True):
      links = self.page.links

    return links