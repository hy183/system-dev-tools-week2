with open("words.txt", encoding="utf-8") as f:
    words = f.read().split()

unique = set()
for word in words:
    unique.add(word)

print("count=", len(unique))
