##################  Q4  #################
from main import *
r = clean_columns()

def q_4():
    count = {
        'count_final': 0,
        'count_second': 0,
        'count_first': 0
    }
    for i in range(0, 460):
        if r[0][i] < 12:
            count['count_final'] += 1
        if r[1][i] < 12:
            count['count_second'] += 1
        if r[2][i] < 12:
            count['count_first'] += 1
    m = max(*count.values())
    for k, v in count.items():
        if v == m:
            print(k)
            return



if __name__ == '__main__':
    q_4()
