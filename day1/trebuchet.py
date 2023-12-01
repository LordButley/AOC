data = open("day1\calibration.txt", "r")
words_to_digits = {
    "one":"o1e",
    "two":"t2o",
    "three":"th3ee",
    "four":"f4ur",
    "five":"f5ve",
    "six":"s6x",
    "seven":"se7en",
    "eight":"ei8ht",
    "nine":"n9ne"
}
answer = 0
for line in data:
    for word in words_to_digits:
        line = line.replace(word, words_to_digits[word])
    numbers = [i for i in line if i.isdigit()]
    if len(numbers) == 1:
        numbers = numbers[0] + numbers[0]
    else:
        numbers = numbers[0] + numbers[-1]
    answer += int(numbers)
print(answer)