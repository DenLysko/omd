import csv


def get_reader():
    corp_summay_csv = open("Corp_Summary.csv", "r", encoding="utf-8")
    my_reader = csv.reader(corp_summay_csv)
    return my_reader


def write_report(report):
    report__csv = open("report.csv", "w", newline="")
    writer = csv.writer(report__csv)
    writer.writerows(report.items())
