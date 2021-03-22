def Descending_Order(num):
  num_list = list(str(num))
  num_list.sort()
  num_list.reverse()
  max_num = ""
  for num in num_list:
    max_num += str(num)
  return int(max_num)
