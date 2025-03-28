# GENE SEQUENCES FINDER SCRIPT V2
# you can create a summary of the analysis into a summary text file

import re
import csv

# Open and read the DNA sequence file
with open("./Homo_sapiens_TBK1_sequence.fa.txt", "r") as file:
    lines = file.readlines()[1:]

# A little post processing to ommit the fist line
# remove newlines convert it to a single line
dna_sequence  = "".join(lines).replace("\n", "")

# Define pattern and seqs lengths
maxLen = 50 # set max lengths
patterns = []

for i in range(maxLen):
    patterns.append(fr"([A-Z]{{{i}}})")


# Find all occurrences of the pattern
matches = []
for pattern in patterns:
    matches.extend(re.findall(pattern, dna_sequence))

# Count occurrences of each Neucleotides
pattern_count = {}
for match in matches:
    pattern_count[match] = pattern_count.get(match, 0) + 1

# Sort seqs by count in descending order
sorted_seqs = sorted(pattern_count.items(), key=lambda x: x[1], reverse=True)

# Add a column for seqs lengths
isorted_seqs = []
for seqs, counts in sorted_seqs:
    if counts > 1 and len(seqs) != 0:
        isorted_seqs.append([len(seqs), seqs, counts])

# Write results to a CSV file
with open('dna_seq_counts.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write header
    csvwriter.writerow(['Seqns', 'Count', 'Seqns_length'])
    
    # Write only seqs that appear more than once
    for i, seqs, count in isorted_seqs:
        if count > 1:
            csvwriter.writerow([seqs, count, i])

print("===SUMMARY===")

# Write a Sequences summary
# - Sequences length
# - Nucleotides distribution in in the sequence
# - Max occurrences of patterns len 2,3,4,5, 10-20, 20-30

print(f"Sequences length = {len(dna_sequence)}")
print("\nNucleotides distribution:")

# Print no of indivitual Nucleotides in the gene

print("Nucleotides, count")
for i, seqs, counts in isorted_seqs:
    if i == 1:
        print(seqs,"=",counts)


# Function to return the first occurrences 
# of pattern acoarding to its size

def seqs_l_first_find(index, array):
    temp_arr = []
    for i,s,c in array:
        if i == index:
            temp_arr.append([i,s,c])

    return temp_arr

# load an empty list with above Function
ff_seqs_l = []
for i in range(2,6):
    ff_seqs_l.append(seqs_l_first_find(i, isorted_seqs)[0])


# Print found sequence
print("\nSeqences found:\nLength, Seqns, Count")
for i,s,c in ff_seqs_l:
    print(f"{i}, {s}, {c}")

# Print found sequence of max length
print("Seqences with maxmimum length:")
print(*isorted_seqs.pop(), sep=", ")

print("\nSeqences counts have been exported to dna_seq_counts.csv")
