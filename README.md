# ETH Balance Tracker

Just a simple project to auto track ETH balances for a list of wallets using a GitHub Action.

## How it works

* A GitHub Action runs on a schedule (i set it to twice a day by default).
* It reads the wallet addresses you provide in `wallets.txt`.
* It then queries the Ethereum mainnet for the ETH balance of each wallet.
* The results are saved to a new CSV file inside the `results/` directory, named with the current date (for eg, `2025-07-21-PM.csv`).
* The action comits the new report back to this repo automatically.

## Setup

To get this working in your own repo, you just need to do a few things:

1.  **Add Wallets:** Put the Ethereum addresses you want to track in `wallets.txt`, one address per line.

2.  **Get an API Key:** You'll need an API key from a node provider like [Infura](https://infura.io). Their free plan is more than enough for this, but you can choose any other node provder. 

3.  **Create GitHub Secret:** This is the most important part. In your GitHub repo, go to `Settings` > `Secrets and variables` > `Actions`. Create a **New repository secret** with:
    * Name: `INFURA_URL`
    * Secret: Your full Infura HTTPS endpoint URL (eg, `https://mainnet.infura.io/v3/your-api-key`).

## Changing the Schedule

If you want to change how often the script runs, just edit the `cron` line in `.github/workflows/main.yml`. The comments in `config.ini` i have some examples of different schedules.

## important

Make sure your "Actions" settings are set yo read and write permissions.