from rake_nltk import Rake

f = open("abstract.txt",'r')

text = f.read()

s = ""

list = text.split('.')

phrases = ['in this paper','in this ','in this study','our research','this paper proposes','this novel','this paper','this paper aimed','we describe','this article',
'this article extends','this work examined','the present study','we present','the objective of this paper','we examine','this paper surveys','this paper conducted',
'this paper presents','we develop a novel approach','we develop','in this paper,we have proposed','this paper describe','in this domain']

selected = []
for line in list:
	for phrase in phrases:
		lower = line.lower()
		index = lower.find(phrase)
		if index != -1:

			selected.append(line)
for i in selected:
	s = s+i+". "
text = s


r=Rake()
r.extract_keywords_from_text(text)

list = (r.get_ranked_phrases())
astext = ""
for items in list:
	astext = astext + items +". "

print(astext)
