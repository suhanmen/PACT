from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1} # dictionary to map musical notes to beat durations
    notes = music_string.split() # split the string into a list of individual notes
    beats = [durations[note] for note in notes] # map each note to its beat duration using the durations dictionary
    return beats
