from rituparna import isProtienValid #importing functions used in the files

with open("data") as f:  # opening the file
    for item in f:  # traversing the file object for each line
        if(item[0] == '>'):
            print('hi')
            sequence = f.readline().rstrip()
            if(isProtienValid(sequence)):  # code for checking stop sequence and triplets
                print("Found Stop sequence in", sequence)#this line prints the valid sequence

                '''Eiat Sequence tu eta string hoi, eitu protien sequence tu hoi, eituk 
                toi binary tree ba ji bisaro heitu form ot store kori dibi
                FunctionForStoringTheString()---> eitu function e string tu data structure
                                                  etat store kori dibo aru hei data structure 
                                                  tu return kori dibo.'''
        else:  # ignoring the lines till a '>' is not found.
            pass