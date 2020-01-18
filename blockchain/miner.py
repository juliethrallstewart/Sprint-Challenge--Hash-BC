import hashlib
import requests
import json

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")

    
    #  TODO: Your code here
    # block_string = json.dumps(last_proof)
    # p = f"{last_proof}".encode()
    # last_6 = p[-6:]
    # result = hashlib.sha256(last_6).hexdigest()
    # proof = result[-6:]

    block_string = json.dumps(last_proof)
    proof = 0
    while valid_proof(block_string, proof) is False:
        proof += 1
    
    return proof
  


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """

    guess = f"{proof}{last_hash}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    last = f"{last_hash}".encode()
    last_h = hashlib.sha256(last).hexdigest()
    
    # print(f"guess_hash {guess_hash[:6]}, last_h {last_h[-6:]}")

    return guess_hash[:6] == last_h[-6:]
    
 


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}
        print(post_data, "POST DATA")
        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:

            print('help')
            print(data.get('message'))
        
