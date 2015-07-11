import urllib2
from bs4 import BeautifulSoup
import re
from collections import Counter
import unicodedata


def get_common_words(url,N=100) :
    resp = urllib2.urlopen(url)
    html = resp.read()
    raw = BeautifulSoup(html).get_text() #is unicode

    # only use characters in the "Letter" and "Spacing" categories
    valid_prefixes = ["L", "Z"]
    raw = ''.join([c for c in raw
                   if unicodedata.category(c)[0] in valid_prefixes])


    words = [w for w in raw.split(" ") if len(w) > 0]
    freqs = Counter(words)
    return dict(freqs.most_common(N))
