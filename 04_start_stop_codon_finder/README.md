# Start & Stop Codon Finder

This project identifies start and stop codons in a DNA sequence.

## 🧬 Features
- Detects start codon (ATG)
- Detects stop codons (TAA, TAG, TGA)
- Returns their positions

## ⚙️ How it Works
- The DNA sequence is scanned using a sliding window of 3 bases
- Each codon is compared with start and stop codons
- Positions are stored and displayed

## 📌 Example
DNA: ATGAAATAG  
Start Codon: [0]  
Stop Codon: [6]

## ▶️ How to Run
Run the script and enter a DNA sequence.

## 💡 Applications
- Gene prediction
- Genome annotation