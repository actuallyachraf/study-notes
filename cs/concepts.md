# Concepts and Notations

## Representations

Numbers can be represnted as strings of bits {0,1}  : n -> bitstring s
- The leftmost bit in s is the MSB
- The right most bit in s is the LSB

Converting a natural number to its bit representation can be done using the recursive function :

```ocaml
let NtS n =
    match n with
    | 0 -> 0 
    | 1 -> 1
    | n -> string_of_int(floor(n/2)*parity(n)) + ""
```

A python implementation can be written as

```python
def NtS(n):
    if n < 1 : return ""
    return NtS(floor(n/2)) + str(n%2)
```

Representing integers adds a sign bit to the left making the sign bit the MSB.
We can define it as such

```python
def ZtS(m):
    if m >= 0:
        return '0'+NtS(m)
    # -m gives the positive rep of m
    return '1'+NtS(-m) 
```

The sign magnitude representation is forgone for the two-complement in practice.
The Two Complement representation can be defined as :
For an integer k in the set -2^n...2^n-1 :

ZtSn(k) :

- NtS(n+1)(k) if 0 < k < 2^n - 1
- NtS(n+1)(2^n+1 + k) if -2^n < k < 0

Where NtS(n+1)(k) is the standard representation of using a n+1-length string.
Padded with leading zeroes if needed.
For example :
- NtS(4)(1) = 0001
- NtS(8)(120) = (0)1111000 // () denotes the pad

```python
def ZtStwo(l,k):
    rep = ZtS(k)
    if len(rep)==l:
        return rep
    return (l - len(rep))*'0' + rep
```

Representing rational numbers defines a new alphabet {0,1,||}
the || represents the fraction symbol /.
For example -5/8 can be represented as a pair of strings 
denoting the (numerator,denominator) the pair of strings can
be then separated by ||.

- -5/8 = (1101,01000)
Now to map this to a bit string we can specify || = 01
to avoid confusion we define a new mapping :

- map 0 -> 00 1 -> 11 || -> 01

Thus 

- (1101,01000) = (11110011010011000000)

Parsing this is easy, we split each couple of bits and use the inverse mappings
respective to new alphabet.
This representations allows us to go back to the simpler alphabet {0,1}.
Padding allows us to split the string to couples

### Prefix Free Encoding

We generalize this "hack" to the prefix-free encoding mechanism.
Given that 01 in a even length representation doesn't map to 0 or 1
this means that 01 can't be a prefix to 1 or 0.
Thus encoding rationals by mapping 0 to 00 and 1 to 11 and || to 01 we
effectively have an always-correct encoding for rationals.


- Proof by Python in page 102 in the [textbook](introtcs.org)

We can use prefix free encoding to encode lists which are the most
primitive object to *bundle* things.

### Representing Letters and Text

The ISO standards of letters and texts are ASCII (128 letters and symbols to 7-bit strings).
UTF-8 expands on this to 8-bit to 32-bit length strings (up to 128,000 symbols).

To view this we can use the following program to probe how values are stored
in memory by leveraging C language ability (or handicap) to access memory .

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *bytes(void *p,int n){
  int i;
  int j;
  char *a = (char *) p;
  char *s = malloc(9*n+2);
  s[9*n] = '\n';
  s[9*n+1] = 0;


  j = 0;
  for(i=0;i< n*8;i++){
    s[j] = a[i/8] & (128 >> (i % 8)) ? '1' : '0';
    if (i% 8 == 7) { s[++j] = ' '; }
    ++j;
  }
  return s;
}

void printint(int a) {
  printf("%-8s %-5d: %s", "int", a, bytes(&a,sizeof(int)));
}

void printlong(long a) {
  printf("%-8s %-5d: %s", "long", a, bytes(&a,sizeof(long)));
}


void printstring(char *s) {
  printf("%-8s %-5s: %s", "string", s, bytes(s,strlen(s)+1));
}


void printfloat(float f) {
  printf("%-8s %-5.1f: %s", "float", f, bytes(&f,sizeof(float)));
}

void printdouble(double f) {
  printf("%-8s %-5.1f: %s", "double", f, bytes(&f,sizeof(double)));
}



int main(void) {
  
  printint(2);
  printint(4);
  printint(513);
  printlong(513);
  

  printint(-1);

  printint(-2);

  printstring("Hello");

  printstring("abcd");

  printfloat(33);
  printfloat(66);
  printfloat(132);
  printdouble(132);

  
  return 0;
}
```

Compiling this and executing gives the following output.
We can remark that strings end with a 0 byte (8-bit all 0 string) that represents the end of a string.

```sh
> gcc prober.c -o prober

int      2    : 00000010 00000000 00000000 00000000 
int      4    : 00000100 00000000 00000000 00000000 
int      513  : 00000001 00000010 00000000 00000000 
long     513  : 00000001 00000010 00000000 00000000 00000000 00000000 00000000 00000000 
int      -1   : 11111111 11111111 11111111 11111111 
int      -2   : 11111110 11111111 11111111 11111111 
string   Hello: 01001000 01100101 01101100 01101100 01101111 00000000 
string   abcd : 01100001 01100010 01100011 01100100 00000000 
float    33.0 : 00000000 00000000 00000100 01000010 
float    66.0 : 00000000 00000000 10000100 01000010 
float    132.0: 00000000 00000000 00000100 01000011 
double   132.0: 00000000 00000000 00000000 00000000 00000000 10000000 01100000 01000000 
```

### Representing Vectors, Matrices, Tensors

Once we can represent numbers and list of numbers we can represent vectors.
Once we have vectors we can represent matrices (list of (list of numbers)).
Once we have matrices we have tensors (list of (list of (list of numbers)))

A pixel in grayscale image is a 1 byte number, each color is red/green/blue
can be represented using a 3 numbers list thus a pixel is a list of 3 lists.
An image of n pixels is a list of n 3 lists and a video is a list of images.

### Representing Graphs, Trees

Graphs can be represented using either an adjacency list (a list of lists of neighbors)
Or an adjancency matrix (edge i,j -> 0 or 1) for non weighted graphs x for weighted ones.
Each representation has a respective memory footprint choosing each depends on tasks ...

Trees can be represented using nested lists similarly to how you would construct one
in Lisp or OCaml (using Cons construction).

```lisp
(1
	(2,3),4 
	(5,(6,7),8,(9,10))
)
```

The tree is rooted at one has two child nodes (2,3) and 4 that have two childs 5,8 each have (6,7) (9,10)
as children.


# End Notes

We should always distinguish between

- *functions* and *programs*
- *specification* and *implementation*
- *circuit* and *machine*

A function is a set of inputs and outputs the mapping is *how we compute it* using a *program*.
A *program* **computes** a *function*.

- A computational tasks is the task of *computing a function F : {0,1}^n -> {0,1}^n*
- Our aim is to be able to 
	- Define whether F is *computable*
	- Define whether an *efficient* algorithm for *computing* F exists.
	- Define whether a *hard to compute* function can be used for other applications.
	- Finding or giving bounds on the *best algorithm* to compute such F.
	- Can we show equivalences between F and F' .

