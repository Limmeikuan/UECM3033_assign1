import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(-x**3)*5*x**3, (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array([[3,1,4,5,6,0,0,2,0,0],[2,0,3,2,1,0,0,1,2,0],[4,3,5,4,3,1,0,0,3,1],[3,4,3,5,4,2,2,0,0,0],[1,9,3,2,3,0,1,3,3,0],[1,7,5,6,8,9,0,0,2,1],[0,3,2,4,5,9,1,7,0,0],[2,0,0,3,4,4,1,7,0,1],[0,0,0,0,4,3,0,6,3,9],[2,0,1,0,2,0,8,0,9,4]])
    b = np.array([9,8,8,3,2,1,7,2,8,2])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1306098
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
