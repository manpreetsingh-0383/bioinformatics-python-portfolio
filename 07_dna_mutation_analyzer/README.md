# 🧬 DNA Mutation Analyzer

A simple Python-based bioinformatics tool to detect mutations between two DNA sequences.

## 🚀 Features

- Detects **Substitution mutations**
- Detects **Insertion mutations**
- Detects **Deletion mutations**
- Provides mutation position and type

---

## 🧠 How It Works

The program compares two DNA sequences:

- **Original DNA**
- **Mutated DNA**

It then:
1. Compares each base pair
2. Identifies mismatches (substitutions)
3. Detects extra or missing bases (insertions/deletions)

---

## 💻 Usage

### Run the program:

```bash
python main.py

Enter original DNA: ATGCGTACGTTAGC
Enter mutated DNA: ATGAGTACGTTTAGCA

Mutations Found:
(3, 'C', 'A', 'Substitution')
('End', '-', 'A', 'Insertion')