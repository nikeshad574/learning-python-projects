import re

story = "One day, a [adjective] [animal] named [name] decided to visit the [place]. It was a [weather] day, perfect for an adventure. Along the way, [name] met a [adjective] [another animal] who was looking for a [object]. Together, they decided to [verb] and search for the missing [object]. After hours of wandering through the [adjective] forest, they finally found it near a [place]. They celebrated by [verb ending in -ing], feeling very [emotion]. From that day on, [name] and the [another animal] became the best of friends."

matches  = re.findall(r'\[[^\]]*\]', story)
words = set(matches)
answers = {}

for word in words:
    newWord = input(f"Enter a word for {word}: ")
    answers[word] = newWord

for word in words:
    story = story.replace(word, answers[word])

print(f"\n {story}")