# Maksymalne koło wpisane

# Dane problemu

X = [ (2.0, 6.0), (2.0, 5.0), (3.0, 4.0), (4.0, 5.0), (5.0, 6.0), (6.0, 5.0), (7.0, 6.0) ]
Y = [ (3.0, 1.0), (5.0, 2.0), (6.0, 4.0), (7.0, 3.0), (8.0, 2.0), (8.0, 5.0) ]

# Rozwiązanie problemu

p = MixedIntegerLinearProgram()
var = p.new_variable(nonnegative=False) # Zakładamy, że wielokąt jest w pierwszej ćwiartce
 
a, b, d = var['a'], var['b'], var['d']

p.set_objective(d)

for x in X:
    p.add_constraint(a*x[0]+b+d <= x[1])
for x in Y:
    p.add_constraint(a*x[0]+b-d >= x[1])
p.add_constraint(d >= 0)
    
# Rozwiązanie problemu

print 'Optymalna wartość funkcji celu = ', p.solve()
print 'a=', p.get_values(a), ' b=', p.get_values(b), ' d=', p.get_values(d)

# Wizualizacja

def lin(z):
    return z*p.get_values(a)+p.get_values(b)

X.append(X[0])
Y.append(Y[0])
plot(lin,(0,10)) + list_plot(X, plotjoined=False, rgbcolor=(0, 0, 0)) + list_plot(Y, plotjoined=False, rgbcolor=(1, 0, 0))
