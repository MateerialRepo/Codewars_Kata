def disemvowel(string):
    check = ['a','A','e','E','i','I','o','O','u','U']
    for i in check:
      if i =='a' :
        answ = string.replace(i,'')
      else:
        answ = answ.replace(i,'')
    return answ

#refactored implementation
# def disemvowel(s):
#     for i in "aeiouAEIOU":
#         s = s.replace(i,'')
#     return s
