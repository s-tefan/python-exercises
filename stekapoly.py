class StekaPoly:
    coeffs=[]
    
    __init__(self,coeffs):
        self.coeffs=coeffs

    __copy__(self):
        return StekaPoly(self.coeffs)

    __deepcopy__(self):
        return StekaPoly(self.coeffs.copy()):


    add(self,addend):
        sl=len(self.coeffs)
        al=len(addend.coeffs)
        if sa>=al:
            for k in range(al):
                self.coeffs[k]+=addend.coeffs[k]
        else:
            for k in range(sl):
                self.coeffs[k]+=addend.coeffs[k]
            sel.coeffs.extend(addend.coeffs[sl:])

    __add__(self,addend:
        return self.deepcopy().add(addend)



