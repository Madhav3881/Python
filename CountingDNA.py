def read_txt(fname):
    
    sequence = ""	
    file = open(fname,"r")

    for line in file.readlines():
    	if line.endswith('\n'):
    	    line = line[:-1]
    	sequence = sequence+line

    return sequence

def count_bases(seq):
    bases = {"A":0,"T":0,"C":0,"G":0}
    l = len(seq)
    
    for i in range(0,l):
    	bases[seq[i]] +=1

    print bases.get("A"), bases.get("C"), bases.get("G"), bases.get("T")

sq = read_txt("rosalind_hamm.txt")
count_bases(sq)