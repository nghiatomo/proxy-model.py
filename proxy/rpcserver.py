from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from .plugin.solana_rest_api import EthereumModel

eth = EthereumModel()

def eth_blockNumber():
    return eth.eth_blockNumber()

def eth_getBalance(account, tag):
    return eth.eth_getBalance(account, tag)

def eth_getLogs(obj):
    return eth.eth_getLogs(obj)

def getBlockBySlot(slot, full):
    return eth.getBlockBySlot(slot, full)

def eth_getStorageAt(account, position, block_identifier):
    return eth.eth_getStorageAt(account, position, block_identifier)

def eth_getBlockByHash(trx_hash, full):
    return eth.eth_getBlockByHash(trx_hash, full)

def eth_getBlockByNumber(tag, full):
    return eth.eth_getBlockByNumber(tag, full)

def eth_call(self, obj, tag):
    return eth.eth_call(obj, tag)

def eth_getTransactionCount(account, tag):
    return eth.eth_getTransactionCount(account, tag)

def eth_getTransactionReceipt(trxId, block_info = None):
    return eth.eth_getTransactionReceipt(trxId, block_info)

def eth_getTransactionByHash(trxId, block_info = None):
    return eth.eth_getTransactionByHash(trxId, block_info)



def startRpc():
    
    server = SimpleJSONRPCServer(('localhost', 8090))
    server.register_function(eth_blockNumber)
    server.register_function(eth_getBalance)
    server.register_function(eth_getLogs)
    server.register_function(getBlockBySlot)
    server.register_function(eth_getStorageAt)
    server.register_function(eth_getBlockByHash)
    server.register_function(eth_getBlockByNumber)
    server.register_function(eth_call)
    server.register_function(eth_getTransactionCount)
    server.register_function(eth_getTransactionReceipt)
    server.register_function(eth_getTransactionByHash)
    print("Start rpc server")
    server.serve_forever()


