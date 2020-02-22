import os
import sys
import glob
from Bio.Blast import NCBIXML


ending = sys.argv[1]
db = sys.argv[2]


genes = [fname[:-len(ending)] for fname in glob.glob('*%s' % (ending))]

#genes = ['abce']

for gene in genes:
        print 'working on gene %s' % (gene)
        os.system('blastp -query %s%s -db %s -out %s_rep.blastout  -max_target_seqs 10 -outfmt 5 -num_threads 60' % (gene,ending,db,gene))
        result_handle = open ('%s_rep.blastout' % (gene))
        blast_records = NCBIXML.parse(result_handle)
        out = open('%s_reciped.fas' % (gene),'w')

        infile = open('%s%s' % (gene,ending))
        line = infile.read()
        infile.close()

        seqs = line.split('>')[1:]

        d = {}

        for seq in seqs:
                d[seq.split('\n')[0]] = seq


        try:
                for record in blast_records:
                        if len(record.alignments) != 0:
          #                      print record.alignments[0].title
                                hit = record.alignments[0].title.split(' ')[1]
				hit = '_'.join(hit.split('_')[:2])
                                #print hit
                                #print gene
                                if hit == '_'.join(gene.split('_')[:2]):
                                        #print 'ok'
                                        out.write('>%s' % (d[record.query]))
                                else:
                                        print '%s %s %s' % ('_'.join(gene.split('_')[:2]),hit,record.query)
        except ValueError:
                print 'gene %s had no hits' % (gene)