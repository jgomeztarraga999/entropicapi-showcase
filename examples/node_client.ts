import { x402Client } from "@coinbase/x402-axios"; // Nota: Asume el uso del SDK estándar
import axios from "axios";
import { Wallet } from "ethers";

// 1. Setup your wallet
const privateKey = process.env.EVM_PRIVATE_KEY || "0xYOUR_PRIVATE_KEY_HERE";
const wallet = new Wallet(privateKey);

async function main() {
  // 2. Configure x402 Client
  const client = new x402Client({
    account: wallet,
    network: "eip155:196", // X Layer
  });

  // 3. Make request
  const url = "https://api.entropicapi.com/hyperliquid/slippage?symbol=xyz:CL&window=7d";
  console.log(`Fetching: ${url}`);
  
  try {
    const response = await client.get(url);
    console.log("Data received:", response.data);
  } catch (error) {
    console.error("Error:", error);
  }
}

main();
