from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}
    music_notes = music_string.split()
    beats_list = []
    for note in music_notes:
        beats_list.append(durations[note])
    return beats_list
