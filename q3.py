##################  Q3  #################
from main import *
r = replace_columns()

def q_3():
    count = 0
    for i in range(0, 460):
        if df["زمان سفر"][i] in [3 , 4]:
            if r[9][i] in ["ترجیح دوره", "شهرت"]:
                count += 1
            else:
                pass
        else:
            pass
    print(count)
    return count


if __name__ == '__main__':
    q_3()