from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = []
    notes = music_string.split()
    for note in notes:
        if note == 'o':
            durations.append(4)
        elif note == 'o|':
            durations.append(2)
        elif note == '.|':
            durations.append(1)
    return durations
