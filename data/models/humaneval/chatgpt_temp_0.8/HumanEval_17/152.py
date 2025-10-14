from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}
    beats = []
    for note in music_string.split():
        beats.append(durations[note])
    return beats
