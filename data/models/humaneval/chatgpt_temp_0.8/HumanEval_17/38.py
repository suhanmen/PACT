from typing import List


def parse_music(music_string: str) -> List[int]:
    notes_duration = {"o": 4, "o|": 2, ".|": 1}
    notes_list = music_string.split()
    result = []
    
    for note in notes_list:
        result.append(notes_duration[note])
        
    return result
