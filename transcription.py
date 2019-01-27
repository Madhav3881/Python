def read_txt(fname):
    
    sequence = ""	
    file = open(fname,"r")

    for line in file.readlines():
        if line.endswith('\n'):
            line = line[:-1]
        sequence = sequence+line

    return sequence

def trans(seq):
    l = len(seq)
    newseq = ""
    
    for i in range(0,l):
        if seq[i] == "T":
            newseq = newseq+"U"
        else:
            newseq = newseq+seq[i]

    print(newseq)

sq = read_txt("rosalind_rna.txt")
trans(sq)