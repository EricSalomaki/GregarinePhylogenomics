import os
import sys
import glob
from Bio import Phylo

files = [fname for fname in glob.glob('RAxML_bipartitions.*.tre')]
print(files)
for fname in files:
    Phylo.convert("%s" % (fname), "newick", "%s.nexus" % (fname), "nexus")

