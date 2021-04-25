# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:51:25 2021

@author: admin
"""
esp = [2200,2350,2000,2130,2190]

print(esp[1]-esp[0])
print(esp[0]+esp[1]+esp[2])
print(2000 in esp)
char = "false"
for i in range(4):
    if esp[i]==2000:
        char = "true"
print (char)
esp.append(1980)
print(esp[5])
esp[3]=esp[3]-200
print(esp[3])

heros=['spider man','thor','hulk','iron man','captain america']
heros.append('black panther')
print (heros)
heros.remove('black panther')
print (heros)
heros.insert(3, 'black panther')
print (heros)
heros[1:3]=['doctor strange']
print (heros)
heros.sort()
print (heros)

m =int(input())
odd = []
for i in range(m):
    if i%2 == 1:
        odd.append(i)

print (odd)