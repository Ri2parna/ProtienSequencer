# importing functions used in the files
from rituparna import isProtienValid, splitSequence, findAcid
print('Sequence\t FoundProtien')
with open("data") as f:  # opening the file
    for item in f:  # traversing the file object for each line
        if(item[0] == '>'):
            sequence = f.readline().rstrip()
            if(isProtienValid(sequence)):  # code for checking stop sequence and triplets
                # print("Found Stop sequence in", sequence)#this line prints
                # the valid sequence
                newlist = splitSequence(sequence)
                lacid = ''.join(findAcid(newlist))
                print('Sequence is', str(lacid))
        else:  # ignoring the lines till a '>' is not found.
            pass