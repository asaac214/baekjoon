n = int(input())

a = input()
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
score = 0
for j in range(26):
    if a.count(alphabet[j]) > 0:
        score += ((j+1) * a.count(alphabet[j]))
print(score)
