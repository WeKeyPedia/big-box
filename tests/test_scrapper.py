from wekeypedzia.wikipedia_page import WikipediaPage

def test_fetch():
  page = WikipediaPage("unit testing")

  assert page.problem == None

def test_ambiguity():
  page = WikipediaPage("transformation")

  assert page.problem == "ambiguity"

def test_no_match():
  page = WikipediaPage("utin testgni")

  assert page.problem == "no match"

def test_links():
  page = WikipediaPage("unit testing")
  links = page.links()

  assert len(links) > 0