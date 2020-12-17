import subprocess as sp
from pathlib import Path
import os

def make_blast_db(filename):
    command = f"makeblastdb -in {filename} -dbtype nucl"
    sp.run(command, shell=True)

def do_blast(db_file, fasta_path, output_path):
    command = f"tblastn -db {db_file} -query {fasta_path} -out {output_path}"
    sp.run(command, shell=True)


if __name__ == "__main__":

    abs_path = str(Path(__file__).parents[0])

    db_file = f"{abs_path}/genome/SRR642936.fa"
    make_blast_db(db_file)

    for filename in os.listdir(abs_path + '/queries'):
        # only look at .fasta files
        if filename.endswith(".fasta"):
            fasta = f"{abs_path}/queries/{filename}"
            output_path = f"{abs_path}/results/{filename}.result.out"
            do_blast(db_file, fasta, output_path)

