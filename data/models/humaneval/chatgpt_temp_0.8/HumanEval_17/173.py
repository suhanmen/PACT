from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}  # dictionary to map note strings to their durations
    notes = music_string.split()  # split the string by whitespace
    durations_list = [durations[note] for note in notes]  # use list comprehension to get duration for each note
    return durations_list
