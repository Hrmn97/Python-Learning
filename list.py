courses = ['History', 'Maths', 'Physcis', 'CompSci']
courses_2 = ['Art', 'Education']
nums = [1, 5, 3, 2, 6, 9, 12, 23, 4]


# convert list into string and then string to list again
#course_str = ', '.join(courses)
#new_str = course_str.split(', ')
# print(course_str)
# print(new_str)

# looping alongside index value
# for index, variable in enumerate(courses, start=1):
#    print(index, variable)


# looping items
# for variable in courses:
#   print(variable)


# to check that certain value exist in our list
#print('Maths' in courses)


# find index of the value
# print(courses.index('Maths'))


# print(courses[-4])
# negative index access list from backside


# print(courses[0:3])
# range of list that exclude the value after colon

# add item to end
# courses.append('Art')


# insert the value at particular place
#courses.insert(0, 'Art')


# add another list to existing list at last
# courses.extend(courses_2)


# remove value
# courses.remove('Maths')


# pop last value from list
#popped = courses.pop()
# print(courses)
# print(popped)


# reverse
# courses.reverse()


# sorting
# nums.sort()
# print(nums)

# sort in reverse order
# nums.sort(reverse=True)
# print(nums)


# sorted function
#sorted_course = sorted(courses)
# print(sorted_course)
# print(courses)


# get min and max from nums and get sum of the value in list
# print(min(nums))
# print(max(nums))
# print(sum(nums))
