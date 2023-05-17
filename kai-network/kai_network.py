# !/usr/bin/env python3

"""
Kai Network - Video Player Application

This Python-based video player application allows you to play videos from a playlist,
control playback, manage playback history, and more.

Author: CireWire, The Helix Corporation
Date: May 6, 2023

Usage:
- Execute the script directly to run the application.
- Make sure to have the required dependencies installed.
- Refer to the README file for detailed instructions.

"""

import pyglet
import requests
import io
import os
import cv2

# Initialize Pyglet
window = pyglet.window.Window(800, 600, fullscreen=True)
player = pyglet.media.Player()
playlist = [
    "http://example.com/video1.mp4",
    "http://example.com/video2.mp4",
    "http://example.com/video3.mp4",
]
current_video_index = 0
volume = 0.5
volume_step = 0.1
history = []
resume_playback = False
resume_text = None
resume_text_timeout = 3 * 60  # 3 seconds * 60 frames per second

# Generate video thumbnails
thumbnail_directory = "thumbnails"
if not os.path.exists(thumbnail_directory):
    os.makedirs(thumbnail_directory)

for video_path in playlist:
    response = requests.get(video_path)
    video_data = io.BytesIO(response.content)
    video_capture = cv2.VideoCapture(video_data)
    success, frame = video_capture.read()
    if success:
        thumbnail_path = os.path.join(
            thumbnail_directory, f"{os.path.basename(video_path)}.jpg"
        )
        cv2.imwrite(thumbnail_path, frame)
    video_capture.release()


def load_video(video_url):
    response = requests.get(video_url)
    video_data = io.BytesIO(response.content)
    source = pyglet.media.load(video_url, file=video_data)
    player.queue(source)


def play_video():
    if not player.playing:
        player.play()


def pause_video():
    if player.playing:
        player.pause()


def seek_video(seconds):
    player.seek(player.time + seconds)


def set_volume(volume_level):
    player.volume = volume_level


def save_playback_time():
    history.append(player.time)


def resume_playback():
    if len(history) > 0:
        player.seek(history[-1])
        history.pop(0)


def play_next_video():
    global current_video_index
    current_video_index = (current_video_index + 1) % len(playlist)
    load_video(playlist[current_video_index])


def play_previous_video():
    global current_video_index
    current_video_index = (current_video_index - 1) % len(playlist)
    load_video(playlist[current_video_index])


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        if player.playing:
            pause_video()
        else:
            play_video()
    elif symbol == pyglet.window.key.LEFT:
        seek_video(-10)
    elif symbol == pyglet.window.key.RIGHT:
        seek_video(10)
    elif symbol == pyglet.window.key.UP:
        volume_level = min(player.volume + volume_step, 1.0)
        set_volume(volume_level)
    elif symbol == pyglet.window.key.DOWN:
        volume_level = max(player.volume - volume_step, 0.0)
        set_volume(volume_level)
    elif symbol == pyglet.window.key.H:
        save_playback_time()
    elif symbol == pyglet.window.key.R:
        resume_playback()
    elif symbol == pyglet.window.key.N:
        play_next_video()
    elif symbol == pyglet.window.key.P:
        play_previous_video()


@window.event
def on_draw():
    window.clear()
    if player.source:
        player.get_texture().blit(0, 0)

        if resume_playback:
            if len(history) > 0:
                if player.time <= history[0]:
                    resume_text = "Resuming from history"


text_label = pyglet.text.Label(
    resume_text,
    font_name="Helvetica",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
    color=(119, 178, 140, 255),
)
text_label.draw()

# Load the initial video

load_video(playlist[current_video_index])

# Start the application

pyglet.app.run()
