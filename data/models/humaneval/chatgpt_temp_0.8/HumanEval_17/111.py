from typing import List


def parse_music(music_string: str) -> List[int]:
    note_duration = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    music_notes = music_string.split()
    duration_list = []
    
    for note in music_notes:
        duration = note_duration[note]
        duration_list.append(duration)
    
    return duration_list
