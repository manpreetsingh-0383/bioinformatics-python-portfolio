def detect_mutations(seq1, seq2):
    mutations = []

    min_len = min(len(seq1), len(seq2))

    # Check substitutions
    for i in range(min_len):
        if seq1[i] != seq2[i]:
            mutations.append((i, seq1[i], seq2[i], "Substitution"))

    # Check insertion
    if len(seq2) > len(seq1):
        mutations.append(("End", "-", seq2[len(seq1):], "Insertion"))

    # Check deletion
    elif len(seq1) > len(seq2):
        mutations.append(("End", seq1[len(seq2):], "-", "Deletion"))

    return mutations


# MAIN
dna1 = input("Enter original DNA: ").upper()
dna2 = input("Enter mutated DNA: ").upper()

result = detect_mutations(dna1, dna2)

print("\nMutations Found:")
for m in result:
    print(m)