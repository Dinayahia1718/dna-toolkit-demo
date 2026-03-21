from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def run_demo():
    file_path = "data/sample.fasta"
    
    print("--- Bioinformatics Repo Demo ---")
    
    # Check if the file exists first
    try:
        for record in SeqIO.parse(file_path, "fasta"):
            # Using the library to calculate GC content
            gc_val = gc_fraction(record.seq) * 100
            
            print(f"Sequence ID: {record.id}")
            print(f"Length:      {len(record.seq)} bp")
            print(f"GC Content:  {gc_val:.2f}%")
            print("-" * 30)
            
    except FileNotFoundError:
        print("Error: Could not find data/sample.fasta. Did you 'cd' into the repo?")

if __name__ == "__main__":
    run_demo()
