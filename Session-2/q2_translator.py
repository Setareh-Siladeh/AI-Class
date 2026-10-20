words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "hello": "سلام",
    "book": "کتاب",
    "student": "دانشجو",
    "school": "مدرسه",
    "computer": "کامپیوتر"
}

sentence = "I love python and AI"

translated_words = 0
not_translated_words = 0

sentence = sentence.lower()
word_list = sentence.split()

for word in word_list:
    if word in words:
        print(words[word], end=" ")
        translated_words = translated_words + 1
    else:
        print("[" + word + "]", end=" ")
        not_translated_words = not_translated_words + 1

print()

print("تعداد کلمات ترجمه‌شده:", translated_words)
print("تعداد کلمات ترجمه‌نشده:", not_translated_words)
