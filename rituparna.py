#determining the acid structure
acid = {}
acid['TTT'] = 'F'
acid['TTC'] = 'F'
acid['TTA'] = 'K'
acid['TTG'] = 'K'
acid['TCT'] = 'S'
acid['TCC'] = 'S'
acid['TCA'] = 'S'
acid['TCG'] = 'S'
acid['TAT'] = 'Y'
acid['TAC'] = 'Y'
acid['TAA'] = 'stop'
acid['TAG'] = 'stop'
acid['TGT'] = 'C'
acid['TGC'] = 'C'
acid['TGA'] = 'stop'
acid['TGG'] = 'W'
acid['CTT'] = 'K'
acid['CTC'] = 'K'
acid['CTA'] = 'K'
acid['CTG'] = 'K'
acid['CCT'] = 'P'
acid['CCC'] = 'P'
acid['CCA'] = 'P'
acid['CCG'] = 'P'
acid['CAT'] = 'H'
acid['CAC'] = 'H'
acid['CAA'] = 'Z'
acid['CAG'] = 'Z'
acid['CGT'] = 'R'
acid['CGC'] = 'R'
acid['CGA'] = 'R'
acid['CGG'] = 'R'
acid['ATT'] = 'I'
acid['ATC'] = 'I'
acid['ATA'] = 'I'
acid['ATG'] = 'M'
acid['ACT'] = 'T'
acid['ACC'] = 'T'
acid['ACA'] = 'T'
acid['ACG'] = 'T'
acid['AAT'] = 'N'
acid['AAC'] = 'N'
acid['AAA'] = 'K'
acid['AAG'] = 'K'
acid['AGT'] = 'S'
acid['AGC'] = 'S'
acid['AGA'] = 'R'
acid['AGG'] = 'R'
acid['GTT'] = 'V'
acid['GTC'] = 'V'
acid['GTA'] = 'V'
acid['GTG'] = 'V'
acid['GCT'] = 'A'
acid['GCC'] = 'A'
acid['GCA'] = 'A'
acid['GCG'] = 'A'
acid['GAT'] = 'N'
acid['GAC'] = 'N'
acid['GAA'] = 'Q'
acid['GAG'] = 'Q'
acid['GGT'] = 'G'
acid['GGC'] = 'G'
acid['GGA'] = 'G'
acid['GGG'] = 'G'


def findAcid(newlist):
	replacedProtien = []
	for item in newlist:
		if(item.upper() in acid):
			replacedProtien.append(acid[item.upper()])
		else:
			replacedProtien.append(NULL)
	return replacedProtien



#checking wether the protien is valid or not
def isProtienValid(_str_):
    if(_str_[-4:-1] == 'taa' or 'uaa' or _string_ == 'uag' or _string_ == 'uga'):
        if(len(_str_) % 3 == 0):  # checking for multiples of 3
            return True
        else:
            return False
    else:
        return False
def splitSequence(_str_):
	newarray = []
	for i in range(0,len(_str_),3):
		newarray.append(_str_[i:i+3])
	return newarray
def countOccurences(_str_):
	occurences = {
		'a' : 0,
		't' : 0,
		'g' : 0,
		'c' : 0
	}
	for item in _str_:
		if(item in occurences):
			occurences[item] += 1
	return(occurences['a'],occurences['t'],occurences['g'],occurences['c'])
