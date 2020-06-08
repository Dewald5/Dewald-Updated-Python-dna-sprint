# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
inputfile ="DNAFile.txt" 
f = open(inputfile, "r") 
txt = f.read().replace("\n","")
def mutate():
    inputfile2 ="Mutate.txt"  
    inputfile3 ="DNAFile.txt"
    inputfile4 ="Normaldna.txt"

    f2 = open(inputfile2, "w") #opens the Mutate file and write to it
    f3 = open(inputfile3, "r") #opens and reads from the Dnafile
    f4 = open(inputfile4, "w") #opens and writes to the normal dnafile

    Dna = f3.read().replace("\n", "")  #removes all spaces and creates string 
    ddna = Dna.replace("a", "T")     #replaces all the 'a' with 'T'     
    ddna2 = Dna.replace("a", "A")    #replaces all the 'a' with 'A'
    
    f2.write(ddna)                  #writes the string to the file
    f4.write(ddna2)
    
    f2.close()                      #Closes the file
    f3.close()
    f4.close()
        
def translate(seq): 
      
    table = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    } 
    protein =""  
    for i in range(0, len(seq), 3): 
        codon = seq[i:i + 3] 
        if codon in table:
            protein+= table[codon]   #returns the variable if the 3 letters match in the table
        else:
            protein += "X"           #returns X because the 3 variables dont match any in the table 
    return protein

def filereader(file):                 #opens the file and reads it and removes all spaces in it
    Fcontent = open(file,"r")
    return Fcontent.read().replace("\n", "")

def txttranslate():
    mutate()                          #uses mutate function to change the files
    mutat = filereader("Mutate.txt")
    norm = filereader("Normaldna.txt")
    
    find = translate(mutat)         #uses translate function to return the correct values for the file    
    find1 = translate(norm)
    print("output of mutation" + "\n" + find + "\n" + "Output of normal" +"\n"+ find1)

txttranslate()            #prints the output of the changed files  
