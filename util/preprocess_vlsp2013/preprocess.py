from os import listdir, remove
from os.path import join, exists
from os.path import dirname

# Preprocess Train Data
FOLDER = "../../data/vlsp2013"


folder1 = FOLDER + "/raw/WordSegmentationTask/Trainset/Trainset-Segmentation-1"
folder2 = FOLDER + "/raw/WordSegmentationTask/Trainset/Trainset-Segmentation-2"
count = 0
output_filepath = "tmp/train_dev.txt"

if exists(output_filepath):
    remove(output_filepath)
output = open(output_filepath, "a")

for file in listdir(folder1):
    lines = open(join(folder1, file)).readlines()
    lines = lines[3:-3]
    for line in lines:
        tags = ["<Date>", "</Date>", "<pTitle>", "</pTitle>", "<pHead>", "</pHead>", "<pBody>", "</pBody>", "<pAuthor>", "</pAuthor>",
                "<pInterTitle>", "</pInterTitle>", "<pAnswer>", "</pAnswer>", "<pQuestion>", "</pQuestion>", "<pSuperTitle>",
                "</pSuperTitle>", "<pSubTitle>", "</pSubTitle>"]
        is_break = False
        for tag in tags:
            if line.startswith(tag):
                is_break = True
                continue
        if is_break:
            continue
        output.write(line)
        count += 1
print("Number of sentences in Trainset-Segmentation-1 folder:", count)

count = 0
for file in listdir(folder2):
    for line in open(join(folder2, file)):
        if line.strip():
            output.write(line)
            count += 1
print("Number of sentences in Trainset-Segmentation-2 folder:", count)

# Preprocess Test Data
count = 0
folder = FOLDER + "/raw/Testset-POS"
output_filepath = "tmp/test.txt"
if exists(output_filepath):
    remove(output_filepath)
output = open(output_filepath, "a")
for file in listdir(folder):
    for line in open(join(folder, file)).readlines():
        tokens = line.split()
        tokens = [token.split("/")[0] for token in tokens]
        count += 1
        content = " ".join(tokens) + "\n"
        output.write(content)
print("Number of sentences in Testset:", count)


