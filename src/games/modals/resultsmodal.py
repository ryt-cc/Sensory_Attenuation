from dataclasses import dataclass


@dataclass
class GameResults:
    sample_id:int
    name_of_game:str
    rounds:int
    score:int