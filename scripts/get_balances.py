import os
import csv
from datetime import datetime
from web3 import Web3

def get_eth_balances():
    # --- Configuration ---
    # Get Infura URL from environment variable for security
    infura_url = os.environ.get('INFURA_URL')
    if not infura_url:
        raise Exception("INFURA_URL environment variable not set.")

    wallets_file = 'wallets.txt'
    results_dir = 'results'

    # --- Setup ---
    w3 = Web3(Web3.HTTPProvider(infura_url))
    if not w3.is_connected():
        raise Exception("Failed to connect to Ethereum node.")

    # Create results directory if it doesn't exist
    os.makedirs(results_dir, exist_ok=True)

    # --- Read Wallets ---
    with open(wallets_file, 'r') as f:
        wallet_addresses = [line.strip() for line in f if line.strip()]

    # --- Process Balances ---
    balances = []
    print(f"Querying balances for {len(wallet_addresses)} wallets...")
    for address in wallet_addresses:
        try:
            balance_wei = w3.eth.get_balance(w3.to_checksum_address(address))
            balance_eth = w3.from_wei(balance_wei, 'ether')
            balances.append({'Wallet': address, 'Balance_ETH': f"{balance_eth:.8f}"})
            print(f"  {address}: {balance_eth:.8f} ETH")
        except Exception as e:
            print(f"Could not get balance for {address}: {e}")
            balances.append({'Wallet': address, 'Balance_ETH': 'Error'})

    # --- Save to CSV ---
    now = datetime.utcnow()
    # Determine if it's an AM or PM run (based on UTC hour)
    period = "AM" if now.hour < 12 else "PM"
    file_name = f"{now.strftime('%Y-%m-%d')}-{period}.csv"
    file_path = os.path.join(results_dir, file_name)

    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Wallet', 'Balance_ETH']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(balances)

    print(f"\n✅ Successfully saved results to {file_path}")

if __name__ == "__main__":
    get_eth_balances()