##################  Q5  #################
from main import *
r = clean_columns()


def q_5():
    count = 0
    for i in range(0, 460):
        if df["شرکت در کلاس خصوصی"][i] == "yes":
            count += 1
    print((count / 460) * 100)
    cnt = 0
    for i in range(0, 460):
        if df["شرکت در کلاس خصوصی"][i] == "yes":
            if r[0][i] - r[1][i] >= 3:
                cnt += 1

    progress_percentage = (cnt / count) * 100
    if progress_percentage > 50:
        return "yes"
    else:
        return "no"


if __name__ == '__main__':
    print(q_5())
