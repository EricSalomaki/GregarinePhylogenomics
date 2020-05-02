#!/usr/bin/env  python3.6

import sys
from Bio import SeqIO

fasta = SeqIO.parse(open(sys.argv[1]), 'fasta')

query_id =[]

for fa in fasta:
	name = fa.id
	query_id.append(name)

renamed = [query.replace("Pseudo07", "Pseudo") for query in query_id]
renamed = [query.replace("Pseudo08", "Pseudo") for query in renamed]
renamed = [query.replace("Pseudo09", "Pseudo") for query in renamed]
renamed = [query.replace("Poly1_total", "Poly") for query in renamed]
renamed = [query.replace("Poly29", "Poly") for query in renamed]
renamed = [query.replace("Poly39", "Poly") for query in renamed]
renamed = [query.replace("Pycno19", "Pycno") for query in renamed]
renamed = [query.replace("Pycno20", "Pycno") for query in renamed]
renamed = [query.replace("Gyna25", "Gyna") for query in renamed]
renamed = [query.replace("Gyna26", "Gyna") for query in renamed]
renamed = [query.replace("Nauph75", "Nauph") for query in renamed]
renamed = [query.replace("Nauph77", "Nauph") for query in renamed]
renamed = [query.replace("Nauph80", "Nauph") for query in renamed]
renamed = [query.replace("HR1_total", "HissingRoach") for query in renamed]
renamed = [query.replace("HS2_total", "HissingRoach") for query in renamed]
renamed = [query.replace("HS2_sc", "HissingRoach") for query in renamed]
renamed = [query.replace("Cory88", "Cory") for query in renamed]
renamed = [query.replace("Pseudosen96", "Pseudosen") for query in renamed]
renamed = [query.replace("Pseudosen97", "Pseudosen") for query in renamed]

sep = "__"

l = [x for x in renamed if sep in x]

new_list = []

for item in l:
	rest = item.split(sep,1)[0]
	new_list.append(rest)

unique = []
duplicates = []
for taxon in new_list:
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
