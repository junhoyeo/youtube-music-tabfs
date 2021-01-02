# Youtube Music TabFS

Python Proof of Concept for retrieving **Now Playing** on YouTube Music with [TabFS](https://github.com/osnr/TabFS).

```python
music_information = get_now_playing()
pprint(music_information)
```

```json
{
  "title": "Ruthless(피처링: 제이 크리치)",
  "artist": "Lil Tjay",
  "progress": 94,
  "duration": 245
}
```

- Optional Parameter `tabfs_path_from_title` is available in `get_now_playing`. Default value is `./tabfs/fs/mnt/tabs/by-title` under the current user's home directory.

- `progress` and `duration` are in numbers.
