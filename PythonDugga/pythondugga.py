# Use the dugga_python environment!!!!!!!!!!!!

# Emma Eliasson

#####################
# Part 1. Loops & If/else
######################

# Input data:
numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]

# a) Identify all numbers with an absolute value >= 10. Print the sum of those numbers.
summa = 0
for num in numbers:
    if abs(num) >= 10:
        summa += num
print(summa)

# 15 - 12 + 10 - 10 = 3
# 3

# b) Build and print a list of the cubes (n^3) of negative numbers:
cube_list = []
for num in numbers:
    if num < 0:
        cube_list.append(num**3)
print(cube_list)

# [-125, -1728, -343, -1000]
# (There are 4 negative numbers in numers and in this list. I at least know that the first and last cube-number is correct.)

# c) Scan left-to-right and print the first repeated absolute value; if none, print "No repeats"
seen = []
first_dup = None
for n in numbers:
    if abs(n) in seen:
        first_dup = abs(n)
        break
    else:
        seen.append(n)
print(first_dup if first_dup is not None else "No repeats")

# The first value that repeats its absolute value is 7. There is both 7 and -7 before 10 and -10.
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

# So when you run the file: python pythondugga.py brca_head500_genes.csv

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