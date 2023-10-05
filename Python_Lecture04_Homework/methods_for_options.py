import csv


def generate_command_hierarchy(reader) -> None:
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


def generate_report(reader) -> None:
    # Можно написать класс для этого, но мы пока что их не проходили
    # Название <-> (численность, сумма зп, мин зп, макс зп, сред зп)
    primary_report: dict[str, list] = {}
    for row in reader:
        cells = str.split(row[0], ";")

        if cells[1] == "Департамент":
            continue

        salary = int(cells[5])

        if cells[1] not in primary_report:
            primary_report[cells[1]] = [
                1,
                salary,
                salary,
                salary,
                0,
            ]

        else:
            add_another_person_to_department(primary_report, cells, salary)

    calculate_avg_salary(primary_report)
    return primary_report


def add_another_person_to_department(primary_report: dict(), cells, salary: int):
    primary_report[cells[1]][0] += 1
    primary_report[cells[1]][1] += int(salary)
    if primary_report[cells[1]][2] > salary:
        primary_report[cells[1]][2] = salary
    elif primary_report[cells[1]][3] < salary:
        primary_report[cells[1]][3] = salary


def calculate_avg_salary(primary_report: dict()):
    for key, value in primary_report.items():
        primary_report[key][4] = primary_report[key][1] / primary_report[key][0]
