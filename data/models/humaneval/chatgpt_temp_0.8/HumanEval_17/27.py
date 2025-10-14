from typing import List

def parse_music(music_string: str) -> List[int]:
    note_dict = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    result = []
    
    for note in music_list:
        result.append(note_dict[note])
        
    return result
