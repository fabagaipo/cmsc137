def to_bits(num):
  return bin(num)


def from_bits(bits):
  return int(bits, 2)


def checksum(data):
  result = 0
  for i in data:
    result += from_bits(i)

  result = to_bits(result)

  if len(result) > 8:
    x = len(result) - 8
    result = bin(int(result[0:x], 2) + int(result[x:], 2))[2:]

  complement = ''
  for i in result:
    if i == '1':
      complement += '0'
    else:
      complement += '1'

  return complement


def detect_errors(x):
    k = 8

    data = [x[i:i+k] for i in range(0, len(x), k)]

    complement = checksum(data)

    if "1" in complement:
        print('Checksum error detected')
    else:
        print('Accept data')


def main():
  # Sample Input
  """sample_data_stream = '10011001 11100010 00100100 10000100 11011010'"""

  # User Input
  data_stream = input("Data: ")
  data_stream = data_stream.replace(" ", "")

  detect_errors(data_stream)

main()
