# DNA Motif Finder

dna = input("Enter DNA Sequence: ").upper()
motif = input("Enter Motif: ").upper()

positions = []

for i in range(len(dna) - len(motif) + 1):
    if dna[i:i+len(motif)] == motif:
        positions.append(i)

print("\nDNA Sequence:", dna)
print("Motif:", motif)

if positions:
    print("Motif found at positions:", positions)
else:
    print("Motif not found ❌")