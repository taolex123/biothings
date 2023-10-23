from pathlib import Path

files = Path("C:/Users/Administrator/Downloads/YGNGV")#path

def id_simplify(i,outfile):
    with open(i,'rt') as f1:
        with open(outfile,'wt') as f2:
            for eachline in f1:
                eachline = eachline.replace('_site_1', '').replace('_', ' ')#alternate
                if eachline[0] == '>':
                    f2.write(eachline.strip().split()[0])
                    f2.write('\n')
                else:
                    f2.write(eachline)
                    
def search_fa_simplify():
    for i in files.iterdir():
        if i.suffix == '.fasta':
            outfile = i.parent / (i.stem + '_simplify.fasta')
            id_simplify(i,outfile)

search_fa_simplify()
