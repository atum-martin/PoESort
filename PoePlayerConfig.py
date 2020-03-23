class PlayerConfig:
    poe_session_id = None
    account_name = None
    league = None
    path_of_exile_executable_title = None
    logfile = None
    resolution = None
    chaos_tab_ids = None
    sorting_flask = None
    sorting_jewel = None
    sorting_prophecy = None
    sorting_incubator = None
    sorting_oil = None
    sorting_catalyst = None
    sorting_metamorph = None
    sorting_gem = None
    sorting_override_div = None
    sorting_override_delve = None
    sorting_override_currency = None
    sorting_override_maps = None
    sorting_override_essence = None
    sorting_override_fragments = None
    sorting_override_uniques = None

def setupConfig(config):
    PlayerConfig.poe_session_id = config['poe_session_id']
    PlayerConfig.account_name = config['account_name']
    PlayerConfig.league = config['league']
    PlayerConfig.path_of_exile_executable_title = config['path_of_exile_executable_title']
    PlayerConfig.logfile = config['logfile']
    PlayerConfig.resolution = config['resolution']
    PlayerConfig.chaos_tab_ids = config['chaos_tab_ids']
    PlayerConfig.sorting_flask = config['sorting_flask']
    PlayerConfig.sorting_jewel = config['sorting_jewel']
    PlayerConfig.sorting_prophecy = config['sorting_prophecy']
    PlayerConfig.sorting_incubator = config['sorting_incubator']
    PlayerConfig.sorting_oil = config['sorting_oil']
    PlayerConfig.sorting_catalyst = config['sorting_catalyst']
    PlayerConfig.sorting_metamorph = config['sorting_metamorph']
    PlayerConfig.sorting_gem = config['sorting_gem']
    PlayerConfig.sorting_override_div = config['sorting_override_div']
    PlayerConfig.sorting_override_delve = config['sorting_override_delve']
    PlayerConfig.sorting_override_currency = config['sorting_override_currency']
    PlayerConfig.sorting_override_maps = config['sorting_override_maps']
    PlayerConfig.sorting_override_essence = config['sorting_override_essence']
    PlayerConfig.sorting_override_fragments = config['sorting_override_fragments']
    PlayerConfig.sorting_override_uniques = config['sorting_override_uniques']
