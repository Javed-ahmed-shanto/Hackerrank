import string
def solve(s):
    if 0 < len(s) < 1000:
       return string.capwords(s,' ')
    #or
    #return s.title()
