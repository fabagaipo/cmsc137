def xor(a, b):
  result = ''
  for i in range(1, len(b)):
    result += '1' if a[i] != b[i] else '0'
  
  return result
   
def mod2div(dividend, divisor):
  pick = len(divisor)
  
  tmp = dividend[0 : pick]
  while pick < len(dividend):
  
      if tmp[0] == '1':
          tmp = xor(divisor, tmp) + dividend[pick]
      else:
          tmp = xor('0'*pick, tmp) + dividend[pick]
      pick += 1
  
  if tmp[0] == '1':
      tmp = xor(divisor, tmp)
  else:
      tmp = xor('0'*pick, tmp)
  checkword = tmp
  
  return checkword

def main():
    # Key
    divisor = '1011'
   
    # Sample Input
    sample_data = '1001110'
    sample_result = mod2div(sample_data, divisor)
    if sample_result.count('1') == 0:
        print("Accept data")
    else:
        print("CRC error detected.")
 
    # User Input
    data = input("Data: ")
    result = mod2div(data, divisor)
    if result.count('1') == 0:
        print("Accept data")
    else:
        print("CRC error detected.")
 
main()
