from blockchain import Blockchain

def print_blockchain(blockchain):
    for block in blockchain.chain:
        print(f"Block #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Transactions: {block.transactions}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print("\n")

def main():
    blockchain1 = Blockchain()
    blockchain2 = Blockchain()

    blockchain1.add_transaction({"from": "Alice", "to": "Bob", "amount": 50})
    blockchain1.add_transaction({"from": "Bob", "to": "Charlie", "amount": 25})

    blockchain1.mine_pending_transactions("miner1")

    blockchain2.add_transaction({"from": "Eve", "to": "Frank", "amount": 75})
    blockchain2.add_transaction({"from": "Frank", "to": "Grace", "amount": 35})

    blockchain2.mine_pending_transactions("miner2")

    print("Blockchain 1:")
    print_blockchain(blockchain1)
    print(f"Is blockchain 1 valid? {blockchain1.is_chain_valid()}")

    print("Blockchain 2:")
    print_blockchain(blockchain2)
    print(f"Is blockchain 2 valid? {blockchain2.is_chain_valid()}")

if __name__ == "__main__":
    main()
