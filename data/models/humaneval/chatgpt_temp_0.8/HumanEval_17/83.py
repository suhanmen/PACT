from typing import List


def parse_music(music_string: str) -> List[int]:
    beats_dict = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    return [beats_dict[note] for note in music_list]
