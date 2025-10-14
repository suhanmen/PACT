from typing import List


def parse_music(music_string: str) -> List[int]:
    result = []
    legend = {'o': 4, 'o|': 2, '.|': 1}
    for note in music_string.split():
        result.append(legend[note])
    return result
