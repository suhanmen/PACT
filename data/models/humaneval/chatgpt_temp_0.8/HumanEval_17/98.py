from typing import List


def parse_music(music_string: str) -> List[int]:
    note_duration = {"o": 4, "o|": 2, ".|": 1}  # dictionary to map note to duration
    music_list = music_string.split()  # split the music string by space
    durations = []
    for note in music_list:
        durations.append(note_duration[note])
    return durations
