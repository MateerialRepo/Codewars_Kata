def disemvowel(string):
    check = ['a','A','e','E','i','I','o','O','u','U']
    for i in check:
      if i =='a' or i=='A':
        answ = string.replace(i,'')
      else:
        answ = answ.replace(i,'')
    return answ
