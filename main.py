from moviepy.editor import *
videoclip = VideoFileClip("blood.mp4")
audioclip = AudioFileClip("despacito1.mp3")

new_audioclip = CompositeAudioClip([videoclip.audio, audioclip])
videoclip.audio = new_audioclip
videoclip.write_videofile("output6.mp4")