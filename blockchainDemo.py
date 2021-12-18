# This is for encryption
import hashlib

# This is how we format our block
import json

# For the timestamp
from time import time

class Blockchain(object):
    def __init__(self):
        # Where blocks will be added
        self.chain = []
        # where transactions sit until approved
        self.pending_transactions = []
        # Create the genesis block
        self.new_block(previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks", proof=100)

    # builds new blocks
    def new_block(self, proof, previous_hash=None):
        # json block
        block = {
            # length of the chain plus one
            'index': len(self.chain) + 1,
            # time stamp to check transaction confirmation time
            'timestamp': time(),
            # add pending transactions
            'transactions': self.pending_transactions,
            # comes from the miner
            'proof': proof,
            # hashed version of the previous approved block 
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        # clear the pending transactions
        self.pending_transactions = []
        # add the block to the chain
        self.chain.append(block)

        return block
    #get the last block
    @property
    def last_block(self):
        # get the last block in the chain
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        #json transaction
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }
        # add transaction to pending transactions
        self.pending_transactions.append(transaction)
        # return the index of the block that will hold this transaction
        return self.last_block['index'] + 1
    
    def hash(self, block):
        # changes key values into strings
        string_object = json.dumps(block, sort_keys=True)
        # turns string into unicode
        block_string = string_object.encode()

        # SHA256 hash
        raw_hash = hashlib.sha256(block_string)
        # turn into hexadecimal
        hex_hash = raw_hash.hexdigest()

        return hex_hash

blockchain = Blockchain()
t1 = blockchain.new_transaction("Alice", "Bob", '5 BTC')
t2 = blockchain.new_transaction("Bob", "Satoshi", '1 BTC')
t3 = blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Alice", "Bob", '5 BTC')
t5 = blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
t6 = blockchain.new_transaction("Mike", "Ryan", '0.5 BTC')
blockchain.new_block(6789)

print("Blockchain: ", blockchain.chain)
