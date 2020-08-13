# ---------------------------------IMPORTING MODULES----------------------
from protien_operations import isProtienValid, splitSequence, findAcid, countOccurences
import database
# import plotting
# --------------------------------DRIVER FUNCTION-------------------------
arr = []
with open("assets/Ecol_K12_MG1655_.ena") as f:  # opening the file
    for line in f:  # iterating over each line
        if(line[0] == '>'):
            # if lenght of array is > 0
            # add the files to the database using the acid name
            # also the other details like occurences of ATGC and others
            # then, delete the array you created
            if(len(arr)):
                # combining the list of triplets to a sequence string
                sequence = ''.join(arr)
                if(isProtienValid(sequence)):  # perfoming checks for valid protien
                    print('Checking protien: {}'.format(ACID_LABEL), end='')
                    # the sequence array is split in terms of triplet codons
                    newlist = splitSequence(sequence)
                    # finding the corresponding acid
                    lacid = ''.join(findAcid(newlist))
                    # counting the frequencies of the acids occured
                    A, T, G, C = countOccurences(sequence)
                    # database.pushToDatabase(ACID_LABEL,sequence,lacid,A,T,G,C)
                else:
                    print('Entire Sequence Wrong.')
                    exit()
            ACID_LABEL = line
            arr.clear()
        else:
            arr.append(line.rstrip())
# ----------------------------------------------------------------------------------
# newDict = database.retrieveDatabase()
# print('returned sequence count is',newDict)
# plotting.plot(newDict)
