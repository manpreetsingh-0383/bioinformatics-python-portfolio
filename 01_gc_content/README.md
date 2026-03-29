# GC Content Calculator (BioPython)

This project calculates the GC content of a DNA sequence using the BioPython library.

## 🧬 Features
- Uses Bio.Seq module from BioPython
- Calculates:
  - DNA length
  - Count of A, T, G, C
  - GC Content percentage

## ⚙️ How it Works
The program takes a DNA sequence and:
1. Counts the number of G and C nucleotides
2. Calculates GC content using the formula:

(G + C) / Total Length × 100

## 📌 Example Output
DNA Sequence: ATGCGTACGTTAGCGC  
Length: 16  

A: 3  
T: 4  
G: 5  
C: 4  

GC Content: 56.25 %

## 🚀 Requirements
- Python
- BioPython

Install BioPython using:
pip install biopython

## ▶️ How to Run
Run the script and it will display GC content and nucleotide counts.

## 💡 Applications
- Genome analysis
- DNA stability estimation
- Bioinformatics preprocessing