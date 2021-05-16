class RosalindFasta:
    def __init__(self, fasta_id, sequence):
        self.fasta_id = fasta_id
        self.sequence = sequence


def splice_motif(dna_seq, motif):
    current_search_pos = 0
    current_search_base = motif[current_search_pos]
    print(current_search_base)
    motif_positions = []
    for base in range(len(dna_seq)):
        if dna_seq[base] == current_search_base:
            motif_positions.append(str(base + 1))  # Add 1 to base since DNA counting begins at 1 not 0.
            if current_search_pos == len(motif) - 1:
                break
            else:
                current_search_pos += 1
                current_search_base = motif[current_search_pos]
                print(current_search_base)

    return motif_positions


def create_fasta_list(file_name):
    file = open(file_name, "r")

    current_id = ""
    current_seq = ""
    fasta_list = []

    for line in file:
        if line[0] == ">" and current_id == "":
            current_id = line[1:].rstrip()
        elif line[0] == ">" and current_id != "":
            fasta_list.append(RosalindFasta(current_id, current_seq))
            current_id = line[1:].rstrip()
            current_seq = ""
        else:
            current_seq += line.rstrip()
    else:
        fasta_list.append(RosalindFasta(current_id, current_seq))

    file.close()
    return fasta_list


sequence_list = create_fasta_list('rosalind_sseq(2).txt')

positions = splice_motif(sequence_list[0].sequence, sequence_list[1].sequence)
print(positions)

pos_string = ' '.join(positions)

output_file = open('solution.txt', 'w')
output_file.write(pos_string)
output_file.close()
print(pos_string)
