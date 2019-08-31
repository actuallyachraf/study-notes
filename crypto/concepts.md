# Concepts and Notations

The goal is to build a model for secure communications.
Alice and Bob wish to communicate over an unsecure channel,
Eve an eavesdropper can tap the channel and read all the messages.

- Plaintext : Messages to be sent the contain the information Alice wishes to transmit to Bob
- Ciphertext : The *encrypted* plaintext that goes trough the channel

- We define and formalize 3 important algorithms : **Gen**, **Enc**, **Dec** 
    - Gen : a key generation algorithm
    - Enc : an encryption algorithm that takes plaintexts and outputs ciphertexts.
    - Dec : a decryption algorithm that takes ciphertexts and outputs plaintexts.

- *Kerchoff Principle (1884)* : the only thing that should be assumed secret is the private key.

A result of *Kerchoff's* principle stipulates that **Gen** **can not** be *deterministic*
otherwise Eve can compute everything, thus **Gen** is a *randomized algorithm*.

## Private Key Encryption

A private key encryption scheme is a triplet of algorithms *(Gen,Enc,Dec)* such as :

- *Gen* : a randomized algorithm that returns *k* a *private key* in the keyspace.
- *Enc* : a potentially randomized algorithm that on an input *(k,m)* outputs *c* a ciphertext.
- *Dec* : a deterministic algorithm that on an input *(k,c)* outputs *m* the plaintext message.

- if *Enc* is deterministic it can be vulnerable to data leak attacks where an attacker can guess
a *m* based on patterns of *Enc(k,m)*.


## Examples :

### Caesar Shift

The caesar shift algorithm is a cyclic algorithms that shifts *m* based on *k in {0...25}*
we can formalize the Caesar cipher as such :

- *M* message space : {A...Z}
- *K* key space : {0...25}
- *Gen* : k <- K
- *Enc* : Enc(k,m1m2m3...mn) = c1c2...cn where ci = mi + k mod 26
- *Dec* : Dec(k,c1c2...cn) = m1m2...mn where mi = ci - k mod 26

Caesar cipher is easily broken trough bruteforce, try all k in {0...25} until the output is *readable*.

### Substitution Cipher

The substitution cipher samples k from the set of all permutations over {A...Z} Card(Keyspace) = 26! difficult to bruteforce.

- *M* : {A...Z}
- *K* : Perm({A...Z})
- *Enc* : Enc(k,m1m2...mn) = c1c2..cn where ci = k(mi).
- *Dec* : Dec(k,c1c2...cn) = m1m2..mn where mi = k^-1(mi), k^-1 is the inverse of k.

To attack the substitution cipher we can use frequency analysis of english letters.

## Modern Cryptography

The previous schemes were *artistic* in a sense there is no framework of *provable security* and are easily broken.
Modern cryptography moves to a more provably secure schemes based on *hard computation problems*.
Instead of creating ad-hoc schemes modern cryptography follows the following paradigms.

- Providing mathematical definitions of *security*.
- Providing precise *assumptions* of the *security* of the scheme "factoring is hard" is a probable assumption.
- Providing secuirt proofs relying on the *provable assumptions* of the scheme.

Modern cryptography moves away from the simple *secure communications model* to more developed use cases
such as *identity schemes*, *interactive and non-interactive proofs of zero-knowledge*, *multi-party computation*...
These use cases always aim to *hide* but *transmit information*.

- Encryption : *hides* from *eavesdroppers* to *transmit messages*.
- Zero Knowledge Proofs : Alice wishes to *prove that she knows x* to Bob without devulging *x* (the adversary is Bob) the
information is *knowledge of x*.
- Identity schemes: Alice wishes to prove *authenticate herself* as *owner of x* without maybe *disclosing x*.

### Examples

- Alice wants to prove to Bob that she knows two prime factors of *N* mainly *p* and *q* without disclosing both.
- Alice wants to prove to Bob that she is the creator of an unreleased book *B* she signs *B* and provides Bob with a *signature* and a *hash of B*.


