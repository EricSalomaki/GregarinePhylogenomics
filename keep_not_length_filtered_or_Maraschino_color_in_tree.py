import sys
import glob
import os

treefile=sys.argv[1]
fasta=sys.argv[2]
outfile=sys.argv[3]

infile=open(treefile)
lines=infile.read()
infile.close

lines = lines.split("taxlabels")[1]
lines = lines.split("\n;")[0]
lines = lines.split("\n")

to_keep=[]
deleted=[]
for line in lines: 
	if "[&!color=#ff0000]" not in line: # identify sequences to keep
		line = line.strip("\t") #remove tab at the beginning of the line
		line = line.strip("'") #remove apostrophes
		line = line.rsplit("_", 1)[0] #remove length filter percentage
		to_keep.append(line) #add keep headers to list
	if "[&!color=#ff0000]" in line: #identify sequences to be deleted
		deleted.append(line) #add do deleted list
#print(to_keep)	
#print(len(to_keep))

infile = open(fasta) ### open system argument 2 - the alignment 
lines = infile.read() ### read infile in as line
infile.close() ### close infile
starting_seqs=[]
seqs = lines.split('>')[1:] ### split line on >, keep everything after the first split (which was an empty space due to split always breaking into two - first > had nothing before it)
seq_d = {} ### make an empty directory called seq_d
for line in lines:
	if ">" in line:
		starting_seqs.append(line)
	
for seq in seqs: ### for every string in list seqs
	seq=seq.replace('*','') #remove any remaining stop codons
	seq_d[seq.split("\n")[0]] = ''.join(seq.split('\n')[1:]) ### make seq_d of key being the sequence name and the sequence (all wrapped lines joined into a single line)
out = open(outfile, 'w') #create your outputfile


for kept in to_keep [1:]: #iterate through 

	kept = seq_d[kept] #pulls the sequences to be kept
print "You kept",len(to_keep)-1, "sequences,",len(deleted), "were removed by you and", len(starting_seqs) - len(deleted) - len(to_keep) +1, "were removed by the length filter"

for seq in seqs:
	name = seq.split('\n')[0]
	if name in to_keep:
		out.write('>%s\n%s\n' % (seq.split('\n')[0], ''.join(seq.split('\n')[1:])))
