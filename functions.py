# def hello_func():
#     pass  # to leave it blank


# print(hello_func())


# def func():
#     print("hello message")


# func()

# def func_n():
#     return ('HELLO FROM FUNC')


# print(func_n())


# arguments in function =======

# def hello_func(greeting, name='You'):
#     return '{}, {}.'.format(greeting, name)


# print(hello_func('hi', name="hrmn"))


# def hello(greeting, name):
#     return '{},{}'.format(greeting, name)


# print(hello('hello', 'Singh'))
# print(hello('hello', 'Harman'))
# print(hello('hello', 'Chetan'))


# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)


# courses = ['Math', 'Art']
# info = {'name': 'Hrmn', 'age': 25}

# # student_info('Math', 'Art', name="Hrmn", age='25')
# student_info(*courses, **info)


# # Number of days per month. First value placeholder for indexing purposes
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# def is_leap(year):
#     """Return True for leap years, False for non-leap years."""
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# def days_in_month(year, month):
#     """Return number of davs in that month in that year."""

#     if not 1 <= month <= 12:
#         return 'Invalid Month!'
#     if month == 2 and is_leap(year):
#         return 29

#     return month_days[month]


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid month'
    if month == 2 and leap_year(year):
        return 29

    return month_days[month]


print(leap_year(2020))
print(days_in_month(2017, 2))
