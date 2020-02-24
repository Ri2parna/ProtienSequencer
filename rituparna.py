#checking wether the protien is valid or not
def isProtienValid(_str_):
    if(_str_[-4:-1] == 'taa' or 'uaa' or _string_ == 'uag' or _string_ == 'uga'):
        if(len(_str_) % 3 == 0):  # checking for multiples of 3
            return True
        else:
            return False
    else:
        return False