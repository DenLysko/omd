def step2_umbrella():
    print(
        "Зонтик ☂️  спас уточку от дождя по пути в бар! \n Решение вязть его оказалось верным!"
    )


def step2_no_umbrella():
    print("По пути в бар была солнечная погода 🌞! \n Зонтик не понадобился!")


def step1():
    print("Утка-маляр 🦆 решила выпить зайти в бар. " "Взять ей зонтик? ☂️")
    option = ""
    options = {"да": True, "нет": False}
    while option not in options:
        print("Выберите: {}/{}".format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == "__main__":
    step1()
