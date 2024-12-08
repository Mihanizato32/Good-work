first=int(input('Введите первое число:'))
second=int(input('Введите второе число:'))
third=int(input('Введите третье число:'))
if first==second==third:
    print('Ответ: 3')
elif first==second or first==third or second==third:
    print('Ответ: 2')
elif first!=second and first!=third and second!=third:
    print('Ответ: 0')