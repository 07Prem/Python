import sympy as sp

n, z, a = sp.symbols('n z a')

x_n = a**n

X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = a^n u[n]:")
sp.pprint(X_z, use_unicode=True)


