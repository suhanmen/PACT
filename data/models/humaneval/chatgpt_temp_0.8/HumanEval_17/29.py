from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split()
    note_lengths = []

    for note in notes:
        if note == 'o':
            note_lengths.append(4)
        elif note == 'o|':
            note_lengths.append(2)
        elif note == '.|':
            note_lengths.append(1)

    return note_lengths
