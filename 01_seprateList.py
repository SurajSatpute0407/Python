list1 = []
while True:
    value = input('Enter value')
    if value.lower() == 'done':
        break
    try:
        if '.' in value:
            list1.append(float(value))
        else:
            list1.append(int(value))
    except:
        list1.append(value)

print(list1)

num_list = []
str_list = []
other = []

for i in list1:
    if type(i)==str:
        str_list.append(i)
    elif type(i)==int:
        num_list.append(i)
    else:
        other.append(i)

print('int list', num_list)
print('str list', str_list)
print('other list', other)