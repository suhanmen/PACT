from typing import List

def parse_music(music_string: str) -> List[int]:
    beats_map = {"o": 4, "o|": 2, ".|": 1}  # map each note to its corresponding number of beats
    notes = music_string.split()  # split the string into individual notes
    beats = [beats_map[note] for note in notes]  # convert each note to its corresponding number of beats
    return beats
