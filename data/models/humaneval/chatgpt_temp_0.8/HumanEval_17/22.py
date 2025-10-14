from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}  # dictionary mapping note strings to their durations
    notes = music_string.split()  # split the string into individual note strings
    beats = [durations[note] for note in notes]  # create a list of durations by looking up each note in the dictionary
    return beats
