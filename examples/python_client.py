import os
import asyncio
from eth_account import Account
from x402 import x402Client
from x402.http.clients.httpx import x402HttpxClient
from x402.mechanisms.evm import EthAccountSigner
from x402.mechanisms.evm.exact import ExactEvmClientScheme

# 1. Setup your wallet (must have USDT0 on X Layer)
PRIVATE_KEY = os.getenv("EVM_PRIVATE_KEY", "0xYOUR_PRIVATE_KEY_HERE")

async def main():
    if PRIVATE_KEY == "0xYOUR_PRIVATE_KEY_HERE":
        print("Please set your EVM_PRIVATE_KEY environment variable.")
        return

    account = Account.from_key(PRIVATE_KEY)
    print(f"Using wallet: {account.address}")

    # 2. Configure the x402 client for X Layer (eip155:196)
    signer = EthAccountSigner(account)
    client_scheme = ExactEvmClientScheme(signer=signer)
    x402_client = x402Client()
    x402_client.register("eip155:196", client_scheme)

    # 3. Make the request (x402 handles the 402 challenge and payment automatically)
    url = "https://api.entropicapi.com/hyperliquid/slippage?symbol=xyz:CL&window=7d"
    
    print(f"Fetching: {url}")
    async with x402HttpxClient(x402_client=x402_client, timeout=30) as client:
        try:
            response = await client.get(url)
            print(f"Status: {response.status_code}")
            print("Data received:", response.json())
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
