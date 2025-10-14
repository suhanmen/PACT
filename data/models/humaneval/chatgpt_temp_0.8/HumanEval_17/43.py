from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1} # a dictionary that maps each note type to its duration
    notes = music_string.split() # split the string into individual notes
    result = [] # initialize an empty list to store the durations of each note

    # iterate through the notes and add their durations to the result list
    for note in notes:
        result.append(durations[note])

    return result
