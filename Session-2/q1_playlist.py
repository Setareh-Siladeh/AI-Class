playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]

print("تعداد آهنگ‌ها:", len(playlist))

print("اولین آهنگ:", playlist[0])
print("آخرین آهنگ:", playlist[-1])

playlist.append("Dynamite")
playlist.remove("Believer")

playlist.sort()

print("لیست مرتب‌شده:")

for i, song in enumerate(playlist, start=1):
    print(f"{i}. {song}")