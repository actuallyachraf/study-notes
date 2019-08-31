# Computational Hardness

## Notations and Concepts

We start by *formalizing* notions of algorithm, running time and deterministic computation.

- Algorithm : 

A deterministic Turing machines whose inputs and outputs are over the binary alphabet {0,1} such as A *computes* a
function *F*.

- Running Time :

An algorithm *A* is said to run in time *T(n)* for x in {0,1} if A(x) halts within T(x) steps, A is said to
be polynominal if there exists a constant *c* such as T(n) = n^c

- Deterministic Computation :

*A* is said to compute *F* if for all x in {0,1} A(x) = F(x).
A(x) *outputs* F(x).

An algorithm is considered **efficient** if it runs in *Polynomial Time*.

### Computationally Hard Problems

While *computable problems* can be classified in *complexity classes* based on known or believed assumptions,
a problem is called *hard* if there exists no *efficient algorithm* to compute it.

- Halting Problem : Given a description of a turning machine M determine whether M halts on an empty output.

- Satisfiability : The SAT problem is to determine whether a boolean formula has a satisfying assumption,
SAT is *conjectured* not to be solvable in polynomial time.

### Randomized Algorithms

A Randomized algorithm can be thought of as an algorithm with access to *randomness* such as a coin-flip machine or temperature or any 
kind of data that is *random* in a sense.

Formally, a randomaized algorithm or Probabilistic Polynomial Time Turing Machine is a turing machine with an extra *random tape* such
as each bit of this tape is uniformly and independantly choosen.

### One Way Functions

A One way functions is a function X -> Y such as it's *hard* to invert.
In our encryption example we had two main assumptions :

- Given (m,k) it's easy to compute c.
- Given (c) it's hard to compute m and k.

The two assumptions require *Enc* and *Dec* to be *hard to invert* i.e **one way functions**.

- *Worst Case one way functions* : A function *f* is *worst-case one-way* if : 
    - Easy to compute (there exists a PPT *C* that computes f(x) for x in {0,1})
    - Hard to invert for *there is no A such as* all x in {0,1} Pr[A(f(x)) in f-1(f(x))] = 1

- *Strong Case one way functions* : Given an negligible function e(n) *f* is *strong case one-way* if :
    - Easy to to compute
    - Pr[A(f(x))] < e(n) (the probability of finding x for a random y = f(x) is negligeable)


One way functions such as *hash functions* fit both assumptions. 
Modern hash functions have concrete security assumptions that make them *strong case* .

### Factoring, Primes and Multiplication

The multiplication function is one way, but it isn't strong.

- F(x,y) = 1 if x = 1 and y = 1 | x.y otherwise

But it can be easy to invert, if x is even then the output is even if we pick (x,y) uniformally this happens 3/4 times.

Thus the following attack will succeed 3/4 times :

- A(z) = (2,z/2) if z is even | 0 otherwise

The issue here is that we don't have to find *exactly* x and y we only need to find x such as f(x) = y (that's the one-way assumption).

There is a case where this inversion becomes *hard* if p,q are primes.

Let Pn = {q | q is prime and q < 2^n}

Then for every adversary *A* we have the following assumption :

- Pr[p in Pn, q in Pn | N <- p.q : A(N) in {p,q}] < e(n)

In simpler terms given N (big enough) the probability of finding p and q (primes) such as N <- p.q is negligeable.


## Computational Number Theory 

We list here some *efficient algorithms* for number theory computations.

- Extended Euclidean GCD : the following compute x,y such as ax+by = 1

```python
def extended_euclid(a,b):
    if a % b == 0 :
        return (0,1)
    else :
        (x,y) = extended_euclid(b,a % b)
        return (y,x-y*(floor(a/b)))
```

- Modular Exponentiation : a^x mod N

```python
def modular_exp(a,x,N):
    r = 1
    while x > 0 :
        if x % 2 == 0:
            r = r*a % N
        x = floor(x/2)
        a = a*a % N
   return r
```

## One Way Functions from hard problems

We showed how prime multiplication can define a collection of *one way functions* such as for p,q primes f(p,q) = p.q is a 
one way function we now present few other examples that stem from number theoretic or group theoretic hard problems.

### Group Theory

This a quick passover of some background on Group Theory

- A Group **G** is a set with a binary operation * : G x G -> G such as the following assumptions are verified :
    - Closure : a * b is in **G**
    - Identity : there exists *I* in **G** such as *I* * a = a
    - Associativity
    - Inverse : there exists *b* in **G** such as b * a = a * b = *I*

- Z^n is a group : Integers Modulo N is the set of integers {0...N-1} (Multiplicative with . Additive with +)

- if **G** is a multiplicative group then *g* is a generator if G = {g^1,g^2,g^3...}

### Discrete Logarithm

The discrete logarithm problem in the multiplicative group Z^p where p is a prime consists of 
given (p,g,y) find x such as g^x = y mod p.

In some cases the problem is easy but if *g* is a *generator* the problem is *believed* to be **hard**.

Given the following assumption

- Pr[q <- Pn;g <- Gen(G);x <- Z^q : A(g^x) = x ] < e(n)

Let DL = {f : D -> R} such as :

- D = {x | x in Zp}
- R = Gp
- f(p,g,x) = g^x mod p

DL is then a *collection* of *one way functions* .

### RSA

The RSA assumption is more complicated than the factoring one we made above :
but RSA => Factoring, the converse is not known.

- Given (N,e,y) : Pr[x | x^e = y mod N] < e(n)

N is the product of two large primes and e is called the moduli, one more assumption is
that gcd(e,phi(N)) = 1.

- phi(p) the *Euler totient function* .


These set of notes are from [Chapter 2 of Bellare and Shelat](https://www.cs.cornell.edu/courses/cs4830/2010fa/lecnotes.pdf)
