# Finite Computation From Boolean Circuits

**Algorithm** : An algorithm is a set of instructions to compute a 
function *F* on an input *x* such as x -> A -> F(x).

## Computing using AND OR NOT

We first define 3 simple functions that operate on bits.

- OR : {0,1}x{0,1} -> {0,1}
- AND : {0,1}x{0,1} -> {0,1}
- NOT : {0,1} -> {0,1}

We define *OR* as :

- OR(a,b) = 0 if a = b = 0 ; 1 otherwise
- AND(a,b) = 0 if a = b = 1 ; 1 otherwise 
- NOT(a) = 0 if a = 1; 1 if a = 0

- **Example** :

Let's define Maj(x,y,z) : {0,1}x{0,1}x{0,1} -> {0,1} that returns 1 if
at least two out of (x,y,z) are 1

- MAJ(x,y,z) = x AND y OR x AND z OR y AND z = OR(AND(x,y),OR(AND(y,z),AND(x,z)))

Let's define XOR(a,b) : {0,1}x{0,1} -> {0,1} such as XOR(a,b) = a + b mod 2
in other words XOR(a,b) = 0 if a = b ; 1 otherwise (note that it's different than OR : OR(1,1) = 1 and XOR(1,1) = 0)

- XOR(a,b) = 0 if a = b => AND(NOT(AND(a,b)),OR(a,b))

```python

def AND(a,b) : return a*b
def OR(a,b) : return 1-(1-a)*(1-b)
def NOT(a) : return 1 - a
def XOR(a,b) : return AND(NOT(AND(a,b)),OR(a,b))
```

```sh
> ['XOR(0,0)=0', 'XOR(0,1)=1', 'XOR(1,0)=1', 'XOR(1,1)=0']
```


