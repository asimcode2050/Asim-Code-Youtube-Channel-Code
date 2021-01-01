class CleanPrintDict():
    def __init__(self, my_dict):
        self.my_dict = my_dict
    def __str__(self):
        s =''
        for key, value in self.my_dict.items():
            s += key +':'+str(value)+' '
        return s.strip()    

our_dict = {'a':123, 'b':456}
print(our_dict)
clean_dict = CleanPrintDict(our_dict)
print(clean_dict)
