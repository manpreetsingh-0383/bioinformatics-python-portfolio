# Start and Stop Codon Finder

dna = input("Enter DNA Sequence: ").upper()

start_positions = []
stop_positions = []

for i in range(len(dna) - 2):
    codon = dna[i:i+3]
    
    if codon == "ATG":
        start_positions.append(i)
    
    if codon in ["TAA", "TAG", "TGA"]:
        stop_positions.append(i)

print("\nDNA Sequence:", dna)
print("Start Codon Positions (ATG):", start_positions)
print("Stop Codon Positions (TAA, TAG, TGA):", stop_positions)