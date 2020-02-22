import os
import sys
import glob

#script to parse through a blast output, pull top five hits per query, and compile that into a fasta file comprised of those sequencnes
#usage is python pull_top_5_blast_hits.py blastfile.out outfile.fasta
#for example for f in *.out; do python pull_top_5_blast_hits.py $f ToAdd/$f.fasta; done
#line 43 is hard-coded with the location of the fasta files used to make your blastDB - change as necessary with preferably the full path


###########################
#### MAKING A FUCNTION ####
###########################


def create_good_hits(blast_records): 	#define the function create_good_hits(blast_records)
	dict = {}							#make empty dictionary
	list_to_get = []					#make empty list
	for rec in blast_records:			#iterate through the blast output
		hitname = rec.split()[1]		#assign blast subject to variable hitname
		#print hitname
		taxon = hitname.split('_')[0]	#assign first part of hitname as variable taxon
		evalue = float(rec.split()[-2])	#assign second to last split as the evalue
		#print evalue
		if taxon in dict and evalue < 0.0000000001 and len(dict[taxon]) <5 and hitname not in dict[taxon]: 	#set necessary conditions to be included
			dict[taxon].append(hitname)																			#add taxon that meets conditions to the dictionary
			#print dict[taxon]
		elif taxon in dict:										#if the taxon is already in the dictionary but does not meet conditions, move on
			pass
		elif taxon not in dict and evalue < 0.0000000001:			#if the taxon is not in the dictionary but meets the evalue condition, add to the dictionary
			dict[taxon] = [hitname]
		else:
			dict[taxon] = []									#if a taxon exists but never meets any condition to add, skip it
	for i in dict:									#iterate through the dictionary
		for header in dict[i]:						#iterate through the headers in the dictionary
			list_to_get.append(header)				#add headers to the list_to_get in the end
	return(list_to_get)								#leave the function

#################################
#### PARSE FASTAS FROM BLAST ####
#################################

files = [fname for fname in glob.glob('/home/users/eric/Gregarines/DatasetConstruction/TotalDataset/*.fas')] #pull in the fasta files that were the database in the blast search

seq_d = {}															#make empty dictionary
for fname in files:													#iterate though all files
	infile = open(fname)											#open each file
	line = infile.read()											#read in lines from each file	
	infile.close()													#close the file
	seqs = line.split('>')[1:]										#split each sequence on the header >
	for seq in seqs:												#iterate though sequences
		seq_d[seq.split('\n')[0]] = ''.join(seq.split('\n')[1:])	#make a dictionary of headers and sequences
	
#############################
#### PARSE BLAST OUTPUTS ####
#############################

infile = open(sys.argv[1],'r')						#open blast output
lines = infile.readlines()							#iterate through the lines of the blast output
infile.close()										#close the file

records_dict = {}									#create empty dictionary for records

for line in lines:									#iterate through the lines of a blast output
	query = line.split()[0]							#assign the query as the first split
	if query in records_dict:						#iterate through the queries
		records_dict[query].append(line)			#add each line as the value for each query that serves as the key
	else:	
		records_dict[query] = [line]			#if query doesn't exist, make it a new key with the value that is the line
			
###########################################
#### MAKE FASTA OF TOP FIVE BLAST HITS ####
###########################################

out = open(sys.argv[2], 'w') 						#open file to write to

final_list = []											#make empty list

for query in records_dict:								#iterate through records dict from blast output parsing
	list_to_analyze = records_dict[query]				#make each key in the records 
	#print len(list_to_analyze)
	results = create_good_hits(list_to_analyze)			#run function create_good_hits on list to analyze
	#print len(results)
	final_list = list(set(final_list + results))		#remove duplicate sequences
	
for header in final_list:								#iterate though headers in the final list and then print the headers and sequences into a fasta file as an output
	out.write('>%s\n%s\n' % (header, seq_d[header]))

out.close()		
