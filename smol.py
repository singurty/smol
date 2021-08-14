#! /usr/bin/env python3
import struct
import re

f = open('enwik9l')

data = f.read(65536)
dictionary = []
while data != '':
    data = f.read(65536)
    words = re.split('([\s.,;()]+)', data)
    for item in words:
        try:
            dictionary.index(item)
        except ValueError:
            dictionary.append(item)
print("built {} words dictionary".format(len(dictionary)))

df = open('dict', 'wb')
short = True
"""
structure of the dictionary looks like:
are the indices short? +
length of the word +
the word
"""
if len(dictionary) > 65537:
    short = False
    df.write(struct.pack('<?', short))
else:
    df.write(struct.pack('<?', short))
for i in range(len(dictionary)):
    # assume that the length of word will fit into a short
    df.write(struct.pack('<H', len(dictionary[i].encode())))
    df.write(struct.pack(str(len(dictionary[i].encode())) + "s", dictionary[i].encode()))
    if short:
        df.write(struct.pack('<H', 0))
    else:
        df.write(struct.pack('<I', 0))
df.close()

cf = open('smolled', 'wb')
f.seek(0)
data = f.read(65536)
while data != '':
    data = f.read(65536)
    words = re.split('([\s.,;()]+)', data)
    for item in words:
        index = dictionary.index(item)
        if short:
            cf.write(struct.pack('<H', index))
        else:
            cf.write(struct.pack('<I', index))
cf.close()
