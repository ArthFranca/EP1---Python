##Aluno: Arthur Franca
##Turma: 3 - A
##EP1 - Python
##Professor: Masanori


import time
import timeit
import random
k = 2000
while k:
    if k <= 32000:
        vetor = random.sample(range(0,k), k)
        k = k + 2000
    else:
        break
#Selecao##
def selection():
    print("Selection  |  Time(s)")
    vet = []
    n = 2000
    while n:
        if n > 32000:
            break
        else:
            while len(vet) <= n:
                r = random.randint(0, n)
                if r not in vet:
                    vet.append(r)
        inicio = time.time()
        if len(vet) <= 1:
            return vet
        resp = []
        while vet:
            m = min(vet)
            resp.append(m)
            vet.remove(m)
        fim = time.time()
        convert = (fim - inicio) / 0.1671
        print(f"{n}  |  {convert}")
        n = n + 2000
    return 

##Quick###
def quickSort():
    print("QuickSort")
    vet = []
    n = 2000
    while n:
        if n > 32000:
            break
        else:
            while len(vet) <= n:
                r = random.randint(0, n)
                if r not in vet:
                    vet.append(r)
            n = n + 2000
        result = []
        inicio = time.time()
        if len(vet) <= 1:
            return vet
        p = vet[0]
        same = [x for x in vet if x == p]
        bigger = [x for x in vet if x > p]
        lower =  [x for x in vet if x < p]
        fim = time.time()
        convert = (fim - inicio) / 0.1671
        print(f"{n}  |  {convert}")
    return 

##Merge##
def merge(esq, dire):
    inicio = time.time()
    array = []
    i, j = 0, 0
    while i < len(esq) and j < len(dire):
        if esq[i] <= dire[j]:
            array.append(esq[i])
            i += 1
        else:
            array.append(dire[j])
            j += 1
    array += esq[i:]
    array += dire[j:]
    fim = time.time()
    return array
    print((fim - inicio)/0.1671)
def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        esq = mergesort(v[:m])
        dire = mergesort(v[m:])
        return merge(esq, dire)
    



##Nativo##
def nativo():
    print("Nativo")
    vet = []
    ordenado = []
    n = 2000
    while n:
        if n > 32000:
            break
        else:
            while len(vet) <= n:
                r = random.randint(0, n)
                if r not in vet:
                    vet.append(r)
            n = n + 2000
        inicio = time.time()
        ordenado = sorted(vet)
        fim = time.time()
        convert = (fim - inicio) / 0.1671
        print(f"{n}  |  {convert}")
            
        
            

print(selection())
print(quickSort())
print(mergesort(vetor))
print(nativo())
   




















