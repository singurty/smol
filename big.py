#!/usr/bin/env python3
import struct

dictionary = []
df = open('dict', 'rb')
"""
structure of the dictionary looks like:
length of the word +
the word
"""
data = df.read(65536)
print('length of data: {}'.format(len(data)))
while len(data) != 0:
    i = 0
    while i < len(data):
#        print('starting at {}'.format(i))
        length = struct.unpack('<H', data[i:i+2])[0]
        i += 2
        word = struct.unpack(str(length) + "s", data[i:i+length])[0].decode()
        i += length
#        print('adding {}'.format(word))
        dictionary.append(word)
    data = df.read(65536)
df.close()
#print(dictionary)
print('found {} words'.format(len(dictionary)))

"""
structure of smolled looks like:
index
"""
cf = open('smolled', 'rb')
xf = open('xed', 'w')
data = cf.read(65536)
j = 0
while len(data) != 0:
    i = 0
    print('read {} bytes'.format(len(data)))
    while i < len(data):
#        print('starting at {}'.format(i))
        index = struct.unpack('<H', data[i:i+2])[0]
        i += 2
        word = dictionary[index]
#        print('found word {}'.format(word))
        xf.write(word)
        j += 1
    data = cf.read(65536)
print('extracted {} words'.format(j))
cf.close()
xf.close()
