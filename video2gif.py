from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("rat1.mp4")
videoClip.write_gif("rat1.gif")