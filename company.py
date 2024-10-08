"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]


def printing(departments):
    for department in departments:
        print(department["title"])
        for employers in department["employers"]:
            print(employers['first_name'], employers['last_name'], department["title"])


def get_employer_salary(departments):
    for department in departments:
        for employers in department["employers"]:
            if employers["salary_rub"] > 100000:
                print(f"Name of employee who has salary 100k: {employers['first_name']} {employers['last_name']}")
            elif employers["salary_rub"] < 80000:
                print(f"Position with salary less than 80k:{employers['position']}")


def printing_total_salary_expenses(departments):
    total_expenses = 0
    for department in departments:
        for employers in department["employers"]:
            total_expenses += employers["salary_rub"]
    print(f"Departments total expenses: {total_expenses}")    

#Второй уровень

def printing_min_max_average_dep(departments):
    total_salary = 0
    for department in departments:
        min_salary = float('inf')
        max_salary = 0
        for employers in department["employers"]:
            if employers["salary_rub"] < min_salary:
                min_salary = employers["salary_rub"]
                min_department = department["title"]
            elif employers["salary_rub"] > max_salary:
                max_salary = employers["salary_rub"]
        total_salary += employers["salary_rub"]
        average_salary = total_salary / len(department["employers"])
        print(f"{department['title']} has salary min: {min_salary}, average: {average_salary}, max: {max_salary}")


def printing_average_salary(departments):
    total_salary = 0
    count_employers = 0
    for department in departments:
        for employers in department["employers"]:
            total_salary += employers["salary_rub"]
            count_employers += 1
    print(f"average salary: {total_salary/count_employers}")
            

if __name__ == "__main__":
    printing(departments)
    get_employer_salary(departments)
    printing_total_salary_expenses(departments)
    printing_min_max_average_dep(departments)
    printing_average_salary(departments)