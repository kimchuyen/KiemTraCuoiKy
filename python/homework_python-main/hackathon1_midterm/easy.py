from datetime import date


# 1
def day_diff(release_date, code_complete_day):
    release_date = release_date.split("/")
    code_complete_day = code_complete_day.split("-")

    formatted_release_date = date(int(release_date[2]), int(release_date[1]), int(release_date[0]))
    formatted_code_complete_day = date(int(code_complete_day[0]), int(code_complete_day[2]), int(code_complete_day[1]))
    date_for_testing = formatted_release_date - formatted_code_complete_day
    return date_for_testing.days


# 2
def alpha_num(sentence):
    str_list = sentence.split()
    text_contain_num_list = []
    for i in str_list:
        if any(chr.isdigit() for chr in i):
            text_contain_num_list.append(i)
    return text_contain_num_list
