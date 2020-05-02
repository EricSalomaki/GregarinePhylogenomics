#!/usr/bin/env  python3.6

import sys
from Bio import SeqIO

fasta = SeqIO.parse(open(sys.argv[1]), 'fasta')

query_id =[]

for fa in fasta:
	name = fa.id
	name = name.strip(">")
	query_id.append(name)

unique = []
duplicates = []
for taxon in query_id:
	if taxon not in unique: 
		unique.append(taxon)
	else:
		duplicates.append(taxon)
		
while '' in duplicates: ### while there are '' in a string in list names
	duplicates.remove('') ### remove the ''

if not duplicates:
	pass
else:
	print(sys.argv[1])
	for dup in duplicates:
		print(dup)