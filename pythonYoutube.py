from pytube import YouTube
link= input('Nhap link youtube: ')
yt = YouTube(link)
yt.streams.get_by_itag(22).download()

