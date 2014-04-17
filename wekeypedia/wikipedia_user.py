# -*- coding: utf-8 -*-

import requests

class WikipediaUser:
  def __init__(self, lang="en", name=None):
    self.lang = lang
    self.name = name

  def fetch_contribs(self):
    url = "http://%s.wikipedia.org/w/api.php" % (self.lang)

    contribs = []

    params = {
      "action":"query",
      "format": "json",
      "list":"usercontribs",
      "ucuser": self.name,
      "uclimit": "500",
      "continue": ""
    }

    while True:
      r = requests.get(url, params=params).json()
      contribs += r["query"]["usercontribs"]

      if "continue" in r:
#        print r["continue"]
        params.update(r["continue"])
      else:
        break

    return contribs