import numpy as np

""" Реализация градиентного спуска с 2 переменными """

def numerical_derivative_2d(func, epsilon):

    def grad_func(x):
    
        grad = np.array([(func(np.array([x[0] + epsilon, x[1]])) - func(x)) / epsilon,
                         (func(np.array([x[0], x[1] + epsilon])) - func(x)) / epsilon])
        return grad

    return grad_func


def grad_descent_2d(func, low=-5, high=5, epoch=5):

    eps = 10**(-10)
    alpha0 = 1
    delta = 0.95
    e = 0.1
    best_estimate = []
    
    deriv = numerical_derivative_2d(func, 10**(-10))

    for i in range(epoch):
        
        est = np.random.uniform(low, high, size=2)

        n = 0
        prev_est = est + 10
        alpha = alpha0

        while (abs(func(est) - func(prev_est)) > eps and n < 10**4):
            n += 1
        
            while ( func(est - alpha * deriv(est)) > (func(est) - e * alpha * np.linalg.norm(deriv(est))**2 ) ):
                alpha *= delta

            prev_est = est
            est = est - alpha * deriv(est)
            alpha = alpha0

        best_estimate.append(est)
        
    func_estimate = []
    
    for i in range(epoch):
        func_estimate.append(func(best_estimate[i]))
        
    return best_estimate[np.argmin(func_estimate)]

def func(x):
    return 6 * x[0]**6 + 2 * x[0]**4 * x[1]**2 + 10 * x[0]**2 + 6 * x[0] * x[1] + 10 * x[1]**2 - 6 * x[0] + 4

min_point = grad_descent_2d(func)
print(f'Точка минимума: ({min_point[0]}; {min_point[1]})')

print(f'Минимальное значение функции: {func(min_point)}')
