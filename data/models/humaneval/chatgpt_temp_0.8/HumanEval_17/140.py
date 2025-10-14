from typing import List


def parse_music(music_string: str) -> List[int]:
    beats_dict = {'o': 4, 'o|': 2, '.|': 1}
    beats_list = []
    for note in music_string.split():
        beats_list.append(beats_dict[note])
    return beats_list
