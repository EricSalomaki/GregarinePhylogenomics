import os
import sys
import glob
import pickle

files = [fname for fname in glob.glob('*.fasta')]
print files

status_d = {}

for fname in files:
    infile = open(fname)
    line = infile.read()
    infile.close()
    seqs = line.split('>')[1:]
    if 'clean' in fname:
        stat = 'clean'
    else:
        stat = 'deleted'
    for seq in seqs:
        name = seq.split('\n')[0]
        name = name.replace('.', '_')
        status_d[name] = stat

pickle.dump(status_d, open('status.bin','wb'))
print(status_d)
