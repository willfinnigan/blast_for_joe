from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbitblastxCommandline
from io import StringIO

def do_blast_biopython(db_file, fasta_path):
    #Alternative function to do tblastn using biopython

    output = NcbitblastxCommandline(query=fasta_path, db=db_file, evalue=10,
                                    num_threads=1, outfmt=5, num_alignments=1000)()
    print(output[0])
    blast_record = NCBIXML.read(StringIO(output[0]))
    return blast_record
