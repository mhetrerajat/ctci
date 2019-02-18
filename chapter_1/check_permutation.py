# Check Permutation: Given two strings, write a method to decide if one is a  permutation of the other.

from collections import Counter


def check_permutation(strs):
    a,b = strs
    counter_a = Counter(a)
    counter_b = Counter(b)

    for char, count in counter_a.items():
        if counter_b.get(char, 0) != count:
            return False

    return True

def main():
    N = [
        (["abcd", "dcba"], True),
        (["abc", "pqr"], False)
    ]
    for (strs, answer) in N:
        assert check_permutation(strs) == answer


if __name__ == "__main__":
    main()
