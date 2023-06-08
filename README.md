# crypto-trading-bot

<p align="center">
<img src="https://github.com/bhn5ger/crypto-trading-bot/assets/72827220/b3097896-d43b-4a6b-89db-7063143ab09a" width= "354" height="162"/>
</p>

TO DO:
- Finish grid trading implementation
- Try some more strategies
- Host on GCP
- Front-end
- Requirements.txt file to install dependencies quickly on VMs
- Data stream price data lags behind by 1-2s, resulting in strategies being applied to prices 1-2s ago and trades made 1-2s too slow. Optimize latency by executing code in regions closer to exchanges, and using websockets
- Add support for mobile for the website, including fixing the hamburger menu and enlarging the strategies image