def main():
    def swapcases(str):
        str2 = ""
        for ch in str:
            if ord(ch) in range(65,91):
                str2 += chr(ord(ch) + 32);
            elif ord(ch) in range(97,123):
                str2 += chr(ord(ch) - 32);
        return str2

    sentence = "hello WORLD!"
    print(sentence)
    str = swapcases(sentence)
    print(str)
main()
