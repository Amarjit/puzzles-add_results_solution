find_number = int(input("Enter the number you would like to find solutions for: "))
max_solution_numbers = 4

solutions = []
for i in range(0, find_number):
    for j in range(0, find_number):
        result_1 = i + j
        result_2 = result_1 + j

        check_solution = result_2 + result_1

        if check_solution == find_number:
            found_solution = [i, j, result_1, result_2]

            solutions.append(found_solution)

if solutions:
    print("Solutions found for number :", find_number)
    print(*solutions, sep='\r\n')
else:
    print("No solutions exist for ", find_number)
