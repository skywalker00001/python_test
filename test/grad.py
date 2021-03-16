import numpy as np

def numerical_grad(f, x):
    #f是函数,x是向量
    fx = f(x)
    grads = np.zeros(x.shape)
    it =np.nditer(x, flags=["multi_index"], op_flags=["readwrite"])
    h = 0.00001

    while not it.finished():
        index = it.multi_index
        old_value = x[index]
        x[index] = x[index] + h
        fx_new = f(x)
        x[index] = old_value

        grad = (fx_new - fx )/ h
        grads[index] = grad
        it.iternext()

    return grads