# Mathematics and Background

## One way functions

A One way function is one that is hard to find its inverse.

```python
p = 48611
q = 53993
def modular_cube_root(x,p,q):
   n = p*q
    if x > n :
        return -1
    r = x**3 % n

    return r
```

The function we just defined is an example of a one way function, while mathematically the inverse
can be define, It is computationally infeasable to compute it given p,q unknown.
If p and q are known the problem above *modular cube root* can be easily computed which is why RSA's security
is as hard as finding the prime factors.


## Trapdoor functions

A trapdoor function, is a function who's inverse is easily computable given extra information.
As an example the modular cube root is a trap door, since given p and q we can find x.


## Permutation

A Permutation is a *bijection* from a set to itself, such as for each x in S, p(x) is also in s.
The identity function is a permutation.

```python

table = [5,3,1,4,2]

set = [1,2,3,4,5]

def permute(x):
    # use -1 to access by index
    return table[x-1]

```


