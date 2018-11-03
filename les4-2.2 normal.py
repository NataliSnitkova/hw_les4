# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

import re

string = 'GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec'
m = '[a-z][a-z][A-Z]+[A-Z][A-Z]'
sp1 = re.findall('[a-z][a-z][A-Z]+[A-Z][A-Z]', string)
def my_del(n):
    a = str(n[2:-2])
    return(a)
sp2 = []
i = 0
for old_el in sp1:
    old_el = sp1[i]
    sp2.append(my_del(old_el))
    i+=1
print(sp2)




