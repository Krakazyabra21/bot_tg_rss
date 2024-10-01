# def my(a, b=[]):
#     b.append(a)
#     return b
#
# print(my(1),my(2),my(3))
import re

# keys = ['a','b','c']
# values = ['x','y','z']
# idxs = enumerate(zip(keys,values))
#
# print(list(f'{i}: {k} = {v}' for i, (k, v) in idxs))

# phrase = "Data Science Is Awesome"
# result = [(i,char) for i, char in enumerate(phrase) if char.isupper()]
# print(result)

text = "ABCD123"


# print(re.match(r"^[A-Z]{3}\d{2,4][A-Z]?$", text) is not None)

# def process_number(n):
#     summa = sum([int(d) for d in n if d.isdigit()])
#     if summa > 100:
#         return "Превышено"
#     elif summa % 2 == 0:
#         return summa * 2
#
#
# print(process_number("1234"))


# class Item:
#     def __init__(self, date, product, quantity):
#         self.date = date
#         self.product = product
#         self.quantity = quantity
#
#     @property
#     def month(self):
#         months_dict = {
#             "01": "Январь",
#             "02": "Февраль",
#             "03": "Март",
#             "04": "Апрель",
#             "05": "Май",
#             "06": "Июнь",
#             "07": "Июль",
#             "08": "Август",
#             "09": "Сентябрь",
#             "10": "Октябрь",
#             "11": "Ноябрь",
#             "12": "Декабрь"
#         }
#         month = self.date.split('-')[1]
#         return months_dict.get(month, "Неизвестный месяц")
#
#
# def generate_monthly_report(data):
#     dict = {}
#     div_data = data.split(";")
#     for _ in div_data:
#         new_data = _.split(":")
#         new_item = Item(new_data[0], new_data[1], new_data[2])
#         # print(new_data)
#         # dict[f"{new_item.month}:"] = []
#         try:
#             dict[f"{new_item.month}:"] += (f"\n- {new_item.product}: {new_item.quantity}")
#         except:
#             dict[f"{new_item.month}:"] = f"\n- {new_item.product}: {new_item.quantity}"
#     return dict
#
#
# input_data = "2023-03-10:Карандаш:7;2023-04-01:Ручка:6;2023-04-15:Тетрадь:8"
# monthly_report_generator = generate_monthly_report(input_data)
# # print(monthly_report_generator)
# for report in monthly_report_generator:
#     print(report, monthly_report_generator[report])



