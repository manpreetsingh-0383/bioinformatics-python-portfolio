# DNA Processing Toolkit

dna = input("Enter DNA Sequence: ").upper()

# Length
length = len(dna)

# GC Content
G = dna.count("G")
C = dna.count("C")
gc = (G + C) / length * 100 if length > 0 else 0

# Reverse
reverse = dna[::-1]

# Complement
complement = dna.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g").upper()

# Reverse Complement
reverse_complement = complement[::-1]

# Output
print("\nDNA Sequence:", dna)
print("Length:", length)
print("GC Content:", gc, "%")

print("Reverse:", reverse)
print("Complement:", complement)
print("Reverse Complement:", reverse_complement)