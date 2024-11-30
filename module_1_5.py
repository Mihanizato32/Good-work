immutable_var=1,2,3,4,True,'korteg'
print(immutable_var)
immutable_var[1]=200
##Кортеж относится к неизменяемым типам данных, используется в качестве хранилищ данных
print(immutable_var)
mutable_list=[1,2,3,4,5,6]
print(mutable_list)
mutable_list[3]=1000,'lol'
mutable_list[4]='Good'
print(mutable_list)