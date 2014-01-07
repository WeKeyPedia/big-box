from wekeypedzia.wikipedia_page import WikipediaPage

import networkx as nx

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

class WikipediaNetwork:
  def __init__(self, keywords):
    self.keywords = keywords
    self.graph = nx.Graph()

  def get_page_links(self, title):
    w = WikipediaPage(title)
    return w.links()

  def method(self, r):
    concept  = r[0]
    links = r[1]

    print "## %s" % concept

    self.graph.add_node(concept)

    accepted_links = set(links) & set(self.keywords)

    for link in accepted_links:
      print "-> %s" % link
      self.graph.add_edge(concept, link)

    print "\r"

  def build(self):
    pool = ThreadPool(8)

    for kw in self.keywords:
      pool.apply_async(lambda kw: (kw, self.get_page_links(kw)), (kw, ), callback=self.method)

    pool.close()
    pool.join()