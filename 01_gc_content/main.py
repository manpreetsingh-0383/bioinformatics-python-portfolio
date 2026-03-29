dna = input("Enter The DNA Sequence:").upper()

length = len(dna)

A_count = dna.count("A")
T_count = dna.count("T")
G_count = dna.count("G")
C_count = dna.count("C")

gc = (G_count + C_count) / length * 100

print("DNA Sequence:", dna)
print("Length:", length)

print("A:", A_count)
print("T:", T_count)
print("G:", G_count)
print("C:", C_count)

print("GC Content:", gc, "%")