##################  Q7  #################
import pandas as pd
from main import *

df = pd.read_excel('Real Data(1).xlsx', keep_default_na=False)
r = clean_columns()

def q_7():
    count = {
        'fsl': 0,
        'fls': 0,
        'sfl': 0,
        'slf': 0,
        'lfs': 0,
        'lsf': 0
    }
    for i in range(0, 460):
        last = r[0][i]
        second = r[1][i]
        first = r[2][i]

        if first >= second >= last:
            count['fsl'] += 1
        elif first >= last >= second:
            count['fls'] += 1
        elif second >= first >= last:
            count['sfl'] += 1
        elif second >= last >= first:
            count['slf'] += 1
        elif last >= first >= second:
            count['lfs'] += 1
        elif last >= second >= first:
            count['lsf'] += 1
    m = max(*count.values())
    for k, v in count.items():
        if v == m:
            print(k)
            return


if __name__ == '__main__':
    q_7()

#     f = first , s = second , l = last
