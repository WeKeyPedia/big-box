from wekeypedia.importer.wkp_api import WeKeyApi as api

from wekeypedia.wikipedia_page import url2title
from wekeypedia.wikipedia_page import url2lang

def test_api_pages():
	a = api()

	assert len(a.get_pages()) > 0

def test_fn_url2title():
	url = "http://en.wikipedia.org/wiki/Ant"

	assert url2title(url) == "Ant"

def test_fn_url2title_when_user():
	url = "http://en.wikipedia.org/User:Taniki"

	assert url2title(url) == "User:Taniki"

def test_fn_url2lang():
	url = "http://en.wikipedia.org/User:Taniki"

	assert url2lang(url) == "en"