def sender(A):
  n = len(A) + 1
  codeword = ""
  ones = 0

  for i in range(n - 1):
    if A[i] == 1:
      ones += 1

  parity = '1' if ones % 2 != 0 else '0'
  codeword = ''.join(str(j) for j in A)

  print("Codeword: ", codeword+parity)

  return 0
  
def receiver(data_word, codeword):
  k = len(data_word)
  n = len(codeword)

  if n != k + 1:
    return "Discarded"

  parity = sum(codeword) % 2

  return ''.join(map(str, codeword[:-1])) if parity == 0 else "Discarded"

def main():
  A = input("Input A: ")
  A = [*A]
  data_word = [int(i) for i in A]
  
  B = input("Input B: ")
  B = [*B]
  codeword = [int(j) for j in B]

  sender(data_word)
  data = receiver(data_word, codeword)
  print("Data word: ", data)

main()
