def read_txt(fname):
    
    sequence = ""	
    file = open(fname,"r")

    for line in file.readlines():
        if line.endswith('\n'):
            line = line[:-1]
        sequence = sequence+line

    return sequence

def trans(seq):
    bases = {"A":"T","T":"A","C":"G","G":"C"}
    l = len(seq)+1
    sequence = ""

    for i in range(1,l):
        sequence = sequence+bases.get(seq[-i])

    print(sequence)

sq = read_txt("rosalind_revc.txt")
trans(sq)