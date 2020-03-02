from array import *
class acid():
    def __init__(self,codons,acid):
        self.codons = codons
        self.acid = acid


list = []
list.append(acid('TTT','F'))
list.append(acid('TTC','F'))
list.append(acid('TTA','K'))
list.append(acid('TTG','K'))
list.append(acid('TCT','S'))
list.append(acid('TCC','S'))
list.append(acid('TCA','S'))
list.append(acid('TCG','S'))
list.append(acid('TAT','Y'))
list.append(acid('TAC','Y'))
list.append(acid('TAA','stop'))
list.append(acid('TAG','stop'))
list.append(acid('TGT','C'))
list.append(acid('TGC','C'))
list.append(acid('TGA','stop'))
list.append(acid('TGG','W'))
list.append(acid('CTT','K'))
list.append(acid('CTC','K'))
list.append(acid('CTA','K'))
list.append(acid('CTG','K'))
list.append(acid('CCT','P'))
list.append(acid('CCC','P'))
list.append(acid('CCA','P'))
list.append(acid('CCG','P'))
list.append(acid('CAT','H'))
list.append(acid('CAC','H'))
list.append(acid('CAA','Z'))
list.append(acid('CAG','Z'))
list.append(acid('CGT','R'))
list.append(acid('CGC','R'))
list.append(acid('CGA','R'))
list.append(acid('CGG','R'))
list.append(acid('ATT','I'))
list.append(acid('ATC','I'))
list.append(acid('ATA','I'))
list.append(acid('ATG','M'))
list.append(acid('ACT','T'))
list.append(acid('ACC','T'))
list.append(acid('ACA','T'))
list.append(acid('ACG','T'))
list.append(acid('AAT','N'))
list.append(acid('AAC','N'))
list.append(acid('AAA','K'))
list.append(acid('AAG','K'))
list.append(acid('AGT','S'))
list.append(acid('AGC','S'))
list.append(acid('AGA','R'))
list.append(acid('AGG','R'))
list.append(acid('GTT','V'))
list.append(acid('GTC','V'))
list.append(acid('GTA','V'))
list.append(acid('GTG','V'))
list.append(acid('GCT','A'))
list.append(acid('GCC','A'))
list.append(acid('GCA','A'))
list.append(acid('GCG','A'))
list.append(acid('GAT','N'))
list.append(acid('GAC','N'))
list.append(acid('GAA','Q'))
list.append(acid('GAG','Q'))
list.append(acid('GGT','G'))
list.append(acid('GGC','G'))
list.append(acid('GGA','G'))
list.append(acid('GGG','G'))

class tree_node():
    def __init__(self,data):
        self.A = A
        self.T = T
        self.G = G
        self.C = C
        self.data = data

class BinaryTree():
    def __init__(self,root):
        self.root = tree_node()


def createtree(list,root):
     count = 0
     arr = array('u',[])
     root.A = tree_node()
     root.T = tree_node()
     root.G = tree_node()
     root.C = tree_node()
     count+=1
     arr[count-1] = 'A'
     if(count == 3):
         root.data = find_in_array(list,string)
     else:
         createtree(acid,root.A)
     arr[count - 1] = 'T'
     if(count == 3):
         root.data = find_in_array(list,string)
     else:
         createtree(acid, root.T)
     arr[count - 1] = 'G'
     if(count == 3):
         root.data = find_in_array(list,string)
     else:
         createtree(acid, root.G)
     arr[count - 1] = 'C'
     if (count == 3):
         root.data = find_in_array(list,string)
     else:
         createtree(acid, root.C)

     count-=1


def find_in_array(list,string):
    for object in list:
        if(string == object.codons):
            assert isinstance(object.acid, object)
            print(object.acid)



def main():
    root = BinaryTree
    createtree(list,root)