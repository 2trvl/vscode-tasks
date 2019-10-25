message = input()
key = 1
for letter in range(1, len(message)-1):
    base = message[:letter]
    part = message[letter:]
    if base == part:
        continue
    match = base.find(part)
    part = match + len(part) - 1
    if match != -1 and message[part] == base[-1]:
        print("YES\n" + message[:letter])
        key = 0
        break
if key:
    print("NO")