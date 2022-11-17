print ('Что ты ищешь, хозяин? N - мощность алфавита; i - информационный вес символа; I - информационный обьем сообщения; K - число символов в сообщении; i2 - количество информации в одном символе; I2 - объем памяти, требуемый для хранения изображения; x— размер экрана по горизонтали; y — размер экрана по вертикале; i3 — глубина кодирования цвета или разрешение; K2 - количество оттенков\квантования звука; b - битовая глубина кодирования; N - количество произведенных измерений ; H - частота дискретизации; t - время ; A - обьем звуковой информации; D - частота дискретизации; T - время; I3 - разрядность регистра (разрешение); S - (S=1 для моно, S=2 для стерео, S=4 для квадро)')
p = str(input())
if p == 'N' :
    a= int(input('Введите N - информационный вес символа '))
    print( 2**a )
elif p == 'i':
    import math
    a= int(input('Введите i - мощьность алфавита в битах '))
    y = math.log2(a) 
    print(y)
elif p == 'I':
    a= int(input('Введите K - число символов в сообщении '))
    b = int(input('Введите i - количество информации в одном символе в битах '))
    print(a*b)
elif p == 'K':
    a= int(input('Введите I - информационный обьем сообщения '))
    b = int(input('Введите i - количество информации в одном символе в битах'))
    print( a/b )
elif p == 'i2':
    a= int(input('Введите I - информационный обьем сообщения '))
    b = int(input('Введите K - число символов в сообщении '))
    print( a / b )
elif p == 'I2':
    a= int(input('Введите i3 глубина цвета '))
    b = int(input('Введите x размер экрана по горизонтали '))
    с = int(input('Введите y размер экрана по вертикале '))
    print( a * b * с )
elif p == 'i3':
    a= int(input('Введите I2 информационный обьем видеопамяти  '))
    b = int(input('Введите x размер экрана по горизонтали '))
    с = int(input('Введите y размер экрана по вертикале '))
    print( a / (b * с) )
elif p == 'x':
    a= int(input('Введите I2 информационный обьем видеопамяти  '))
    b = int(input('Введите i3 глубину цвета '))
    с = int(input('Введите y размер экрана по вертикале '))
    print( a / (b * с) )
elif p == 'y':
    a= int(input('Введите I3 информационный обьем видеопамяти  '))
    b = int(input('Введите x размер экрана по горизонтали '))
    с = int(input('Введите i3 глубину цвета '))
    print( a / (b * с) )
elif p == 'K2' :
    a= int(input('Какая b - битовая глубина кодирования? '))
    print( 2**a )
elif p == 'b':
    import math
    a= int(input('Какое K2 - количество оттенков\квантования звука? '))
    y = math.log2(a) 
    print(y)
elif p == 'N':
    a= int(input('Введите H - частота дискретизации '))
    b = int(input('Введите t - время '))
    print(a*b)
elif p == 'H':
    a= int(input('Введите N - количество произведенных измерений '))
    b = int(input('Введите t - время '))
    print(a/b)
elif p == 't':
    a= int(input('Введите N - количество произведенных измерений '))
    b = int(input('Введите H - частота дискретизации '))
    print(a/b)
elif p == 'A' :
    D= int(input('Какая D частота дискретизации? '))
    T= int(input('Какое T время? '))
    I3= int(input('Какая I3 разрядность регистра(разрешение)? '))
    S= int(input('Моно - 1, стерео - 2? '))
    print( D*I3*T*S )
elif p == 'D':
    A= int(input('Какой A обьем звуковой информации? '))
    T= int(input('Какое T время? '))
    I3= int(input('Какая I3 разрядность регистра(разрешение)? '))
    S= int(input('Моно - 1, стерео - 2? '))
    print( A /(I3*T*S) )
elif p == 'T':
    A= int(input('Какой A обьем звуковой информации? '))
    D= int(input('Какая D частота дискретизации? '))
    I3= int(input('Какая I3 разрядность регистра(разрешение)? '))
    S= int(input('Моно - 1, стерео - 2? '))
    print( A/(I3*D*S) )
elif p == 'I3':
    A= int(input('Какой A обьем звуковой информации? '))
    D= int(input('Какая D частота дискретизации? '))
    T= int(input('Какое T время? '))
    S= int(input('Моно - 1, стерео - 2? '))
    print( A/(T*D*S) )
elif p == 'S':
    A= int(input('Какой A обьем звуковой информации? '))
    D= int(input('Какая D частота дискретизации? '))
    I3= int(input('Какая I3разрядность регистра(разрешение)? '))
    T= int(input('Какое T время? '))
    print( A/(I3*D*T) )
