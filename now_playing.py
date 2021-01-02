import os
from pathlib import Path
from pprint import pprint

HOME_PATH = str(Path.home())
DEFAULT_TABFS_PATH_FROM_TITLE = os.path.join(
    HOME_PATH, './tabfs/fs/mnt/tabs/by-title')


def rindex(haystack, needle):
    for index, item in enumerate(reversed(haystack)):
        if item == needle:
            return len(haystack) - index - 1


def nth_rindex(haystack, needle, nth):
    count = 0
    for index, item in enumerate(reversed(haystack)):
        if item == needle:
            count += 1
            if count == nth:
                return len(haystack) - index - 1


def get_seconds(timestamp):
    minutes, seconds = list(map(int, timestamp.split(':')))
    return minutes * 60 + seconds


def get_now_playing(tabfs_path_from_title=DEFAULT_TABFS_PATH_FROM_TITLE):
    tabs = os.listdir(tabfs_path_from_title)

    tab_with_youtube_music = ''
    for tab_name in tabs:
        if 'YouTube_Music' in tab_name:
            tab_with_youtube_music = tab_name

    if not tab_with_youtube_music:
        print('No open tabs with YouTube Music.. :(')
        exit(1)

    tab_directory_path = os.path.join(
        tabfs_path_from_title, tab_with_youtube_music)

    title_file_path = os.path.join(tab_directory_path, 'title.txt')
    text_file_path = os.path.join(tab_directory_path, 'text.txt')

    title = ''
    with open(title_file_path) as f:
        title = f.read().strip().replace(' - YouTube Music', '')

    music_text = []
    with open(text_file_path) as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:
                music_text.append(stripped_line)

    last_title_index = rindex(music_text, title)
    if last_title_index == None:
        fourth_dot_index = nth_rindex(music_text, '•', 2)
        title = music_text[fourth_dot_index - 2]
        last_title_index = rindex(music_text, title)

    player_information = music_text[last_title_index - 1:]

    progress, duration = player_information[0].split(' / ')
    artist = player_information[2]

    return {
        'title': title,
        'artist': artist,
        'progress': get_seconds(progress),
        'duration': get_seconds(duration),
    }


if __name__ == '__main__':
    music_information = get_now_playing()
    pprint(music_information, sort_dicts=False)
