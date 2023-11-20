## Issue 05

Содержимое файла `issue05.py` по директории 
```
..\omd\Python_Lecture08_Homework\issues\issue05
```
скопирован из файла `what_is_year_now.py` по директории 
```
..\omd\Python_Lecture08_Homework
```
и доработан обложением тестов с использованием `unittest`.

Результат запуска тестов и команды, а также результат вызов отчёта о покрытии находятся в файле `result.txt` по директории

```
..\omd\Python_Lecture08_Homework\issues\issue05
```
и разделенны между собой двумя чертами из тире.

Отчет о покрытии находится по директории
```
..\omd\Python_Lecture08_Homework\issues
```
и включает в себя файл `.coverage` и содержимое папки `htmlcov`.

### Запуск
Шаг 1: Чтобы запустить тесты необходимо, находясь в директории
```
..\omd\Python_Lecture08_Homework\issues
```

запустить директиву 
```
python -m unittest -v .\issue05\issue05.py
```

Шаг 2: Чтобы сформировать отчет необходимо, находясь по той же директории запустить директиву

```
python -m pytest -q .\issue05\issue05.py --cov, --cov-report html
```