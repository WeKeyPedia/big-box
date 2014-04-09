from __future__ import absolute_import

import sys

from wekeypedia.wikipedia_network import WikipediaNetwork
from wekeypedia.exporter.nx_json import NetworkxJson
from wekeypedia.exporter.mapping import Mapping

def parse_source_line(line):
  concept = line

  if len(concept.split(",")) > 1:
    split = concept.split(",")

    concept = split[0]

    try:
      int(split[1])
    except:
      concept = concept +", "+split[1]

  concept = concept.strip()

  return concept

def open_source_list(da_source):
  da_list = []

  da_list = map(parse_source_line, open(da_source, "r"))

  return da_list

def store_mapping(mapping):
  m = Mapping(mapping)
  m.csv("%s.mapping.csv" % (sys.argv[1]))

def get_wikipedia_network_structure(concepts):

  wkn = WikipediaNetwork(concepts)
 
  wkn.build()

  store_mapping(wkn.mapping)

  return wkn.graph

if len(sys.argv) > 1:
  source = sys.argv[1]

  concepts = open_source_list(source)
  graph = get_wikipedia_network_structure(concepts)

  for export_type in ["node_link", "adjacency"]:
    target_name = "%s.%s.json" % (source, export_type)

    exporter = NetworkxJson(graph)
    exporter.nx_export(export_type, target_name)