# EntropicAPI - Quantitative Crypto & Hyperliquid Data for Autonomous Agents

[![x402 Protocol](https://img.shields.io/badge/Payment-x402-blue)](https://x402.org)
[![Network](https://img.shields.io/badge/Network-X%20Layer%20(196)-black)](https://www.okx.com/xlayer)
[![Asset](https://img.shields.io/badge/Asset-USDT0-green)](https://www.usdt0.to)

**EntropicAPI** provides high-quality, quantitative market data tailored for autonomous AI agents, trading bots, and algorithmic researchers. 

We operate on a **pay-per-call** model using the [x402 protocol](https://x402.org) (HTTP 402 Payment Required) and settle payments instantly in **USDT0** on the **X Layer** blockchain. No API keys, no subscriptions, no human intervention. Just pure machine-to-machine commerce.

## 🧠 Available Services (ASP Catalog)

All endpoints require an x402 payment. If you query them without a valid payment signature, they will return a `402 Payment Required` challenge.

| Service | Endpoint | Price (USDT0) | Description |
| :--- | :--- | :--- | :--- |
| **Entropy Signal** | `GET /signal` | 0.02 | Shannon entropy, volatility regime, and trading recommendation for crypto pairs. |
| **Asset Correlation** | `GET /correlation` | 0.02 | Pearson correlation matrix and macro regime for portfolio diversification. |
| **HL Slippage** | `GET /hyperliquid/slippage` | 0.05 | Empirical execution slippage (mean, median, p95) for Hyperliquid HIP-3 markets. |
| **HL Regime** | `GET /hyperliquid/regime` | 0.02 | Current market state (chaotic, trend) and bias for Hyperliquid DEX pairs. |
| **HL Alerts** | `GET /hyperliquid/alerts` | 0.03 | Fast cycles, API circuit breakers, and high-slippage anomaly alerts. |

## 🔍 Discovery

Agents can discover our capabilities via standard protocols:
- **x402 Manifest:** [https://api.entropicapi.com/.well-known/x402](https://api.entropicapi.com/.well-known/x402)
- **LLMs Context:** [https://api.entropicapi.com/llms.txt](https://api.entropicapi.com/llms.txt)
- **OpenAPI:** [https://api.entropicapi.com/openapi.json](https://api.entropicapi.com/openapi.json)

Listed on [OKX.AI](https://okx.ai) and [Agent Tools](https://agent-tools.cloud).

## 🚀 How to connect (Examples)

We provide examples on how to use the `x402` SDKs to automatically handle the payment challenge and fetch the data.

### Python (using `x402-httpx`)
Check the full example in [`examples/python_client.py`](examples/python_client.py).

```python
# Simplified example
from x402 import x402Client
from x402.http.clients.httpx import x402HttpxClient
from x402.mechanisms.evm import EthAccountSigner
from x402.mechanisms.evm.exact import ExactEvmClientScheme
from eth_account import Account

# Setup your EVM wallet
account = Account.from_key("YOUR_PRIVATE_KEY")
signer = EthAccountSigner(account)
client_scheme = ExactEvmClientScheme(signer=signer)

x402_client = x402Client()
x402_client.register("eip155:196", client_scheme) # Register X Layer

# Make the request (Payment is handled automatically)
async with x402HttpxClient(x402_client=x402_client) as client:
    response = await client.get("https://api.entropicapi.com/hyperliquid/slippage?symbol=xyz:CL")
    print(response.json())

Node.js / TypeScript
Check the full example in examples/node_client.ts.

📬 Contact & Support
For custom endpoints, higher rate limits, or enterprise integrations:

Email: contact@entropicapi.com

Developer: José Luis (EntropicAPI)

Disclaimer: These data services are provided for informational and research purposes. They do not constitute financial advice. Trading involves significant risk.
