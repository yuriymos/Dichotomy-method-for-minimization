# Dichotomy method for minimization

# программа для поиска минимума многомерной функции
# методом покоординатного спуска, по каждой координате
# минимум определяется методом дихотомии
# для функции с пятью аргументами

def f(x):
    return 2*x[0]*x[0] + x[0] - 3 + 5*x[1]**4 - 3*x[1]\
           + x[2]*x[2] + 8*x[3]**4 + 5*x[3]\
           + 2*x[4]*x[4] - 2*x[4]

# допустимые диапазоны изменения величин
# по каждой координате

# x1min = -5 x1max = 5
# x2min = -2 x2max = 1
# x3min = -2 x3max = 5
# x4min = -7 x4max = 5
# x5min = -10 x5max = -2

X_range = [[-5, 5],
           [-2, 1],
           [2, 5],
           [-7, 5],
           [-10, -2]]
# начальная точка - средины допустимых интервалов
x = [(X_range[0][0]+X_range[0][1])/2,\
     (X_range[1][0]+X_range[1][1])/2,\
     (X_range[2][0]+X_range[2][1])/2,\
     (X_range[3][0]+X_range[3][1])/2,\
     (X_range[4][0]+X_range[4][1])/2]

# количество аргументов функции
N = 5

# параметры для метода оптимизации
k = 0.001
delta = 2*k

for j in range(0,2):
    X_range = [[-5, 5],
           [-2, 1],
           [2, 5],
           [-7, 5],
           [-10, -2]]
    for i in range(0,N):
        a = X_range[i][0]
        b = X_range[i][1]
        
        while(b-a > delta):
            r = k*(b-a)
            x[i] = (a+b)/2-r
            F1 = f(x)
            x[i] = (a+b)/2+r
            F2 = f(x)

            if(F1 > F2):
                a = (a+b)/2-r
            else:
                b = (a+b)/2+r

            X_range[i][0] = a
            X_range[i][1] = b

            # вывод результатов на каждой итеррации
            # для функции с пятью аргументами
            print(i,"{:.3}".format(x[0]),"{:.3}".format(x[1]),\
                  "{:.3}".format(x[2]),"{:.3}".format(x[3]),\
                  "{:.3}".format(x[4]),\
                  "{:.6}".format(F1),"{:.6}".format(F2))
    print(" ")
    print(j,X_range)

x_result = [[0]*2]*N
for i in range(0,N):
    x_result[i] = (X_range[i][0]+X_range[i][1])/2

F_result = f(x_result)
print(x_result,F_result)
