try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("Something is missing {}".format(e))

# Accept the url first
url = input("Enter the url ")
file_type = int(input("Enter 1 for video and 2 for audio "))
title = YouTube(url).title
length = str(YouTube(url).length)
if file_type == 1:
    video = YouTube(url).streams.get_by_itag(137).download()
else:
    audio = YouTube(url).streams.get_by_itag(140).download()

print("File Downloaded Successfully")
print("Title of this video is " + title)
print("Length: " + length)

