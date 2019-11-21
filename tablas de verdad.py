double= [1,0]

# Tabla de verdad de or

print('p\tq\tr\tp or q or r')
print('-'*38)
for p in double:
    for q in double:
        for r in double:
            print(p, q, r, p or q or r, sep = '\t')

print()



int = [True,False]

# Tabla de verdad de AND

print('p\tq\tr\tp and q and r')
print('-'*38)
for p in int:
    for q in int:
        for r in int:
            print(p, q, r, p and q and r, sep = '\t')

print()


double = [1,0]

# Tabla de verdad de NOT

print('p\tnot p')
print('-'*13)
for p in double:
    print(p,not p, sep ='\t')





booleanos= [True,False]

# Tabla de verdad de bidireccional (<-->)

print('p\tq\tr\tp is q is r')
print('-'*38)
for p in booleanos:
    for q in booleanos:
        for r in booleanos:
            print(p, q, r, p is q is r, sep = '\t')

print()




int = [True,False]
# Tabla de verdad de Direccional (<-->)
print('p\tq\t p-->q')
print('-'*22)
for p in int:
    for q in int:
        print(p,q, not p or (q is p) , sep = '\t')