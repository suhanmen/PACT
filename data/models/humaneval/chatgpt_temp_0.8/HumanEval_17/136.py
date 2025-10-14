from typing import List

def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1} # dictionary with note duration values
    parsed_music = []
    music_notes = music_string.split() # split the input string into individual notes

    for note in music_notes:
        parsed_music.append(durations[note]) # append the corresponding value to the parsed_music list

    return parsed_music
