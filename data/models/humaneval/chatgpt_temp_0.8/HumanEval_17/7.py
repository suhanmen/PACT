from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    notes = music_string.split()
    result = []
    for note in notes:
        result.append(durations[note])
    return result
