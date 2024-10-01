
# def process_employee_data(input_string: str) -> str:
#     ages = []
#     for _ in [i.split(',') for i in input_string.split(";")]:
#         ages.append(_[1])
#     med = 0
#     ages.sort()
#     n = len(ages)
#     if n % 2 != 0:
#         med = ages[n // 2]
#     else:
#         middle1 = ages[n // 2 - 1]
#         middle2 = ages[n // 2]
#         med = (middle1 + middle2) / 2
#     return min(ages), med, max(ages)
#
# input_data = "Иван,28,Инженер;Олег,34,HR;Денис,45,Маркетинг;Анна,30,Инженер;Борис,24,HR"
# output_data = process_employee_data(input_data)
# print(output_data)


input_str = "5 10 15 20 18 22 25 30 28 35".split()
numbers = [int(x) for x in input_str]

sequences = []
current_sequence = []

for num in numbers:
    if not current_sequence or num > current_sequence[-1]:
        current_sequence.append(num)
    else:
        if len(current_sequence) > 1:
            sequences.append(current_sequence)
        current_sequence = [num]

if current_sequence:
    sequences.append(current_sequence)

if not sequences:
    print("Не обнаружено")
else:
    for seq in sequences:
        print(" ".join(map(str, seq)))

