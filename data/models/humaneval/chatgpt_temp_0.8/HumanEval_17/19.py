from typing import List


def parse_music(music_string: str) -> List[int]:
    beats = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    for note in music_string.split():
        result.append(beats[note])
    return result
