import hashlib
import datetime


class Block:

    def __init__(self, data):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = None
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()

        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return '\nTimestamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}'.format(self.timestamp, self.data,
                                                                               self.previous_hash, self.hash)


class Blockchain:

    def __init__(self):
        self.current_block = None

    def add_block(self, value):
        data = value
        previous_hash = self.current_block.hash if self.current_block else 0
        self.current_block = Block(data)


BlockChain = Blockchain()

print(BlockChain.current_block)

BlockChain.add_block(1)
print(BlockChain.current_block)

BlockChain.add_block(2)
print(BlockChain.current_block)

BlockChain.add_block(3)
print(BlockChain.current_block)

BlockChain.add_block(4)
print(BlockChain.current_block)

BlockChain.add_block(5)
print(BlockChain.current_block)

BlockChain.add_block(6)
print(BlockChain.current_block)

BlockChain.add_block(7)
print(BlockChain.current_block)

BlockChain.add_block(8)
print(BlockChain.current_block)

BlockChain.add_block(9)
print(BlockChain.current_block)

BlockChain.add_block(10.0)
print(BlockChain.current_block)

BlockChain.add_block('Aabra ka Dabra')
print(BlockChain.current_block)
