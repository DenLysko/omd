import csv
import methods_for_options


def get_reader():
    corp_summay_csv = open("Corp_Summary.csv", "r", encoding="utf-8")
    my_reader = csv.reader(corp_summay_csv)
    return my_reader


def write_report(report):
    report__csv = open("report.csv", "w", newline="")
    writer = csv.writer(report__csv)
    writer.writerows(report.items())
import writer_and_reader


def step1() -> None:
    my_reader = get_reader()
    print(
        "Выберите пункт меню: \n 1. Вывести иерархию команд \n 2. Вывести сводный отчёт по департаментам \n 3. Cохранить сводный отчёт в виде csv-файла"
    )

    option = 0
    options = [1, 2, 3]
    while option not in options:
        option = int(input())

    if option == 1:
        departments_and_commands = methods_for_options.generate_command_hierarchy(
            my_reader
        )
        for key, value in departments_and_commands.items():
            print("{0}: {1}.".format(key, ", ".join(list(value))))
    elif option == 2:
        report = methods_for_options.generate_report(my_reader)
        for key, value in report.items():
            print(
                f'Департамент "{key}". Численность: {value[0]}, минимальная зарплата: {value[2]}, '
                f"максимальная зарплата: {value[3]}, средняя зарплата: {value[4]}"
            )
    elif option == 3:
        report = methods_for_options.generate_report(my_reader)
        write_report(report)


if __name__ == "__main__":
    step1()
