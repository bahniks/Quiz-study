import os

studies = ["Login",
           "Mindset",
           "Quiz",
           "Overconfidence",
           "Demographics",
           "Ending"
           ]


columns = {"Login": ("id"),
           "Mindset": ("id", "trial", "answer", "item"),
           "Quiz": ("id", "question_number", "answer"),
           "Overconfidence": ("id", "questions_correct", "percentile"),
           "Demographics": ("id", "sex", "age", "language", "student", "field"),
           "Ending": ("id")
           }

frames = ["Login",
          "Introduction",
          "Mindset",
          "Quiz",
          "Overconfidence",
          "Demographics",
          "Ending",
          "end"
         ]

for study in studies:
    with open("{} results.txt".format(study), mode = "w", encoding="utf-8") as f:
        f.write("\t".join(columns[study]))

with open("Time results.txt", mode = "w", encoding="utf-8") as times:
    times.write("\t".join(["id", "order", "frame", "time"]))

files = os.listdir()
for file in files:
    if ".py" in file or "results" in file or "file.txt" in file or "STATION" in file or ".txt" not in file:
        continue

    with open(file, encoding="utf-8") as datafile:
        #filecount += 1 #
        count = 1
        for line in datafile:

            study = line.strip()
            if line.startswith("time: "):
                with open("Time results.txt", mode = "a", encoding="utf-8") as times:
                    times.write("\n" + "\t".join([file, str(count), frames[count-1], line.split()[1]]))
                    count += 1
                    continue
            if study in studies:
                with open("{} results.txt".format(study), mode = "a", encoding="utf-8") as results:
                    for line in datafile:
                        content = line.strip()
                        if not content or content.startswith("time: "):
                            break
                        else:
                            results.write("\n" + content)