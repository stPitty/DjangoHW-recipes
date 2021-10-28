from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def calculate(request, dish):
    try:
        servings = int(request.GET.get('servings'))
    except TypeError:
        servings = 1
    recipe = {}
    if dish in DATA:
        for ingredient in DATA[dish]:
            quantity = round(DATA[dish][ingredient]*servings, 2)
            recipe[ingredient] = quantity
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context=context)
