python
from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {"o": 4, "o|": 2, ".|": 1}
    result = []
    for note in music_string.split():
        result.append(durations[note])
    return result
