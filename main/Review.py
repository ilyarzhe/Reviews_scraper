from dataclasses import dataclass

@dataclass
class Review:
    rating : float
    text : str
    date : str
    summary: str

    