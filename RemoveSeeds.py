import os
import sys
import glob

alignment = sys.argv[1]
outfile = sys.argv[2]

infile = open(alignment)
line = infile.read()
infile.close()

names = line.split("\n")

delete = []

while '' in names:
	names.remove('')
for name in names: 
	if name.count('XP_') != 0 : ### If the header count contains XP_
		print ("You are removing \n"'%s' % (name))
		newname = name.split('\n')[0] ### make newname = the header with all sequence inf removed since its after the line break
		newname = name.split(">")[1]### make newname = everything after the >
		delete.append(newname)
		#while newname.count("'") != 0: ### while there are strings in newname that have occurrences of "'" more than zero
			#newname = newname.replace("'", "") ### replace the apostrophe with nothing
			#delete.append(newname.strip()) ### add newname with whitespace removed to the list todelete

seqs = line.split(">")[1:]
seq_d = {}

for seq in seqs:
	seq_d[seq.split()[0]] = ''.join(seq.split('\n')[1:])
	
out = open(outfile, "w")

for seq in seqs:
	name = seq.split('\n')[0]
	if name not in delete:
		out.write('>%s\n%s\n' % (seq.split('\n')[0], ''.join(seq.split('\n')[1:])))
