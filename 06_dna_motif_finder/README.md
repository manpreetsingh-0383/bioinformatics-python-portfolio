# DNA Crime Analyzer

crime_scene_dna = input("Enter Crime Scene DNA: ").upper()

suspects = {
    "Suspect 1": "ATGCGTAC",
    "Suspect 2": "GCTAGCTA",
    "Suspect 3": "ATGCGTAC"
}

print("\nCrime Scene DNA:", crime_scene_dna)

found = False

for name, dna in suspects.items():
    if dna == crime_scene_dna:
        print(f"{name} is a MATCH! 🧬")
        found = True

if not found:
    print("No suspect matched ❌")