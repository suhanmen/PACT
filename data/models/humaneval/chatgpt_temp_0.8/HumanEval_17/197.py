from typing import List


def parse_music(music_string: str) -> List[int]:
    beats = []
    split_music = music_string.split()
    for note in split_music:
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
    return beats
