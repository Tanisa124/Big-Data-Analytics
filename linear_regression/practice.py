import numpy as np
'''
Example 1:

Suppose we have the following dataset that shows the weight and height of seven individuals:

Y for Weights (lbs) and X for Height (inches)
'''
X = np.array([140, 155, 159, 179, 192, 200, 212])
Y = np.array([60, 62, 67, 70, 71, 72, 75])

def linear_regression(X, Y):

    #define importance params
    sum_y = sum(Y); sum_x = sum(X); sum_square_x = 0; sum_square_y = 0; sum_xy = 0

    for i in range(len(Y)):
        sum_square_x += X[i] ** 2
        sum_square_y += Y[i] ** 2
        sum_xy += X[i] * Y[i]

    # The formula to calculate b0 is: [(ΣY)(ΣX^2) – (ΣX)(ΣXY)]  /  [n(ΣX^2) – (ΣX)^2]

    b0 = ((sum_y * sum_square_x) - (sum_x * sum_xy)) / ((len(Y)*(sum_square_x)) - (sum_x ** 2))
    print(f'b0: {b0}')

    # The formula to calculate b1 is: [n(ΣXY) – (ΣX)(ΣY)]  /  [n(ΣX^2) – (ΣX)^2]

    b1 = ((len(Y) * sum_xy) - (sum_x * sum_y)) / ((len(Y) * sum_square_x) - (sum_x ** 2))
    print(f'b1: {b1}')

    print(f'Equation: Y = {b0} + {b1}X')

    print('------------------------------------------')
    
linear_regression(X, Y)

'''
Example 2

Your task is to find the equation of the straight line that fits the data best.

The following table represents the survey results from the 7 online stores.

the monthly e-commerce sales (Y) and online advertising costs (X)
'''

Y = np.array([368, 340, 665, 954, 331, 556, 376])
X = np.array([1.7, 1.5, 2.8, 5, 1.3, 2.2, 1.3])

linear_regression(X,Y)

'''
Example 3

You have to examine the relationship between the age and price for used cars sold in the last year by a car dealership company.
'''

X = np.array([4, 4, 5, 5, 7, 7, 8, 9, 10, 11, 12])
Y = np.array([6300, 5800, 5700, 4500, 4500, 4200, 4100, 3100, 2100, 2500, 2200])

linear_regression(X,Y)

'''
Example 4
'''
X = np.array([-2, 1, 3])
Y = np.array([-1, 1, 2])

linear_regression(X,Y)

'''
Example 5
'''
X = np.array([-1, 0, 1, 2])
Y = np.array([0, 2, 4, 5])

linear_regression(X,Y)

'''
Example 6
'''
X = np.array([0, 1, 2, 3, 4])
Y = np.array([2, 3, 5, 4, 6])

linear_regression(X,Y)






