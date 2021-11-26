import re
from datetime import date

# 1
def day_diff(release_date, code_complete_day):
    parsed_release = release_date.split("/")
    parsed_complete = code_complete_day.split("-")
    r_date = date(int(parsed_release[2]), int(parsed_release[1]), int(parsed_release[0]))
    c_date = date(int(parsed_complete[0]), int(parsed_complete[2]), int(parsed_complete[1]))
    delta = r_date - c_date
    return delta.days

# 2
def alpha_num(sentence):
    return re.findall("\w+\d+", sentence)