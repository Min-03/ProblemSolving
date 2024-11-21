def string_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    s = s1 * 2
    return s2 in s

def string_compression(s: str) -> str:
    if len(s) == 0:
        return s
    ret = []
    prev = s[0]
    cnt = 1
    for i, ch in enumerate(s):
        if i != 0 and prev == ch:
            cnt += 1
        elif i != 0:
            ret.append(prev + str(cnt))
            prev = ch
            cnt = 1
    ret.append(prev + str(cnt))
    cat = ''.join(ret)
    return s if len(cat) >= len(s) else cat

if __name__ == "__main__":
    s1 = "abc"
    s2 = "bac"
    print(string_rotation(s1, s2))

    s = "aabaaa"
    print(string_compression(s))