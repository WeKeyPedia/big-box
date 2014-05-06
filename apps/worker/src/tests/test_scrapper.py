from wekeypedia.wikipedia_page import WikipediaPage

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

def test_direct_api():
  page = WikipediaPage()

  r = page.fetch_from_api_title("unit testing")

  print r

  assert "-1" not in r["query"]["pages"]

def test_direct_api_no_match():
  page = WikipediaPage()

  r = page.fetch_from_api_title("bleepbloopzerg")

  print r

  assert "-1" in r["query"]["pages"]

def test_api_revisions_without_content():
  page = WikipediaPage()
  r = page.fetch_from_api_title("Taran Killam")
  revisions = page.get_all_editors()

  assert len(revisions) > 500

def test_api_get_specific_revision():
  page = WikipediaPage()
  r = page.fetch_from_api_title("Taran Killam")
  revisions = page.get_all_editors()

  revision = page.get_revisions(extra_params={ "rvstartid": revisions[0]["revid"], "rvlimit" : 1})

  print revision

  assert len(revision) > 0

def test_api_get_revisions_with_continue():
  page = WikipediaPage()
  r = page.fetch_from_api_title("Taran Killam")
  revisions = page.get_all_editors()

  revision = page.get_revisions(extra_params={ "rvstartid": revisions[0]["revid"], "rvlimit" : 500, "continue": ""})

  print revision

  assert len(revision) > 500

def test_api_langlinks():
  page = WikipediaPage()
  r = page.fetch_from_api_title("Jeu de go", lang="fr")
  langlinks = page.get_langlinks()

  print langlinks

  assert len(langlinks) > 10