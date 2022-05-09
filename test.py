from main import *
# df = pd.read_excel('Real Data(1).xlsx', keep_default_na=False)

if __name__ == '__main__':
    friend_old_to_new = {'هفته"': 1, "هرگز !": 1, '"دوستی ندارم"': 1, 'هفته‌ای 6 بار': 5}
    # replace("بیرون رفتن با دوستان ", friend_old_to_new)
    print(replace("بیرون رفتن با دوستان ", friend_old_to_new))
    # check_unique_value("بیرون رفتن با دوستان ")


