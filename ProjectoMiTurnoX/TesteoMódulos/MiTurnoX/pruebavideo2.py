import vlc

m = vlc.MediaPlayer("1.mp4")
media = vlc.Media("1.mp4")
m.set_media(media)
m.play()