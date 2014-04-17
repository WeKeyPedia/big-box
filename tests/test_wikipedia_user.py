from wekeypedia.wikipedia_user import WikipediaUser as User

def test_wikipedia_user_fetch_contributions():
  u = User(name="taniki")

  contribs = u.fetch_contribs()

  assert len(contribs) > 0