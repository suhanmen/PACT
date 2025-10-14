python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split(' ')
    beats = []
    for note in music_list:
        beats.append(notes[note])
    return beats
