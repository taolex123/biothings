import itertools

amino_acids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

sequences = [''.join(seq) for seq in itertools.product(amino_acids, repeat=5)] # repeat=sequence length

with open('sequences.fasta', 'w') as f:
    for i, seq in enumerate(sequences):
        f.write(f'>seq{i}\n{seq}\n')
