def step2_umbrella():

    print(
        f"Зонтик ☂️  спас уточку от дождя по пути в бар! \n" 
        f"Решение вязть его оказалось верным!"
    )

def step2_no_umbrella():
    print(
        f"По пути в бар была солнечная погода 🌞! \n"
        f"Зонтик не понадобился!"
    )

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == "__main__":
    step1()
