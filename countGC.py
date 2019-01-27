def read_txt(fname):
    
    sequence = ""	
    file = open(fname,"r")
    sequences = []

    for line in file.readlines():
        if line.startswith('>'):
            if sequence != "":
                t = (header,sequence)
                sequences.append(t)
            if line.endswith('\n'):
                line = line[:-1]
            header = line[1:]
            sequence = ""
        else:
            if line.endswith('\n'):
                line = line[:-1]
            sequence = sequence+line

    t = (header,sequence)
    sequences.append(t)

    return sequences

def GC_content(sequence):

    GC = 0

    for i in range(0,len(sequence)):
        if sequence[i] == "G" or sequence[i] == "C":
            GC = GC+1

    GC = (GC*100)/len(sequence)
    
    return GC

if __name__ == '__main__':
    GC_per = []
    gc = 0
    i = 0

    dna = read_txt("rosalind_gc.txt")
    for name, seq in dna:
        GC_per.append(name)
        if GC_content(seq) > gc:
            gc = GC_content(seq)
            j = i
        i = i+1
    print(GC_per[j])
    print(gc)