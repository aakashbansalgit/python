from Crypto.PublicKey import RSAfrom Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from uuid import uuid4
from urllib.parse import urlparse
from flask import Flask, request, jsonify, render_template
from time import time
from flask_cors import CORS
from collections import OrderedDict
import binascii
import hashlib
import requests
import json

rewardvar = 1
difficultyval = 2
sendvar = "The Blockchain"

class Blockchain:

    def __init__(self):
        self.list_chain = []
        self.list_transaction = []
        self.list_nodes = set()
        self.id_node = str(uuid4()).replace('-', '')
        self.generator_block_creation(0, '00')

    def block_creation(self, nonce, past_Hash):
        """
        Add a block of transactions to the blockchain
        """
        block = {'block_number': len(self.list_chain) + 1,
                 'timestamp': time(),
                 'transactions': self.list_transaction,
                 'nonce': nonce,
                 'past_Hash': past_Hash}

        # Reset the current list of transactions
        self.list_transaction = []
        self.list_chain.append(block)
        return block
    
    def verify_transaction_signature(self, sender_public_key, signature, transaction):
        """
        The Zero Knowledge Proof algorithm with the
        t = g^e
        c = H(m  t)
        d = e - xc
        The miner would send (c, d) as the signature, along the message m.
        Which is basically a hash of the message with a proof that he knows the secret x.
        To verify the signature you would use the public key y = g^x to compute y^c  g^d = t
        and then you would compute the hash. (All this is accomplished using the RSA function here)
        It would give you the proof that the signer knows x (authentication, non-repudiation) and
        that the message hasn't been tampered (integrity) with zero knowledge of the value of x !
        """
        public_key = RSA.importKey(binascii.unhexlify(sender_public_key))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA.new(str(transaction).encode('utf8'))
        try:
            verifier.verify(h, binascii.unhexlify(signature))
            return True
        except ValueError:
            return False
    
    def node_reg(self, node_url):
        url_read = urlparse(node_url)
        if url_read.netloc:
            self.list_nodes.add(url_read.netloc)
        elif url_read.path:
            self.list_nodes.add(url_read.path)
        else:
            raise ValueError('Invalid URL')

    @staticmethod
    def valid_proof(transactions, ending_hash, nonce, difficulty=difficultyval):
        guess = (str(transactions) + str(ending_hash) + str(nonce)).encode('utf8')
        h = hashlib.new('sha256')
        h.update(guess)
        guess_hash = h.hexdigest()
        return guess_hash[:difficulty] == '0' * difficulty

    def proof_of_work(self):
        ending_block = self.list_chain[-1]
        ending_hash = self.hash(ending_block)
        nonce = 0
        while self.valid_proof(self.list_transaction, ending_hash, nonce) is False:
            nonce += 1

        return nonce

    @staticmethod
    def hash(block):
        # We must to ensure that the Dictionary is ordered, otherwise we'll get inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode('utf8')
        h = hashlib.new('sha256')
        h.update(block_string)
        return h.hexdigest()

    def resolve_conflicts(self):
        neighbours = self.list_nodes
        new_chain = None

        max_length = len(self.list_chain)
        for node in neighbours:
            response = requests.get('http://' + node + '/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.list_chain = new_chain
            return True

        return False

    def valid_chain(self, chain):
        ending_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            if block['past_Hash'] != self.hash(ending_block):
                return False

            transactions = block['transactions'][:-1]
            transaction_elements = ['sender_public_key', 'recipient_public_key', 'amount']
            transactions = [OrderedDict((k, transaction[k]) for k in transaction_elements) for transaction in
                            transactions]

            if not self.valid_proof(transactions, block['past_Hash'], block['nonce'], difficultyval):
                return False

            ending_block = block
            current_index += 1

        return True

    def submit_transaction(self, sender_public_key, recipient_public_key, signature, amount):
        transaction = OrderedDict({
            'sender_public_key': sender_public_key,
            'recipient_public_key': recipient_public_key,
            'amount': amount
        })

        # Reward for mining a block
        if sender_public_key == sendvar:
            self.list_transaction.append(transaction)
            return len(self.list_chain) + 1
        else:
            # Transaction from wallet to another wallet
            signature_verification = self.verify_transaction_signature(sender_public_key, signature, transaction)
            if signature_verification:
                self.list_transaction.append(transaction)
                return len(self.list_chain) + 1
            else:
                return False


# Instantiate the Blockchain
blockchain = Blockchain()

# Instantiate the Node
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/configure')
def configure():
    return render_template('./configure.html')


@app.route('/transactions/get', methods=['GET'])
def get_transactions():
    transactions = blockchain.list_transaction
    response = {'transactions': transactions}
    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.list_chain,
        'length': len(blockchain.list_chain)
    }

    return jsonify(response), 200


@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm
    nonce = blockchain.proof_of_work()

    blockchain.submit_transaction(sender_public_key=sendvar,
                                  recipient_public_key=blockchain.id_node,
                                  signature='',
                                  amount=rewardvar)

    ending_block = blockchain.list_chain[-1]
    past_Hash = blockchain.hash(ending_block)
    block = blockchaink_creation(nonce, past_Hash)

    response = {
        'message': 'New block created',
        'block_number': block['block_number'],
        'transactions': block['transactions'],
        'nonce': block['nonce'],
        'past_Hash': block['past_Hash'],
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.form
    required = ['confirmation_sender_public_key', 'confirmation_recipient_public_key', 'transaction_signature',
                'confirmation_amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    transaction_results = blockchain.submit_transaction(values['confirmation_sender_public_key'],
                                                        values['confirmation_recipient_public_key'],
                                                        values['transaction_signature'],
                                                        values['confirmation_amount'])
    if transaction_results == False:
        response = {'message': 'Invalid transaction/signature'}
        return jsonify(response), 406
    else:
        response = {'message': 'Transaction will be added to the Block ' + str(transaction_results)}
        return jsonify(response), 201


@app.route('/nodes/get', methods=['GET'])
def get_nodes():
    nodes = list(blockchain.list_nodes)
    response = {'nodes': nodes}
    return jsonify(response), 200


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.list_chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.list_chain
        }
    return jsonify(response), 200


@app.route('/nodes/register', methods=['POST'])
def node_reg():
    values = request.form
    # 127.0.0.1:5002,127.0.0.1:5003, 127.0.0.1:5004
    nodes = values.get('nodes').replace(' ', '').split(',')

    if nodes is None:
        return 'Error: Please supply a valid list of nodes', 400

    for node in nodes:
        blockchain.node_reg(node)

    response = {
        'message': 'Nodes have been added',
        'total_nodes': [node for node in blockchain.list_nodes]
    }
    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help="port to listen to")
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port, debug=True)
