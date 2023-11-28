g = 10
def menergy(m, v , h):
    e1 = (m*v**2)/2
    e2 = m*g*h
    e3 = e1+e2
    return e3

a = menergy(10, 10, 15)
print(a)

