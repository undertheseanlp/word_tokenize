

def get_syllables():
    for line in open("data/train.txt"):
        tokens = line.strip().split(" ")
        for token in tokens:
            for syllabel in token.split("_"):
                yield syllabel

syllables = set()
for syllable in get_syllables():
    syllables.add(syllable)
open("tmp/syllables.txt", "w").write("\n".join(sorted(syllables)))
print(0)