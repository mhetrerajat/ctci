# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string



def urlify(source):
    result = []
    for item in source.strip():
        if item == " ":
            item = "%20"
        result.append(item)

    return "".join(result)

def main():
    N = [
        ("Mr John Smith ", "Mr%20John%20Smith")
    ]
    for (source, target) in N:
        assert urlify(source) == target


if __name__ == "__main__":
    main()
