# -*- coding: utf-8 -*-

import requests

class WikipediaUser:
  def __init__(self, lang="en", name=None):
    self.lang = lang
    self.name = name

  def fetch_contribs(self):
    url = "http://%s.wikipedia.org/w/api.php" % (self.lang)

    params = {
      "action":"query",
      "format": "json",
      "list":"usercontribs",
      "ucuser": self.name,
      "uclimit": "5000"
    }

    r = requests.get(url, params=params).json()

    return r["query"]["usercontribs"]