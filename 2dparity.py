def two_dimensional_parity_check(array):
    error_count = 0

    row_sums = [sum(row) for row in array]
    
    for row_sum in row_sums:
      if row_sum % 2 != 0:
        error_count += 1

    col_sums = [sum(array[i][j] for i in range(len(array))) for j in range(len(array[0]))]
    
    for col_sum in col_sums:
      if col_sum % 2 != 0:
        error_count += 1

    return error_count


def main():
    # Sample Input
    data = [[1, 0, 1, 1, 0, 0, 1, 1, 1], 
            [1, 0, 1, 0, 1, 0, 1, 1, 1], 
            [0, 1, 0, 1, 1, 0, 1, 0, 0], 
            [1, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 0, 1, 0, 1, 1, 1, 1]]

    error_count = two_dimensional_parity_check(data)
    print("Error count:", error_count)
  
    # For User Input
    input_data = input("Data: ")

    bits = input_data.split()
    array = [[int(element) for element in bit] for bit in bits]

    error_count = two_dimensional_parity_check(array)
    print("Error count:", error_count)

main()
