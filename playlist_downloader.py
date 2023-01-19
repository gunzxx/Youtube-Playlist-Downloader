from pytube import Playlist

# link = input("Link : ")

yt_playlist = Playlist("https://www.youtube.com/playlist?list=PL9At9z2rvOC-Z6Gt8uO1XMp4oyMlE3gml") #ganti link nya dengan link anda sendiri

for video in yt_playlist.videos:
    video.streams.get_highest_resolution().download()
    print("video : ", video.title)


print("\n done")
