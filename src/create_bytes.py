#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

How to create a bytes object in Python?

¿Cómo se define un objeto bytes en Python?
'''

#bytes is a sequence of small integers, in the range 0 through 255, print as
#ASCII characters when displayed.
#enclosed in single and double quotes
b = b'Bytes objects are immutable sequences of single bytes'
print(b)

#triple single or double quotes allows multiple lines
b = b'''first line text,
second line text,
third line text.'''
print(b)

#created from a iterable of ints, string, bytes or buffer objects.
b = bytes('canción, moño', 'utf8')
print(b)
