glasnie = ['a','e','i','o','u','y']
songs = []
N = int(input())
for i in range(0,N):
    glasInsong = 0
    song = input()
    words = song.split(" ")
    for word in words:
        for leter in word:
            if(leter in glasnie):
                glasInsong += 1
    songs.append(glasInsong)

bigest = sorted(songs)[N-1]
index = songs.index(bigest)+1
print(index,bigest)
