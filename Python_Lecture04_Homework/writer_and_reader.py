import csv


def get_reader():
    """
    Вкладываем информацию о csv-файле в reader
    """
    corp_summay_csv = open("Corp_Summary.csv", "r", encoding="utf-8")
    my_reader = csv.reader(corp_summay_csv)
    return my_reader


def write_report(report: dict[str, list]):
    """
    Выводим отчёт в csv-файл

    :param report: Отчёт по данным из csv-файла
    """
    report_csv = open("report.csv", "w", newline="")
    writer = csv.writer(report_csv)
    writer.writerows(format_report_for_csv(report))
    print("Отчёт создан в файле report.csv текущей директории")


def format_report_for_csv(report: dict[str, list]) -> list[list[str]]:
    """
    Изменение отчета на другую структуру данных
    для более правильно отображения в csv-файле

    :param report: Изначальный отчет
    :return: Преобразованный отчет для csv-файла
    """
    formated_report: list[list[str]] = []
    formated_report.append(generate_first_row())
    for key, value in report.items():
        formated_report.append(generate_row_for_csv(key, value))
    return formated_report


def generate_row_for_csv(key: str, value: list[str]) -> list[str]:
    """
    Перевод пары из словаря с список для отображения в csv-файле

    :param key: Ключ из словаря
    :param value: Значение из словаря
    :return: Строка для csv-файла
    """
    another_row: list[str] = []
    another_row.append(key)
    another_row.append(value[0])
    another_row.append(value[2])
    another_row.append(value[3])
    another_row.append(value[4])
    return another_row


def generate_first_row() -> list[str]:
    """
    Генерация названий колонок для csv-файла

    :return Строка c названием колонок для csv-файла:
    """
    first_row: list[str] = []
    first_row.append("Департамент")
    first_row.append("Численность")
    first_row.append("Минимальная зарплата")
    first_row.append("Максимальная зарплата")
    first_row.append("Средняя зарплата")
    return first_row
