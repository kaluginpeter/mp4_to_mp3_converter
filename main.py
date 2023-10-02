import moviepy.editor

video = moviepy.editor.VideoFileClip('Path to your .mp4 file')

# Converting
audio = video.audio

# Save audio
audio.write_audiofile('Name your audio.mp3') # Ex: my_audio.mp3

# Run file