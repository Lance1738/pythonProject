while True:
    def translate(word):
        result = ""
        for letter in word:
            if letter in "AEIOUaeiou":
                result = result + "f"
            else:
                result = result + letter
        return result


    print(translate(input("Enter a word: ")))
