import csv


def generate_command_hierarchy(reader) -> dict[str, list]:
    """
    Генерирует словарь с департаментами и их отделами

    :param reader: Reader, полученный из csv-файла
    :return: Словарь вида (Название департамента <-> Список его отделов)
    """
    departments_and_commands: dict[str, list] = {}
    for row in reader:
        cells = str.split(row[0], ";")

        if cells[1] == "Департамент":
            continue

        if cells[1] not in departments_and_commands:
            departments_and_commands[cells[1]] = [cells[2]]

        else:
            if cells[2] not in departments_and_commands[cells[1]]:
                departments_and_commands[cells[1]].append(cells[2])
    return departments_and_commands


def generate_report(reader) -> dict[str, list]:
    """
    Генерирует отчет по департаментам

    :param reader: Reader, полученный из csv-файла
    :return: Отчёт по данным из csv-файла
    """
    # Можно написать класс вместо этого словаря, но мы пока что их не проходили
    # Название <-> (численность, сумма зп, мин зп, макс зп, сред зп)
    report: dict[str, list] = {}
    for row in reader:
        cells = str.split(row[0], ";")

        if cells[1] == "Департамент":
            continue

        salary = int(cells[5])

        if cells[1] not in report:
            report[cells[1]] = [
                1,
                salary,
                salary,
                salary,
                0,
            ]

        else:
            add_person_to_report(report, cells, salary)

    calculate_avg_salary(report)
    return report


def add_person_to_report(
    report: dict[str, list], cells: list[str], salary: int | None = None
):
    """
    Добавление информации о работнике в словарь

    :param report: Отчёт по данным из csv-файла
    :param cells: Строка из считанного csv-файла
    :param salary: Зарплата из строки считанного файла
    """
    # В данной задаче такого не произойдет, но метод можно
    # будет переиспользовать в других местах,
    # если salary ещё не вычислена из строки
    if salary is None:
        salary = int(cells[5])

    report[cells[1]][0] += 1
    report[cells[1]][1] += salary
    if report[cells[1]][2] > salary:
        report[cells[1]][2] = salary
    elif report[cells[1]][3] < salary:
        report[cells[1]][3] = salary


def calculate_avg_salary(report: dict[str, list]):
    """
    Вычисляем среднюю зарплату в департаменте,
    зная сумму зп и количество человек в департаменте

    :param report: Отчёт по данным из csv-файла
    """
    for key in report.keys():
        report[key][4] = report[key][1] / report[key][0]
