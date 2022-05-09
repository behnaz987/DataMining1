import pandas as pd
df = pd.read_excel('Real Data(1).xlsx', keep_default_na=False)


def average(lst):
    return int(sum(lst) / len(lst))


def clean_column(column_name, s, e):
    for i in range(0, 460):
        if df[column_name][i] not in range(s, e):
            df[column_name][i] = "x"

    df[column_name] = pd.to_numeric(df[column_name], errors='coerce').astype('Float64')
    df[column_name] = df[column_name].fillna(df[column_name].mean())
    return df[column_name]


def check_unique_value(column_name):
    cnt = 0
    visited = []

    for i in range(0, len(df[column_name])):

        if df[column_name][i] not in visited:
            visited.append(df[column_name][i])
            cnt += 1
            print(i)

    print("No.of unique values :",
          cnt)

    print("unique values :",
          visited)


def replace(column_name, old_to_new):
    df_column = df[column_name]
    df_column.replace(old_to_new, inplace=True)


if __name__ == '__main__':
    final1 = clean_column("نمره امتحان پایانی", 0, 21)
    second1 = clean_column("نمره در امتحان دوم", 0, 21)
    first1 = clean_column("نمره در امتحان اول", 0, 21)

    absent_count = clean_column("تعداد غیبت در طول سال", 0, 94)

    health_state = clean_column("وضعیت سلامت", 1, 5)

    friend_old_to_new = {'هفته"': 1, "هرگز !": 1, '"دوستی ندارم"': 1, 'هفته‌ای 6 بار': 5}
    replace("بیرون رفتن با دوستان ", friend_old_to_new)
    clean_column("وقت آزاد پس از مدرسه", 1, 5)

    quality_old_to_new = {"عالی": 4, "چهار": 4, 0: 1, '': 1}
    replace("کیفیت روابط خانوادگی", quality_old_to_new)

    # check_unique_value("تمایل به تحصیل در مقاطع بالاتر")
    # check_unique_value("مهد کودک")

    # check_unique_value("فعالیت خارج از برنامه")
    # check_unique_value("شرکت در کلاس خصوصی")
    # check_unique_value("تعداد پایه‌های رد شده")
    failed_count = clean_column("تعداد پایه‌های رد شده", 0, 4)

    # check_unique_value("سرپرست")
    # check_unique_value("زمان مطالعه هفتگی")
    # check_unique_value("زمان سفر")

    reason_old_to_new = {'"شهرت"': "شهرت"}
    replace("دلیل انتخاب این مدرسه", reason_old_to_new)

    job_old_to_new = {"others": "other", "Teacher": "teacher", "استاد دانشگاه": "teacher", "معلم خصوصی": "teacher",
                      "بازنشسته": "at_home", "/'at_home'/": "at_home", "teacherr": "teacher", "at home": "at_home",
                      "athom": "at_home",
                      "otherr": "other", '"at_home"': "at_home", '': "other"}
    replace("شغل پدر", job_old_to_new)
    replace("شغل مادر", job_old_to_new)

    edu_old_to_new = {'ابتدایی': 1, '': 0}
    replace("تحصیلات پدر", edu_old_to_new)

    state_old_to_new = {"زندگی مشترکک": "زندگی مشترک", "جدا از هم،": "جدا از هم"}
    replace("وضعیت زندگی مشترک والدین", state_old_to_new)

    child_count_old_to_new = {"LE3": "LT3", "تک فرزند": "LT3", "GT5": "GT3", '۵ فرزند': 'GT3', '4 فرزند': 'GT3'}
    replace("تعداد فرزندان خانواده", child_count_old_to_new)

    house_old_to_new = {"ملک استيجاري": "ملک استیجاری", "ملک شخصي": "ملک شخصی", '"ملک شخصی"': "ملک شخصی",
                        "شخصی": "ملک شخصی", "ملکشخصی": "ملک شخصی"
        , "استیجاری": "ملک استیجاری", "شخصي": "ملک شخصی"}
    replace("نوع مسکن", house_old_to_new)

    clean_column("سن", 15, 23)

    f_m_old_to_new = {"Girl": "دختر", '"G"': "دختر", "Meal": "پسر", "M": "پسر"}
    replace("جنسیت", f_m_old_to_new)