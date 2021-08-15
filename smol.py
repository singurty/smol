#!/usr/bin/env python3
import struct
import re

f = open('enwik9l')

dictionary = []
data = f.read(65536)
i = 0
while data != '':
    words = re.split('([\s.,;()]+)', data)
    for item in words:
        i += 1
        try:
            dictionary.index(item)
        except ValueError:
            dictionary.append(item)
    data = f.read(65536)
print('found {} words'.format(i))
print("built {} words dictionary".format(len(dictionary)))

df = open('dict', 'wb')
"""
structure of the dictionary looks like:
length of the word +
the word
"""
i = 0
for word in dictionary:
    # assume that the length of word will fit into a short
    df.write(struct.pack('<H', len(word.encode())))
    df.write(struct.pack(str(len(word.encode())) + "s", dictionary[i].encode()))
    i += 1
print('wrote {} entries'.format(i))
df.close()

cf = open('smolled', 'wb')
f.seek(0)
data = f.read(65536)
while data != '':
    data = f.read(65536)
    words = re.split('([\s.,;()]+)', data)
    for item in words:
        index = dictionary.index(item)
        cf.write(struct.pack('<H', index))
cf.close()
