# example of proof-of-work algorithm
'''
Bitcoin’s proof of work is very similar to the challenge shown in Example 8-10. 
The miner constructs a candidate block filled with transactions. 
Next, the miner calculates the hash of this block’s header and sees if it is smaller than the current target. 
If the hash is not less than the target, the miner will modify the nonce (usually just incrementing it by one) and try again. 
At the current difficulty in the bitcoin network, miners have to try quadrillions of times before finding a nonce that results in a low enough block header hash.
https://www.oreilly.com/library/view/mastering-bitcoin/9781491902639/ch08.html
'''

import hashlib
import time

try:
    long        # Python 2
    xrange
except NameError:
    long = int  # Python 3
    xrange = range

max_nonce = 2 ** 32  # 4 billion

def proof_of_work(header, difficulty_bits):
    # calculate the difficulty target
    target = 2 ** (256 - difficulty_bits)

    for nonce in xrange(max_nonce):
        str_encoded = bytes(str(header) + str(nonce), encoding='utf-8')
        hash_result = hashlib.sha256(str_encoded).hexdigest()

        # check if this is a valid result, below the target
        
        if long(hash_result, 16) < target:
            print("Success with nonce %d" % nonce)
            print("Hash is %s" % hash_result)
            print(long(hash_result, 16), "smaller than", target)
            return (hash_result, nonce)
        #else:
            #print(long(hash_result, 16), "not smaller than", target)

    print("Failed after %d (max_nonce) tries" % nonce)
    return nonce


if __name__ == '__main__':
    nonce = 0
    hash_result = ''

    # difficulty from 0 to 31 bits
    for difficulty_bits in xrange(32):
        difficulty = 2 ** difficulty_bits
        print("Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))
        print("Starting search...")

        # checkpoint the current time
        start_time = time.time()

        # make a new block which includes the hash from the previous block
        # we fake a block of transactions - just a string
        new_block = 'test block with transactions' + hash_result

        # find a valid nonce for the new block
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)

        # checkpoint how long it took to find a result
        end_time = time.time()

        elapsed_time = end_time - start_time
        print("Elapsed Time: %.4f seconds" % elapsed_time)

        if elapsed_time > 0:

            # estimate the hashes per second
            hash_power = float(long(nonce) / elapsed_time)
            print("Hashing Power: %ld hashes per second" % hash_power)