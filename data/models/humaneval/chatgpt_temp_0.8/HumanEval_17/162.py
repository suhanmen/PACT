from typing import List


def parse_music(music_string: str) -> List[int]:
    duration_dict = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    durations = []
    for note in notes:
        durations.append(duration_dict[note])
    return durations
