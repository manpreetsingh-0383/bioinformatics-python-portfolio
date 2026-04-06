import matplotlib.pyplot as plt

def calculate_gc_content(dna_seq):
    g = dna_seq.count('G')
    c = dna_seq.count('C')
    gc_content = ((g + c) / len(dna_seq)) * 100
    return gc_content

def gc_content_sliding_window(dna_seq, window_size):
    gc_values = []
    
    for i in range(len(dna_seq) - window_size + 1):
        window = dna_seq[i:i+window_size]
        gc = calculate_gc_content(window)
        gc_values.append(gc)
    
    return gc_values

# Sample DNA sequence
dna_sequence = "ATGCGATCGATCGATCGATCGCTAGCTAGCTAGCTAGCTAGCGCGCGATATATATATCGCG"

window_size = 5

gc_values = gc_content_sliding_window(dna_sequence, window_size)

# Plotting
plt.plot(gc_values)
plt.title("GC Content Across DNA Sequence")
plt.xlabel("Position")
plt.ylabel("GC Content (%)")
plt.show()