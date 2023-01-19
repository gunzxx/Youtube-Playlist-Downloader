# Youtube-Playlist-Downloader

Ini merupakan project gabut saya ketika saya ingin mendownload video dari youtube tanpa harus ribet. Daripada saya menggunakan savefrom dan mendownload video satu-satu. Lebih baik saya membuat script sendiri untuk mendownload semua video di playlist sekaligus.


## Cara memasukkan link
Silahkan ganti link yg ada di dalam variabel yt_playlist dan ganti dengan link anda.

## Cara memilih resolusi
### High Resolusi -> default
Untuk mendownload resolusi tinggi anda tidak perlu mengubahnya, tinggal menggunakan scriptnya saja.

### Low Resolusi
Untuk mendownload resolusi tinggi, silahkan ganti get_highest_resolution() menjadi get_lowest_resolution().

### Custom Resolusi
Untuk custom resolusi yang ingin anda download, silahkan ganti get_highest_resolution() menjadi get_by_resolution("480p") jka ingin mendownload resolusi 480p.
Ganti 480p dengan parameter berikut : 
Parameter : Video resolution i.e. “720p”, “480p”, “360p”, “240p”, “144p”


## Mengganti custom path
Silahkan masukkan alamat folder pada download().
video.streams.get_highest_resolution().download()

Semisal kita ingin menaruh di Folder G:\Python\singger, maka ganti menjadi :
video.streams.get_highest_resolution().download("G:\Python\singger")


# Thanks
Silahkan dipakai, jangan lupa star nya ya!:)
