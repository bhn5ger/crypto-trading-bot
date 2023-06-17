# crypto-trading-bot

<p align="center">
<img src="https://github.com/bhn5ger/crypto-trading-bot/assets/72827220/b3097896-d43b-4a6b-89db-7063143ab09a" width= "354" height="162"/>
</p>

TO DO:
- Try some more strategies
- Requirements.txt file to install dependencies quickly on VMs
- Decouple execution engine into a service dedicated to applying strategies and sending orders to a queue and a service dedicated to processing that queue and executing orders
- Currently, if code fails the close position logic (sell) after opening a position (buy) it does not retry at the close position logic to close the open position, but instead starts completely over opening another position
- Must add retries using temporal with workflows and activities that can retry executing code exactly where it failed with the same data at failed runtime
- Add support for mobile for the website, including fixing the hamburger menu and enlarging the strategies image

PREVIOUS:
- Data stream price data lags behind by 1-2s, resulting in strategies being applied to prices 1-2s ago and trades made 1-2s too slow. Optimize latency by executing code in regions closer to exchanges and using websockets
- Finish grid trading implementation