import sys
from Bio import SeqIO


alnfile = sys.argv[1]
filter_percent = sys.argv[2]

alignment=SeqIO.parse(open(alnfile), 'fasta')

removed_sequences=[]
with open(alnfile + '.AT_rich.faa', 'w') as keep:
    for record in alignment:
        name, sequence = record.id, str(record.seq)
        AT_count = 0
        AT_count += record.seq.count('A')
        AT_count += record.seq.count('T')
        
        print ((record.id) + ": " + (str(len(record.seq))) + " nucleotides " + (str(AT_count)) + " AT")
        
        AT_rich = AT_count / len(record.seq)
        if AT_rich > float(filter_percent)/100:
            keep.write(f'>{record.description}_{round(AT_rich, 2)}\n{record.seq}\n')
        else:
            #print(record.name, alnfile)
            removed_sequences.append(f'>{record.description}\n{record.seq}\n')

with open(alnfile + '.not_AT_rich.faa', 'w') as removed:
    for record in removed_sequences:
        removed.write(record)
