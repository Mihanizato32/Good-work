my_dict={'Dima':1996,'Misha':1996,'Max':1995,'Denis':1994}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Dima'])
print('Not existing value: ', my_dict.get('Oleg'))
my_dict.update({'Vanya':2000,
                'Anton':2002})
my_dict.pop('Misha')
print('Modified dictionary:',my_dict)
my_set={1,2,3,4,5,1,2,3,4,5,2,2,(4,5,2)}
print('Set: ', my_set)
my_set.add('Glasha')
my_set.add(42.815)
my_set.discard(2)
print('Modifed set: ', my_set)

