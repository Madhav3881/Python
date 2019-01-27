def read_txt(fname):
    
    sequence = ""
    sequences = []	
    file = open(fname,"r")

    for line in file.readlines():
        if line.endswith('\n'):
    	    sequence = line[:-1]
        else:
            sequence = line
        sequences.append(sequence)

    return sequences

def point_M(seq1,seq2):

    nom = 0

    for i in range(0,len(seq1)):
        if(seq1[i] != seq2[i]):
            nom = nom+1

    return nom

if __name__ == '__main__':
    seq = read_txt("rosalind_hamm (1).txt")
    print(point_M(seq[0],seq[1]))