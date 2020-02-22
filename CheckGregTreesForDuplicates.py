import sys



treefile = sys.argv[1]


infile = open(treefile)
line = infile.read()
infile.close()
	
names = line.split('taxlabels')[1] ###split the infile on 'taxlabels' and keep the second split as the string called  names
names = names.split(';\nend;\n')[0] ### split the string 'names' on the ;\nend\n and keeps the first part as the string called names
names = names.split('\n') ###split the string names on hard returns looking like this - 'a\nb\nc\nd\n' into a list like this ['a', 'b', 'c', 'd']

dups = []
unique = []
taxalist = []

for name in names:
	if "[&!color=#ff0000]" in name: 
		pass
	else:
		taxalist.append(name)

renamed_taxon = [taxon.replace("Pseudo07", "Pseudo") for taxon in taxalist]
renamed_taxon = [taxon.replace("Pseudo08", "Pseudo") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Pseudo09", "Pseudo") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Poly1_total", "Poly") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Poly29", "Poly") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Poly39", "Poly") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Pycno19", "Pycno") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Pycno20", "Pycno") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Gyna25", "Gyna") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Gyna26", "Gyna") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Nauph77", "Nauph") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("HR1_total", "HissingRoach") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("HS2_total", "HissingRoach") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Cory88", "Cory") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Pseudosen96", "Pseudosen") for taxon in renamed_taxon]
renamed_taxon = [taxon.replace("Pseudosen97", "Pseudosen") for taxon in renamed_taxon]


#print(renamed_taxon)		
for taxon in renamed_taxon:
	
	taxon = taxon.strip("\t")		
	taxon = taxon.strip("'")		
	taxon = taxon.split("__")[0]
	if taxon not in unique: 
		unique.append(taxon)
	else:
		dups.append(taxon)
while '' in dups: ### while there are '' in a string in list names
	dups.remove('') ### remove the ''

if not dups:
	pass
else:
	print(sys.argv[1])
	for dup in dups:
		print(dup)	
	
#		name = name.strip("\t")
#		name = name.strip("'")
#		name = name.split("__")[0]
#