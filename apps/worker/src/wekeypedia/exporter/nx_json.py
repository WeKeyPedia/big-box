import json

import networkx as nx
from networkx.readwrite import json_graph

class NetworkxJson:
  def __init__(self, graph):
    self.graph = graph

  def nx_export(self, export_type, output_file):
    data = getattr(json_graph, "%s_data" % export_type)(self.graph)

    target = open(output_file, "w")
    json.dump(data,target, sort_keys=True, indent=2)
    print "export node-link: %s" % output_file