from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}  # mapping of note duration to number of beats

    notes = music_string.split()  # split the string into individual notes
    beats = [durations[note] for note in notes]  # use the mapping to get the number of beats per note

    return beats
