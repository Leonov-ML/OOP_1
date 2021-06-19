class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
        and course in lecturer.courses_attached \
        and course in self.courses_in_progress \
        and grade > 0 and grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def get_avg_grades(self):
        if self.grades:
            sum_hw = 0
            count = 0
            for grades in self.grades.values():
                sum_hw += sum(grades)
                count += len(grades)
            return round(sum_hw / count, 2)
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за домашние задания: {self.get_avg_grades()}\n'\
              f'Курсы в процессе изучения: {self.courses_in_progress}\n'\
              f'Завершенные курсы: {self.finished_courses}\n'
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Нет такого студента!')
            return
        else:
            compare = self.get_avg_grades() < other_student.get_avg_grades()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{other_student.name} {other_student.surname} учится хуже, чем {self.name} {self.surname}')
        return compare

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.get_avg_lecture_grades()}\n'
        return res

    def get_avg_lecture_grades(self):
        if self.grades:
            lecture_grades = 0
            for grades in self.grades:
                lecture_grades += round(sum(self.grades) / len(self.grades), 2)
                return lecture_grades
        else:
            return 'Ошибка'

    def __lt__(self, other_lecture):
        if not isinstance(other_lecture, Lecturer):
            print('Это не лектор!')
            return
        else:
            compare = self.get_avg_lecture_grades() < other_lecture.get_avg_lecture_grades()
            if compare:
                print(f'Лучший лектор: {other_lecture.name} {other_lecture.surname}')
            else:
                print(f'Лучший лектор: {self.name} {self.surname}')
        return compare

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
        and course in self.courses_attached \
        and course in student.courses_in_progress \
        and grade >= 0 and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'
        return res

def get_avg_hw_grade(student_list, course):
    total_sum = 0
    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list), 2)

def get_avg_lect_grade(list_lect):
    total_sum = 0
    for lecturer in list_lect:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)
    return round(total_sum / len(list_lect), 2)


kira_utkina = Student('Kira', 'Utkina', 'female')
kira_utkina.finished_courses += ['Базы данных']
kira_utkina.finished_courses += ['Git']
kira_utkina.courses_in_progress += ['Python']

volodya_popov = Student('Vladimir', 'Popov', 'male')
volodya_popov.finished_courses += ['Базы данных']
volodya_popov.courses_in_progress += ['Python']
volodya_popov.courses_in_progress += ['Git']

lidia_koroleva = Lecturer('Lidia', 'Koroleva')
lidia_koroleva.courses_attached += ['Python']

alex_rumin = Lecturer('Alexy', 'Rumin')
alex_rumin.courses_attached += ['Git']

vladislav_andreev = Reviewer('Vladislav', 'Andreev')
vladislav_andreev.courses_attached += ['Python']

maksim_guravlev = Reviewer('Maksim', 'Guravlev')
maksim_guravlev.courses_attached += ['Git']

vladislav_andreev.rate_hw(kira_utkina, 'Python', 8)
vladislav_andreev.rate_hw(kira_utkina, 'Python', 6)
vladislav_andreev.rate_hw(kira_utkina, 'Python', 10)
vladislav_andreev.rate_hw(kira_utkina, 'Python', 7)

maksim_guravlev.rate_hw(volodya_popov, 'Git', 9)
maksim_guravlev.rate_hw(volodya_popov, 'Git', 7)
vladislav_andreev.rate_hw(volodya_popov, 'Python', 8)
vladislav_andreev.rate_hw(volodya_popov, 'Python', 5)

volodya_popov.rate_lecturers(lidia_koroleva, 'Python', 6)
kira_utkina.rate_lecturers(lidia_koroleva, 'Python', 10)
kira_utkina.rate_lecturers(lidia_koroleva, 'Python', 7)

volodya_popov.rate_lecturers(alex_rumin, 'Git', 9)
volodya_popov.rate_lecturers(alex_rumin, 'Git', 7)

print(kira_utkina)
print(volodya_popov)
print(lidia_koroleva)
print(alex_rumin)
print(vladislav_andreev)
print(maksim_guravlev)

print(kira_utkina.grades)
print(volodya_popov.grades)

print(lidia_koroleva.grades)
print(alex_rumin.grades)

print(kira_utkina < volodya_popov)

print(lidia_koroleva < alex_rumin)

print(get_avg_hw_grade([kira_utkina, volodya_popov], 'Python'))
print(get_avg_lect_grade([lidia_koroleva, alex_rumin]))