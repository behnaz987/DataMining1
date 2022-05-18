##################  Q2  #################
from matplotlib import pyplot as plt
import seaborn as sns

from main import *

r = replace_columns()


def q_2():
    # r[0] = df["بیرون رفتن با دوستان "]
    x = df["وقت آزاد پس از مدرسه"]
    z = df["زمان مطالعه هفتگی"]
    y = r[0]

    print(x.corr(y))
    print(x.corr(z))


if __name__ == '__main__':
    q_2()
