from TwitchChannelPointsMiner import TwitchChannelPointsMiner
twitch_miner = TwitchChannelPointsMiner("D1nocan")
twitch_miner.analytics(host="127.0.0.1", port=5000, refresh=5)
twitch_miner.mine(["roshtein", "vondice", "deuceace"])   
