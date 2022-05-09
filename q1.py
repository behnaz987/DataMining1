##################  Q1  #################
import matplotlib.pyplot as plt
from main import *
r = replace_columns()

def parent_job(person):
    father_job = r[2]
    mother_job = r[3]
    parent = df["سرپرست"]
    if parent[person] == "پدر":
        return father_job[person]
    if parent[person] == "مادر":
        return mother_job[person]
    if parent[person] == "دیگری":
        return None


parent_job2 = list()
for i in range(0, 460):
    parent_job2.append(parent_job(i))

df["شغل سرپرست"] = parent_job2


def q_1():
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    for j in range(0, 460):
        if df["شغل سرپرست"][j] == "at_home":
            s1 = s1 + df["نمره امتحان پایانی"][j]
            c1 += 1
        if df["شغل سرپرست"][j] == "health":
            s2 = s2 + df["نمره امتحان پایانی"][j]
            c2 += 1
        if df["شغل سرپرست"][j] == "teacher":
            s3 = s3 + df["نمره امتحان پایانی"][j]
            c3 += 1
        if df["شغل سرپرست"][j] == "other":
            s4 = s4 + df["نمره امتحان پایانی"][j]
            c4 += 1
        if df["شغل سرپرست"][j] == "services":
            s5 = s5 + df["نمره امتحان پایانی"][j]
            c5 += 1
    m1 = s1 / c1
    m2 = s2 / c2
    m3 = s3 / c3
    m4 = s4 / c4
    m5 = s5 / c5

    jobs = ['at_home', 'health', 'teacher', 'other', 'services']
    values = [m1, m2, m3, m4, m5]
    plt.figure(figsize=(10, 5))
    plt.bar(jobs, values, color='maroon', width=0.4)
    plt.show()


if __name__ == '__main__':
    q_1()
