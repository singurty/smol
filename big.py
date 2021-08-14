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
while len(data) != 0:
    i = 0
    while i < len(data):
        length = struct.unpack('<H', data[i:i+2])[0]
        word = struct.unpack(str(length) + "s", data[i:i+length])
        dictionary[index] = word
print(dictionary)
