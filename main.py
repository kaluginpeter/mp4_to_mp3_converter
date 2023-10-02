import moviepy.editor
video = moviepy.editor.VideoFileClip('Rick_Roll.mp4')
audio = video.audio
audio.write_audiofile('rick.mp3')