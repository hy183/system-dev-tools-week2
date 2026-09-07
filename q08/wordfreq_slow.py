with open("words.txt", encoding="utf-8") as f:
    words = f.read().split()

unique = []
for word in words:
    if word not in unique:
        unique.append(word)

print("count=", len(unique))
