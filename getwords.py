import urllib2
from bs4 import BeautifulSoup
import re
from collections import Counter
import unicodedata


def get_common_words(url,N=100) :
    resp = urllib2.urlopen(url)
    html = resp.read()
    raw = BeautifulSoup(html).get_text() #is unicode
    raw = ''.join([c for c in raw if unicodedata.category(c) != 'Po'])

    words = raw.split(" ")
    freqs = Counter(words)
    return dict(freqs.most_common(N))
