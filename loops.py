nums = [1, 2, 3, 4, 5]

# for loop
# for num in nums:
#     print(num)

#  break
# for num in nums:
#     if num == 3:
#         print('Found!')
#         break
#     print(num)

# continue
# for num in nums:
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)


# loop with in the loop
# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

# for i in range(10): #it will start from 0 to 9 as index value for range is 10
#     print(i)

# for i in range(1, 11):
#     print(i)


# ###################### While Loop

x = 0
# while x < 10:
#     print(x)
#     x += 1  # if you dont increment it will go for infinite loop


while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
