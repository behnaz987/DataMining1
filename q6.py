##################  Q6  ##################
from main import *

def average(lst):
    return int(sum(lst) / len(lst))


def q_6():
    study_time = list(df["زمان مطالعه هفتگی"])
    count = 0
    teacher_parent_study = 0
    avg = average(study_time)
    for i in range(0, 460):
        if df["شغل پدر"][i] == "teacher" or df["شغل مادر"][i] == "teacher":
            teacher_parent_study = df["زمان مطالعه هفتگی"][i] + teacher_parent_study
            count += 1
    teacher_parent_study_avg = teacher_parent_study / count
    if teacher_parent_study_avg > avg:
        return "yes"
    else:
        return "no"


if __name__ == '__main__':
    print(q_6())