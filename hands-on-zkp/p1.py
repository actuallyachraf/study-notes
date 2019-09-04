"""

    Title : Zero Knowledge Proofs for the partition problem
    
    Problem : Given a sequence a0a1a2...an can one partition
    this sequence to two subsets that sum up to the same number.

    Complexity : NP-Complete with a pseudo-polynomial algorithm.

    Method : Our goal is to generate a proof of knowledge of a list m
    of 1s and -1s such <l,m> = 0.
    1 : designates the left subset
    -1 : designates the right subset

    Example : Given instance l = [4,11,8,1] then a solution is
    m = [1,-1,1,-1]

    Our goal is to build a zero-knowledge proof for knowing m 
    without revealing it.
    
    
"""

import random
import hashlib
from math import log2,ceil

def hash(s) :
    return hashlib.sha256(s.encode()).hexdigest()

class MerkleTree:

    def __init__(self,data):
        self.data = data
        next_pow_of_2 = int(2**ceil(log2(len(data))))
        self.data.extend([0] * (next_pow_of_2 - len(data)))
        self.tree = ["" for x in self.data] + [hash(str(x)) for x in self.data]

        for i in range(len(self.data)-1,0,-1):
            self.tree[i] = hash(self.tree[i * 2] + self.tree[i * 2 + 1])

    def root(self):
        return self.tree[1]

    def get(self,id):
        val = self.tree[id]
        ap  = []
        id = id + len(self.data)
        while id > 1:
            ap += [self.tree[id ^ 1]]
            id = id // 2
        return val,ap

def verify_ap(root,size,id,val,path):
    cur = hash(str(val))
    tree_node_id = id + int(2**ceil(log2(size)))
    for sibling in path:
        assert tree_node_id > 1
        if tree_node_id % 2 == 0:
            cur = hash(cur + sibling)
        else:
            cur = hash(sibling + cur)
        tree_node_id = tree_node_id // 2
    assert tree_node_id == 1
    return root == cur
    
    
class ZkMerkleTree:
    """
    A Zero Knowledge Merkle tree implementation using SHA256
    For each list of values add randomness in between leaves
    """
    def __init__(self, data):
        self.data = data
        next_pow_of_2 = int(2**ceil(log2(len(data))))
        self.data.extend([0] * (next_pow_of_2 - len(data)))
        # Intertwine with randomness to obtain zero knowledge.
        rand_list = [random.randint(0, 1 << 32) for x in self.data]
        self.data = [x for tup in zip(self.data, rand_list) for x in tup]
        # Create bottom level of the tree (i.e. leaves).
        self.tree = ["" for x in self.data] + \
                    [hash(str(x)) for x in self.data]
        for i in range(len(self.data) - 1, 0, -1):
            self.tree[i] = hash(self.tree[i * 2] + self.tree[i * 2 + 1])

    def root(self):
        return self.tree[1]

    def get_val_and_path(self, id):
        # Because of the zk padding, the data is now at id * 2
        id = id * 2
        val = self.data[id]
        auth_path = []
        id = id + len(self.data)
        while id > 1:
            auth_path += [self.tree[id ^ 1]]
            id = id // 2
        return val, auth_path

def verify_zk_merkle_path(root, data_size, value_id, value, path):
    cur = hash(str(value))
    # Due to zk padding, data_size needs to be multiplied by 2, as does the value_id
    tree_node_id = value_id * 2 + int(2**ceil(log2(data_size * 2)))
    for sibling in path:
        assert tree_node_id > 1
        if tree_node_id % 2 == 0:
            cur = hash(cur + sibling)
        else:
            cur = hash(sibling + cur)
        tree_node_id = tree_node_id // 2
    assert tree_node_id == 1
    return root == cur

def get_witness(instance,assignment):
    """ 
    given a problem instance and assignment we generate a witness
    that makes the argument zero-knowledge
    """
    sum = 0
    mx = 0
    obf = 1 - 2 * random.randint(0,1)
    witness = [sum]

    # check that len(instance) = len(assignment)
    assert len(instance) == len(assignment)

    for n,side in zip(instance,assignment):
        # zip provides a pair of elements of the same index
        assert side == 1 or side == -1
        sum += side * n * obf # obf simulates the coin flip
        witness += [sum]
        mx = max(mx,n)

    # make sure sum = 0 (dot product of instance and assignment is zero)
    assert sum == 0
    shift = random.randint(0,mx)
    witness = [x + shift for x in witness]
    return witness

""" using Fiat Shamir Heuristic we make the protocol non-interactive
    Using hash functions as randomness beacon prover simulates the 
    exchange and sends one long proof to verifier
"""
    
def gen_proof(instance,assignment,k):
    # k is the number of queries
    proof = []
    randomness_seed = instance[:]
    for i in range(k):
        # repeat the exchange k times
        # start by fetching witness
        wit = get_witness(instance,assignment)
        # build a tree
        tree = ZkMerkleTree(wit)
        random.seed(str(randomness_seed))
        query_idx = random.randint(0,len(instance))
        p =  [tree.root()]
        p += [query_idx]
        p += tree.get_val_and_path(query_idx)
        p += tree.get_val_and_path((query_idx + 1) % len(wit))
        proof += [p]
        randomness_seed += [p]
    return proof

def verify_proof(instance,proof):
    valid = True
    randomness_seed = instance[:]
    for query in proof :
        random.seed(str(randomness_seed))
        query_idx = random.randint(0,len(instance))
        root = query[0]
        valid &= query_idx == query[1]

        if query_idx < len(instance):
            valid &= abs(query[2] - query[4]) == abs(instance[query_idx])
        else:
            valid &= query[2] == query[4]
        valid &= verify_zk_merkle_path(root,len(instance)+1,query_idx,query[2],query[3])
        valid &= verify_zk_merkle_path(root,len(instance)+1,(query_idx + 1) % (len(instance)+1),query[4],query[5])

        randomness_seed += [query]
    return valid


def tests(k):
    problem = [1,2,3,6,6,6,12]
    assignment = [1,1,1,-1,-1,-1,1]
    proof = gen_proof(problem,assignment,k)
    print(proof)
    print(verify_proof(problem,proof))

if __name__ == '__main__' : 
    case = ["Yes", "Sir", "I Can", "Boogie!"]
    assert MerkleTree(case).root() == "b6702a9de57927193254cada92a7b1f92ffc124502a8357f8617a8735ce0a28f"
    tests(4)
