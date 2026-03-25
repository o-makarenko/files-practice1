# import csv
# total = 0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = list(csv.DictReader(file))
#     prices = []
#     quant = []
#     for row in reader:
#         if row == "in_stock":
#             prices.append(float(row[5]))
#             total += float(row[5])
#         print(f"{row["Index"]} {row["Name"]}")
#     print(f"The total value is {total}")
#     print(f"The average price is {total / len(prices)}, max value is {max(prices)}")


# import json
# with open("data/data.json", "r", encoding="utf-8") as file:
#     user_data = json.load(file)
#     total = 0
#     for el in user_data:
#         if el["state"]=='California':
#             total += 1
#
# print(f"The amount of californians {total}, out of {len(user_data)}")
#
# import json
#
# with open("data/data.json", "r", encoding="utf-8") as file,\
#     open("data/data-c.json", "w", encoding="utf-8") as dest:
#     user_data = json.load(file)
#     total = 0
#     list_ca = [i for i in user_data if i['state']=='California']
#     json.dump(list_ca, dest, indent=4)
# print(f"The amount of californians {total}, out of {len(user_data)}")
# print(list_ca)
