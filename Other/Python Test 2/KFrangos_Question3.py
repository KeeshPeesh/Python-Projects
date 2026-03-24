import pandas as pd

data = {
    "Name": ['Alex', 'Sam', 'Jamie', 'Taylor', 'Jordan'],
    "hours_studied": [15, 8, 25, 4, 12],
    "exam_score": [82, 65, 94, 58, 78]
}
df = pd.DataFrame(data)


scoreof70 = df[df['exam_score'] > 70]
print("Passed:", len(scoreof70))

average_score = scoreof70['exam_score'].mean()
print("Average score: {:.1f}".format(average_score))