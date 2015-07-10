import urllib2
from bs4 import BeautifulSoup
import re
from collections import Counter


def get_common_words(url,N=100) :
	resp = urllib2.urlopen(url)
	html = resp.read()
	raw = BeautifulSoup(html).get_text() #is unicode

	words = re.findall(ur'\w+',raw,re.UNICODE)
	freqs = Counter(words)
	return dict(freqs.most_common(N))





