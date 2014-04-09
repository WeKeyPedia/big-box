from wekeypedia.wikipedia_network import WikipediaNetwork

concepts = [
  "Artificial neural network",
  "Biological network",
  "Business networking",
  "Computer network",
  "Electrical network",
  "Neural network",
  "Radio network",
  "Social network",
  "Telecommunications network",
  "Television network",
  "Universities network",
  "Universities network, 10",
]

def test_cross_references():
  wkn = WikipediaNetwork(concepts)
  wkn.build()

  assert len(wkn.graph.nodes()) > 0