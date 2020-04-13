# def cakes(recipe, available):
#     amount = None
#     times_list = []
#     if len(available) >= len(recipe):
#         for i in recipe.keys():
#             times_list.append(available[i] // recipe[i])
#         amount = min(times_list)
#     if amount is None:
#         return 0
#     return amount
#
#
# recipe = {'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
# available = {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}
# print(cakes(recipe, available))

#################### OR ######################################


def cakes(recipe, available):
    return min([available[ing] // recipe[ing] if ing in available else 0 for ing in recipe])
