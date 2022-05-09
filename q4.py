##################  Q4  #################
from main import *


def q_4():
    count = {
        'count_final': 0,
        'count_second': 0,
        'count_first': 0
    }
    for i in range(0, 460):
        if df["نمره امتحان پایانی"][i] < 12:
            count['count_final'] += 1
        if df["نمره در امتحان دوم"][i] < 12:
            count['count_second'] += 1
        if df["نمره در امتحان اول"][i] < 12:
            count['count_first'] += 1
    m = max(*count.values())
    for k, v in count.items():
        if v == m:
            print(k)
            return



if __name__ == '__main__':
    q_4()
