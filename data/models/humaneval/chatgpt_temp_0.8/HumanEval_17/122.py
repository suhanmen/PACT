from typing import List


def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}  # dictionary to store duration of each note
    music_list = music_string.split()  # split string into list of notes
    result = []
    for note in music_list:
        result.append(durations[note])  # append duration of each note to result list
    return result
