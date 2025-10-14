python
from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = music_string.split()
    beat_counts = []
    for note in notes:
        if note == 'o':
            beat_counts.append(4)
        elif note == 'o|':
            beat_counts.append(2)
        elif note == '.|':
            beat_counts.append(1)
    return beat_counts
