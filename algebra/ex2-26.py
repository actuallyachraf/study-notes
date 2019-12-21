# "exercice 2.26 in shoup's introduction to number theory and algebra"
# find all elements of Z19 that have order 18
# 19 being a prime => all elements of Z19 have order Phi(19) = 18
# altough some elements will have an order k < 18 such as k | 18
# we solve this the naive way for clarity

def list_elements_only_18():

    orderk = []
    order18only = []
    for i in range(2,19):
        # loop trough the divisors of 18
        primitive_root = True
        for k in [2,3,6,9] :
            if i**k % 19 == 1:
                primitive_root = False
        if not primitive_root:
            orderk.append(i)
        if primitive_root :
            order18only.append(i)
    return (orderk,order18only)

if __name__ == '__main__':
    a,b = list_elements_only_18()
    print("Elements with order k (2,3,6,9)",a)
    print("Elements with order 18 ONLY",b)

