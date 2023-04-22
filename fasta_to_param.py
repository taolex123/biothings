from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd

def fasta_to_param(fasta_file_path, csv_file_path):
    records = list(SeqIO.parse(fasta_file_path, 'fasta'))
    data = []
    for record in records:
        sequence = str(record.seq)
        analysis = ProteinAnalysis(sequence)
        data.append([record.id, analysis.molecular_weight(), analysis.aromaticity(), analysis.instability_index(), analysis.isoelectric_point()])
    df = pd.DataFrame(data, columns=['id', 'molecular_weight', 'aromaticity', 'instability_index', 'isoelectric_point'])
    df.to_csv(csv_file_path, index=False)
#fasta_to_param('c2.fasta', 'c2para.csv')
