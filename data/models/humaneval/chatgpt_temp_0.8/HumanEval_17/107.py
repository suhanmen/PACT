from typing import List


def parse_music(music_string: str) -> List[int]:
    note_duration_map = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    durations = []

    for note in notes:
        durations.append(note_duration_map[note])

    return durations
