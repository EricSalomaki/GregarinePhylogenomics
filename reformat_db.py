import os
import sys
import glob

d = {'Acancast.faa': 'Acanthamoeba_castellanii', 'AplycaliNEW.faa': 'Aplysia_californica', 'Arabthal.faa': 'Arabidopsis_thaliana', 'BodosaltNEW.faa': 'Bodo_saltans', 'BranflorNEW.faa': 'Branchiostoma_floridae', 'Chlarein.faa': 'Chlamydomonas_reinhardtii', 'ChoncrisNEW.faa': 'Chondrus_crispus', 'CoprcineNEW.faa': 'Coprinus_cinereus', 'CoprprotNEW.faa': 'Copromyxa_protea_CF08-5', 'CyanmeroNEW.faa': 'Cyanidioschyzon_merolae', 'Cyanpara.faa': 'Cyanophora_paradoxa', 'Dictdisc.faa': 'Dictyostelium_discoideum', 'DrosmelaNEW.faa': 'Drosophila_melanogaster', 'Emilhuxl.faa': 'Emiliania_huxleyi', 'GaldsulpNEW.faa': 'Galdieria_sulphuraria', 'GiarlambNEW.faa': 'Giardia_lamblia', 'Goniavon.faa': 'Goniomonas_avonlea', 'Guilthet.faa': 'Guillardia_theta', 'Isoc1324NEW.faa': 'Isochrysis_sp_CCMP1324', 'Leismajo.faa': 'Leishmania_major', 'Monoexil.faa': 'Monocercomonoides_exilis', 'Naeggrub.faa': 'Naegleria_gruberi', 'Planfung.faa': 'Protostelium_aurantium_var_fungivorum', 'PygsbifoNEW.faa': 'Pygsuia_biforma', 'Sacccere.faa': 'Saccharomyces_cerevisiae', 'SapppedaNEW.faa': 'Sappinia_pedata', 'Spirsalm.faa': 'Spironucleus_salmonicida', 'Thalpseu.faa': 'Thalassiosira_pseudonana', 'Tricvagi.faa': 'Trichomonas_vaginalis', 'Trypbruc.faa': 'Trypanosoma_brucei', 'UstimaydNEW.faa': 'Ustilago_maydis', 'VolvcartNEW.faa': 'Volvox carteri'}

for i in d:
        c = 0

        infile = open(i)
        line = infile.read()
        infile.close()

        seqs = line.split('>')[1:]

        out = open('%s_reformatted.fas' % (i.split('.')[0]), 'w')
        out2 = open('%s_archived.fas' % (i.split('.')[0]), 'w')
        for seq in seqs:
                out.write('>%s_%s\n%s\n' % (d[i], c, ''.join(seq.split('\n')[1:])))
                out2.write('>%s_%s@%s\n%s\n' % (d[i], c, seq.split('\n')[0], ''.join(seq.split('\n')[1:])))
                c = c + 1
        out.close()
        out2.close()