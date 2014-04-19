# -*- coding: utf-8 -*-
import os

import json

from wekeypedia.wikipedia_page import WikipediaPage as Page, url2title, url2lang

from colorama import init
from colorama import Fore, Back, Style

from multiprocessing.dummy import Pool as ThreadPool

users = {}

init()

extra_languages = [ "en", "simple", "uk", "fr", "ru", "de" ]

source_in = "data/in/wicrimea-seeds.txt"
source_ext = "data/out/wicrimea-seeds.extended.txt"

out = open(source_ext, "w")

with open(source_in, "r") as file:
  for l in file:
    p = Page()
    r = p.fetch_from_api_title(url2title(l.strip()))

    print ""
    print u"→ %s (%s)" % (p.title, l.strip())

    langs = p.get_langlinks()

    for l in langs:
      if l["lang"] in extra_languages:
#        print l

        p_lang = Page()
        p_lang.fetch_from_api_title(l["*"], lang=l["lang"])

        print u"   → [%s] %s (%s)" % (l["lang"], p_lang.title, p_lang.url)
        out.write(p_lang.url+"\n")

out.close()

def write_revision(rev_id, file):
  rev_with_content = p.get_revisions(extra_params={ "rvstartid": rev_id, "rvlimit" : 1})

  with open(file, "w") as f:
    json.dump(rev_with_content, f)

with open(source_ext, "r") as file:
  for l in file:
    lang = url2lang(l)
    p = Page()
    r = p.fetch_from_api_title(url2title(l.strip()), lang=lang)

    print ""
    print u"📖  [%s] %s" % (lang, p.title)

    revisions = p.get_all_editors()
    revisions_downloaded = 0

    # print revisions[0:10]

    print u"  🔨  revisions: %s" % (len(revisions))

    # revs = p.get_revisions(extra_params={ "rvstartid": revisions[0]["revid"], "rvendid": revisions[-1]["revid"] })

    revisions_dir = "data/out/%s/%s-%s/revisions" % (lang, p.page_id, p.title)

    if not os.path.exists(revisions_dir):
      os.makedirs(revisions_dir)

    pool = ThreadPool(8)

    for revision in revisions:
      rev_id = revision["revid"]

      file = "%s/%s.json" % (revisions_dir, rev_id)
      if not os.path.isfile(file):
        r = pool.apply_async( write_revision, args=(rev_id, file,) )
        # r.get()
        revisions_downloaded += 1

    pool.close()
    pool.join()

    print u"  📥  downloaded revisions: %s" % (revisions_downloaded)

    unique_editors = set()
    hidden_users = 0

    for r in revisions:
      if "user" in r:
        unique_editors.add(r["user"])
      else:
        if "userhidden" in r:
          hidden_users += 1
        else:
          print r
          print r["user"]

    users[lang] = unique_editors

    print u"  😀  unique editors: %s" % (len(unique_editors))
    print u"  👻  hidden users: %s" % (hidden_users)

print "users: %s" % (len(users))