from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    return [durations[note] for note in music_list]
