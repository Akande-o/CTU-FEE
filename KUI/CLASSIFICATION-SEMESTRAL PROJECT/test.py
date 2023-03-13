import csv
dict_test = {"a":5, "b":10, "c":15}
with open("classification.dsv", "w", newline="") as csv_output:
        writer = csv.writer(csv_output, delimiter=":")
        writer.writerows(dict_test.items())