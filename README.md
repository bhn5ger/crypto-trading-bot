# crypto-trading-bot

<p align="center">
<img src="https://github.com/bhn5ger/crypto-trading-bot/assets/72827220/b3097896-d43b-4a6b-89db-7063143ab09a" width= "354" height="162"/>
</p>

TO DO:
- Trading on decentralized exchanges using sandwich trading
    - Prone to salmonella attack: https://github.com/Defi-Cartel/salmonella
- Requirements.txt file to install dependencies quickly on VMs
- Decouple execution engine into a service dedicated to applying strategies and sending orders to a queue and a service dedicated to processing that queue and executing orders
- Add retries

PREVIOUS:
- Trading on centralized exchanges using arbitrage and grid trading
- Optimize latency by executing code in regions closer to exchanges and using websockets