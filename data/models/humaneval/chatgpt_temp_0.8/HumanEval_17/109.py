from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_values = {'o': 4, 'o|': 2, '.|': 1}  # dictionary to map note string to beat value
    note_list = music_string.split()  # split the string into individual note strings
    beat_list = []  # empty list to store beat values
    for note in note_list:
        beat_list.append(beat_values[note])  # append the beat value of the note to the beat list
    return beat_list
