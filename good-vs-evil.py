def good_vs_evil(good, evil):
    good_dict = {"hobbits": 1, "men": 2, "elves": 3, "dwarves": 3, "eagles": 4, "wizards": 10}
    evil_dict = {"orcs": 1, "men": 2, "wargs": 2, "goblins": 2, "uruk hai": 3, "trolls": 5, "wizards": 10}
    good_list = good.split(" ")
    evil_list = evil.split(" ")
    good_total = sum([(list(good_dict.values())[i] * int(good_list[i])) for i in range(len(good_list))])
    evil_total = sum([(list(evil_dict.values())[i] * int(evil_list[i])) for i in range(len(evil_list))])
    if good_total > evil_total:
        battle_result = "Good triumphs over Evil"
    elif evil_total > good_total:
        battle_result = "Evil eradicates all trace of Good"
    else:
        battle_result = "No victor on this battle field"
    return f"Battle Result: {battle_result}"


print(good_vs_evil('1 1 1 1 1 1', "1 1 1 1 1 1 1"))