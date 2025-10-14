from typing import List


def parse_music(music_string: str) -> List[int]:
    duration = {'o': 4, 'o|': 2, '.|': 1}
    music_notes = music_string.split()
    duration_list = [duration[note] for note in music_notes]
    return duration_list
