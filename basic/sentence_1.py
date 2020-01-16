import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        # include '...' in a long sentence, except the start and end words.
        return 'Sentence(%s)' % reprlib.repr(self.text)


ex = "The world is beautiful. It's a nice day"
s = Sentence(ex)
#print(list(s))
#print(s)
#print(s[1])

# check if it's iterable
#print(iter(s))
#from collections import abc
#print(issubclass(Sentence, abc.Iterable))
it = iter(s)
#print(list(it))
#it.__next__()
next(it)
print(list(it))
