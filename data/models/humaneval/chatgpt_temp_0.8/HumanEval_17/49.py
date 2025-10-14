from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = []
    notes = music_string.split()
    note_values = {'o': 4, 'o|': 2, '.|': 1}
    for note in notes:
        beats.append(note_values[note])
    return beats
