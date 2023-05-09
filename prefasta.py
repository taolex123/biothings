# -*- coding: utf-8 -*-
from Bio import SeqIO
import pandas as pd

def grepaa(fasta_file, new_fasta_file):
    records = list(SeqIO.parse(fasta_file, 'fasta'))
    filtered_records = []
    for record in records:
        if any(char in record.seq for char in ['B', 'J', 'O', 'U', 'X', 'Z']):
            continue
        filtered_records.append(record)
    with open(new_fasta_file, 'w', encoding='utf-8') as output_handle:
        SeqIO.write(filtered_records, output_handle, 'fasta')

def seqaa(min_length, max_length, input_file, output_file):
    with open(input_file, encoding='utf-8') as original_fasta:
        with open(output_file, "w", encoding='utf-8') as new_fasta:
            for record in SeqIO.parse(original_fasta, "fasta"):
                if min_length <= len(record.seq) <= max_length:
                    SeqIO.write(record, new_fasta, "fasta")

def rmdupaa(input_file, output_file):
    sequences = set()
    with open(output_file, "w") as out_handle:
        for record in SeqIO.parse(input_file, "fasta"):
            if str(record.seq) not in sequences:
                sequences.add(str(record.seq))
                SeqIO.write(record, out_handle, "fasta")

def sortaa(input_file, output_file):
    records = sorted(SeqIO.parse(input_file, "fasta"), key=lambda x: len(x.seq))
    with open(output_file, "w") as out_handle:
        SeqIO.write(records, out_handle, "fasta")

def renameaa(input_file, output_file):
    records = list(SeqIO.parse(input_file, "fasta"))
    for i, record in enumerate(records):
        record.id = "seq{:04d}".format(i+1)
        record.description = ""
    SeqIO.write(records, output_file, "fasta")

def f2t(fasta_file, csv_file):
    records = SeqIO.parse(fasta_file, "fasta")
    df = pd.DataFrame(columns=["id", "sequence"])
    for record in records:
        df = df.append({"id": record.id, "sequence": str(record.seq)}, ignore_index=True)
    df.to_csv(csv_file, index=False)

def t2f(csv_file, fasta_file):
    df = pd.read_csv(csv_file)
    records = []
    for index, row in df.iterrows():
        record = SeqIO.SeqRecord(Seq(row["sequence"]), id=row["id"], description="")
        records.append(record)
    SeqIO.write(records, fasta_file, "fasta")