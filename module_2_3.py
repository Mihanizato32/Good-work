my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
положительные = []
index = 0
while index < len(my_list):
    if my_list[index] < 0:
        break
    положительные.append(my_list[index])
    index += 1
print(положительные)