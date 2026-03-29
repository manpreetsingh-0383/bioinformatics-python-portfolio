# DNA to Protein Translation

# Genetic Code Dictionary
codon_table = {
    'AUG': 'M', 'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y',
    'UGU': 'C', 'UGC': 'C',
    'UGG': 'W',
    'UAA': '*', 'UAG': '*', 'UGA': '*'
}

# Input DNA
dna = input("Enter DNA Sequence: ").upper()

# Convert DNA to RNA
rna = dna.replace("T", "U")

# Translate RNA to Protein
protein = ""

for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    
    if len(codon) == 3:
        protein += codon_table.get(codon, '?')

# Output
print("DNA:", dna)
print("RNA:", rna)
print("Protein:", protein)