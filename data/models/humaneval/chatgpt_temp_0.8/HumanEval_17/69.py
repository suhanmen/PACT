from typing import List


def parse_music(music_string: str) -> List[int]:
    beats = []
    symbols = {"o": 4, "o|": 2, ".|": 1}
    for note in music_string.split():
        beats.append(symbols[note])
    return beats
