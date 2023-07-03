"""This file adds conveniences for calling the remote api from backend.production.omeda-aws.com/api/public/"""


# Imports


# API Calls
def get_matches_byEpoch(epoch: str):
    """Gets information from the last 10 matches starting with a unix epoch.
    
    Uses API endpoint https://backend.production.omeda-aws.com/api/public/get-matches-since/<Epoch Time>/
    
    Parameters:

    Returns:

    """
    pass


def get_matches_byMatchID(match_id: str):
    """Gets information from a single match identified by a match ID.
    
    Uses API endpoint  https://backend.production.omeda-aws.com/api/public/get-match/<Match ID>/
    
    Parameters:

    Returns:
    
    """
    pass


def get_matches_byPlayerID(player_ID: str):
    """Gets information from the last 10 matches identified by a player ID.
    
    Uses API endpoint  https://backend.production.omeda-aws.com/api/public/get-matches-by-player/<Player ID>/
    
    Parameters:

    Returns:
    
    """
    pass


def get_itemID(item_name: str):
    """Gets identifying information from an item name.
    
    Uses API endpoint  https://backend.production.omeda-aws.com/api/public/<Item Name>/
    
    Parameters:

    Returns:
    
    """
    pass


def get_item(item_name: str):
    """Gets information about an item.
    
    Uses API endpoint  https://backend.production.omeda-aws.com/api/public/<Item ID>/
    
    Parameters:

    Returns:
    
    """
    pass


def get_hero(hero_name: str):
    """Gets information about an item.
    
    Uses API endpoint https://backend.production.omeda-aws.com/api/public/hero/<Hero Name>/
    
    Parameters:

    Returns:
    
    """
    pass