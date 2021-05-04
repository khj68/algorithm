from collections import Counter
from collections import deque
from functools import reduce
import bisect
import heapq
import math

def solution(S):
    size_sum = {'music': 0, 'images': 0, 'movies': 0, 'other': 0}
    music = {'mp3', 'aac', 'flac'}
    image = {'jpg', 'bmp', 'gif'}
    movie = {'mp4', 'avi', 'mkv'}
    
    for s in S.split('\n'):
        ext, size = s.split(' ')
        ext = ext.split('.')[-1]
        size = int(size[:-1])

        if ext in music:
            size_sum['music'] += size
        elif ext in image:
            size_sum['images'] += size
        elif ext in movie:
            size_sum['movies'] += size
        else:
            size_sum['other'] += size

    return f"music {size_sum['music']}b\nimages {size_sum['images']}b\nmovies {size_sum['movies']}b\nother {size_sum['other']}b"

print(solution('my.song.mp3 11b\ngreatSong.flacccc 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b'))