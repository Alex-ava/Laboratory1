numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index=numbers.index(None)
sum_of_numbers_missing=sum(num for num in numbers if num is not None)
count_of_numbers=len(numbers)
average_of_numbers=sum_of_numbers_missing/count_of_numbers
numbers[missing_index]=round(average_of_numbers,2)

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
