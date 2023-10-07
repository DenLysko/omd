import methods_for_options
import writer_and_reader


def run() -> None:
    my_reader = writer_and_reader.get_reader()
    option = get_option_and_reader()

    match option:
        case 1:
            departments_and_commands = methods_for_options.generate_command_hierarchy(
                my_reader
            )
            for key, value in departments_and_commands.items():
                print("{0}: {1}.".format(key, ", ".join(list(value))))
        case 2:
            report = methods_for_options.generate_report(my_reader)
            for key, value in report.items():
                # Не было указаний до какого числа необходимо огруглять среднюю зарплату,
                # поэтому вывожу число полностью. Но всегда можно написать round(value[4], 2), например
                print(
                    f'Департамент "{key}". Численность: {value[0]}, минимальная зарплата: {value[2]}, '
                    f"максимальная зарплата: {value[3]}, средняя зарплата: {value[4]}"
                )

        case 3:
            report = methods_for_options.generate_report(my_reader)
            writer_and_reader.write_report(report)


def get_option_and_reader():
    """ """
    print(
        "Выберите пункт меню: \n 1. Вывести иерархию команд \n"
        + "2. Вывести сводный отчёт по департаментам \n 3. Cохранить сводный отчёт в виде csv-файла"
    )

    option = 0
    options = [1, 2, 3]
    while option not in options:
        option = int(input())
    return option


if __name__ == "__main__":
    run()
