from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}  # mapping note types to their durations in beats
    music_notes = music_string.split()  # split input string into separate notes
    beats_list = [durations[note] for note in music_notes]  # convert each note to its duration in beats
    return beats_list
