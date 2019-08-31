# Knowledge, Zero-knowledge and interactive proofs


## A Short Story

What is *knowledge* ?, knowledge is information about *how* to complete a specific task.
In a sense, knowledge is an artifact that when received can let you accomplish a task
you couldn't accomplish before.

> Knowledge is an update of information state.

Suppose you don't know how to add numbers, you *know* the arabic numerals and
that you can count.But if I give you two numerals you *couldn't* add them.
As you're sitting there in front of your math test about to fail,
I appear in front of you wearing a cloak and tell you the following :

> To sum two numerals, make a line for each numeral and count all your lines.

The test shows 7 + 8 so you go trough the following step :

- You scratch 7 lines on a piece of paper
- You scratch 8 more lines on a piece of paper
- YOu start counting how many lines you have

While addition is basically counting, you *didn't know that* 
the + symbol looked like a summoning symbol for yellow dancing devils.

**The new knowledge you acquired was addition (+) = counting how many lines both numeral make**

## Formally

Given a one way function *f*, Alice tells Bob "the preimage of the preimage of (n times) 0".
f^-1(f^-1(...(f^-1(0)))) = x, while this message is deterministic Bob had no way of knowing
x unless he did the computation himself which as we showed earlier is *hard*.

> The preimage of 1 by g is 36 all you know is that g^-1(1) = 36 and g(36) = 1

I'd have to also tell you that g(x) = x^7 mod 17

The amount of knowledge conveyed in a message can be quantified by considering the size
and running time of a Turing machine to produce it.

Given any algorithm is considered efficient if it runs in polynomial time, Bob
can generate it for himself thus it *conveys* no *knowledge*.

Suppose Alice samples from a randomness source to provide Bob with a message *m*, then
the amount of knowledge in a *random message* is equivalent to the complexity of
a turing machines that samples from a *computationally indistinguishable* distribution.

> two families of distributions are computationally indistinguishable if no efficient algorithm
  can tell the difference between them except with small probability. 
