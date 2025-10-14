from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    parsed_music = []
    for note in music_string.split():
        parsed_music.append(notes[note])
    return parsed_music
