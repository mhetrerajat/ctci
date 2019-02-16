


def is_unique(s):
    for letter in s:
        if s.count(letter) > 1:
            return False

    return True

def main():
    N = [
            ("abcbab", False), ("abcd", True)
    ]
    for (s, answer) in N:
        assert is_unique(s) == answer
