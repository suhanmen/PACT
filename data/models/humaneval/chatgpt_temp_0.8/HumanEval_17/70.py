from typing import List


def parse_music(music_string: str) -> List[int]:
    beats_dict = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    notes = music_string.split()
    for note in notes:
        result.append(beats_dict[note])
    return result
