# Use the dugga_python environment!!!!!!!!!!!!

# Emma Eliasson

#####################
# Part 1. Loops & If/else
######################

# Input data:
numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]

# a) 
summa = 0
for num in numbers:
    if abs(num) >= 10:
        summa += num
print(summa)

# 3

# b)
cube_list = []
for num in numbers:
    if num < 0:
        cube_list.append(num**3)
print(cube_list)

# [-125, -1728, -343, -1000]

# c) 
seen = []
first_dup = None
for n in numbers:
    if abs(n) in seen:
        first_dup = abs(n)
        break
    else:
        seen.append(n)
print(first_dup if first_dup is not None else "No repeats")

# 7

######################
# Part 2
#######################

# Import libraries:
import csv
import pandas as pd
import matplotlib.pyplot as plt
import sys

####
# 2.1
#####

# Read the file "brca_head500_genes" into a dataframe.
# Since this is a .csv file, the separator is ",".

# Avoiding har coded paths by letting the user define the path to the input file.
input_file = sys.argv[1]     # Should be "brca_head500_genes.csv"

# Så när du kör filen: python pythondugga.py brca_head500_genes.csv

df = pd.read_csv(input_file, sep=',')

####
# 2.2
#####

# FPKM = Fragments Per Kilobase of transcript per Million mapped reads (chatgpt)

# 2.2.1 & 2.2.3

def plot_hist():
    plt.hist(df["fpkm_log2"])
    plt.title("Distribution of gene expression")
    plt.xlabel("Expression")
    plt.ylabel("Number of genes")
    plt.savefig('fpkm_distribution.png', dpi=300)  # I used AI to know that the saving must come before showing the histogram.
    plt.show()

# 2.2.2

# Call the function

plot_hist()

# This worked for me :). I get the histogram with the correct labels and the picture file is in my directory.