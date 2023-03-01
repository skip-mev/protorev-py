from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins

from cosmpy.aerial.client import LedgerClient, NetworkConfig, Account
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey
from cosmpy.aerial.tx import Transaction as Tx, SigningCfg

from cosmpy.protos.osmosis.gamm.v1beta1.tx_pb2 import MsgSwapExactAmountIn
from cosmpy.protos.osmosis.poolmanager.v1beta1.swap_route_pb2 import SwapAmountInRoute
from cosmpy.protos.cosmos.base.v1beta1.coin_pb2 import Coin

# @DEV TODO: 
# EDIT MNEMONIC TO BE ONE WITH A LOT OF UOSMO (ADMIN ACCOUNT FROM PREVIOUS TESTS SHOULD SUFFICE
# THIS ONE IS FROM LOCALOSMOSIS SETUP
MNEMONIC = "notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"

# @DEV TODO: 
# EDIT AMOUNT TO BE A LARGE AMOUNT THE ADMIN ADDRESS HAS
# WILL SWAP THIS AMOUNT OF UOSMO INTO POOL 1
INITIAL_SWAP_AMOUNT = "1000000000"

# @DEV TODO: 
# EDIT PARAMS FOR TESTNET
CHAIN_ID = "localosmosis"
DENOM = "uosmo"
ADDRESS_PREFIX = "osmo"
GAS_LIMIT = 10_000_000
GAS_FEE = "50000uosmo"
RPC_NODE = "http://0.0.0.0:26657/"
REST_NODE = "http://0.0.0.0:1317"

def main():
    cfg = NetworkConfig(
        chain_id=CHAIN_ID,
        url=f"rest+{REST_NODE}",
        fee_minimum_gas_price=.0025,
        fee_denomination="uosmo",
        staking_denomination="uosmo",
    )
    client = LedgerClient(cfg)
    
    # Used to test the tx pool points / limits work properly
    # Most likely not useful for osmosis team testing as tracking pool points consumption
    # is via adding print statements throughout on my localosmosis setup    
    many_balancer_swaps_in_one_tx(client)
    
    # Maxs out the block limit of number of backruns by swapping 200 times in one block
    many_balancer_swaps_in_one_block(client, 497, "ibc/46B44899322F3CD854D2D46DEEF881958467CDD4B3B10086DA49296BBED94BED")
    
    #many_stableswap_swaps_in_block(client)
    
def many_balancer_swaps_in_one_tx(client):
    admin_wallet, admin_address, admin_account = create_wallet(client, MNEMONIC)
    swap_amount_in_route_pairs = [
        [SwapAmountInRoute(pool_id=3, token_out_denom="ibc/1480B8FD20AD5FCAE81EA87584D269547DD4D436843C1D20F15E00EB64743EF4"),
        SwapAmountInRoute(pool_id=4, token_out_denom="ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2")],
        [SwapAmountInRoute(pool_id=573, token_out_denom="ibc/4E5444C35610CC76FC94E7F7886B93121175C28262DDFDDE6F84E82BF2425452"),
        SwapAmountInRoute(pool_id=574, token_out_denom="ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2")],
        [SwapAmountInRoute(pool_id=497, token_out_denom="ibc/46B44899322F3CD854D2D46DEEF881958467CDD4B3B10086DA49296BBED94BED"),
        SwapAmountInRoute(pool_id=498, token_out_denom="ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2")],
        ]
    token_in = Coin(denom=DENOM, amount=INITIAL_SWAP_AMOUNT)
    msgs=[]
    for route in swap_amount_in_route_pairs:
        msg_swap_exact_amount_in = MsgSwapExactAmountIn(
            sender=admin_address,
            routes=route,
            token_in=token_in,
            token_out_min_amount="1")
        msgs.append(msg_swap_exact_amount_in)
    create_and_send_tx(msgs, admin_wallet, admin_account, client, "Swap", admin_account.sequence)   

def many_balancer_swaps_in_one_block(client, pool_id: int, token_out_denom: str, num_swaps: int = 200):
    admin_wallet, admin_address, admin_account = create_wallet(client, MNEMONIC)
    for i in range(num_swaps):
        swap_amount_in_route = SwapAmountInRoute(pool_id=pool_id, token_out_denom=token_out_denom)
        token_in = Coin(denom=DENOM, amount=INITIAL_SWAP_AMOUNT)
        msg_swap_exact_amount_in = MsgSwapExactAmountIn(
            sender=admin_address,
            routes=[swap_amount_in_route],
            token_in=token_in,
            token_out_min_amount="1")
        create_and_send_tx([msg_swap_exact_amount_in], admin_wallet, admin_account, client, "Swap", admin_account.sequence + i + 1)
        
def many_stableswap_swaps_in_block(client):
    admin_wallet, admin_address, admin_account = create_wallet(client, MNEMONIC)
    first_denom_out = "ibc/D189335C6E4A68B513C10AB227BF1C1D38C746766278BA3EEB4FB14124F1D858"
    swap_amount_in_route = SwapAmountInRoute(pool_id=678, token_out_denom=first_denom_out)
    token_in = Coin(denom=DENOM, amount=INITIAL_SWAP_AMOUNT)
    msg_swap_exact_amount_in = MsgSwapExactAmountIn(
        sender=admin_address,
        routes=[swap_amount_in_route],
        token_in=token_in,
        token_out_min_amount="1")
    create_and_send_tx([msg_swap_exact_amount_in], admin_wallet, admin_account, client, "Swap", admin_account.sequence)
    
    balance = client.query_bank_balance(admin_address, first_denom_out)
    
    balance_chunk = int(balance / 1000)
    
    for i in range(100):
        swap_amount_in_route = SwapAmountInRoute(pool_id=872, token_out_denom="ibc/9F9B07EF9AD291167CF5700628145DE1DEB777C2CFC7907553B24446515F6D0E")
        token_in = Coin(denom=first_denom_out, amount=str(balance_chunk))
        msg_swap_exact_amount_in = MsgSwapExactAmountIn(
            sender=admin_address,
            routes=[swap_amount_in_route],
            token_in=token_in,
            token_out_min_amount="1")
        create_and_send_tx([msg_swap_exact_amount_in], admin_wallet, admin_account, client, "Swap", admin_account.sequence + i + 1)
    
    
def swap(client):
    admin_wallet, admin_address, admin_account = create_wallet(client, MNEMONIC)
    swap_amount_in_route = SwapAmountInRoute(
        pool_id=1,
        token_out_denom="ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2")
    token_in = Coin(denom=DENOM, amount=INITIAL_SWAP_AMOUNT)
    msg_swap_exact_amount_in = MsgSwapExactAmountIn(
        sender=admin_address,
        routes=[swap_amount_in_route],
        token_in=token_in,
        token_out_min_amount="1")
    create_and_send_tx([msg_swap_exact_amount_in], admin_wallet, admin_account, client, "Swap")
    
def create_wallet(client, mnemonic: str) -> tuple[LocalWallet, str, Account]:
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    bip44_def_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.COSMOS).DeriveDefaultPath()
    wallet = LocalWallet(PrivateKey(bip44_def_ctx.PrivateKey().Raw().ToBytes()), prefix=ADDRESS_PREFIX)
    address = str(wallet.address())
    print(f"Address: {address}")
    account = client.query_account(address=address)
    print(f"Account: {account}")
    balance = client.query_bank_balance(address=address, denom=DENOM)
    print(f"Balance: {balance}")
    return wallet, address, account    

def create_and_send_tx(msgs: list, wallet: LocalWallet, account: Account, client, print_helper, sequence: int = 0) -> None:
    tx = Tx()
    for msg in msgs:
        tx.add_message(msg)
    if sequence > 0:
        tx.seal(signing_cfgs=[SigningCfg.direct(wallet.public_key(), sequence)], fee=GAS_FEE, gas_limit=GAS_LIMIT)
        tx.sign(wallet.signer(), CHAIN_ID, account.number)
        tx.complete()
        client.broadcast_tx(tx)
    else:
        tx.seal(signing_cfgs=[SigningCfg.direct(wallet.public_key(), account.sequence)], fee=GAS_FEE, gas_limit=GAS_LIMIT)
        tx.sign(wallet.signer(), CHAIN_ID, account.number)
        tx.complete()
        submitted_tx = client.broadcast_tx(tx)
        submitted_tx.wait_to_complete()
        print(f"{print_helper} Submitted Tx Response: {submitted_tx.response}")
    
if __name__ == "__main__":
    main()