ALPHA = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

def solution(encrypted_text, key, rotation):
    key_num = []
    result = []
    for k in key:
        key_num.append(ALPHA[k])
    text = list(encrypted_text)
    if rotation >= 0:
        head = text[rotation:]
        tail = text[:rotation]
        text = head + tail
    else:
        head = text[abs(rotation):]
        tail = text[:abs(rotation)]
        text = head + tail
    for i in range(len(text)):
        text[i] = ALPHA[text[i]] - key_num[i]
        if text[i] < 1:
            text[i] = text[i] + 26
    alpha = {j:p for p, j in ALPHA.items()}
    for num in text:
        result.append(alpha[num])
    answer = ''.join(result)
    return answer
encrypted_text = "qyyigoptvfb"
key = "abcdefghijk"
rotation = 3

print(solution(encrypted_text, key, rotation))