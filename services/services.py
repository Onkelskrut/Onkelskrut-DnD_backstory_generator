from database.database import DICT_STORIES_RU
from random import choice


def generate_story():
    char_traits = choice(DICT_STORIES_RU['character_traits']).lower()
    char_race = choice(DICT_STORIES_RU['race_list'])
    char_prof = choice(DICT_STORIES_RU['profession_list'])
    char_appearance = choice(DICT_STORIES_RU['appearance_features'])
    char_features = choice(DICT_STORIES_RU['features'])
    char_prehistories = choice(DICT_STORIES_RU['pre_histories'])
    char_motivation = choice(DICT_STORIES_RU['motivation'])
    char_phobias = choice(DICT_STORIES_RU['phobias'])

    return f"Сегодня ты {char_traits} {char_race} - {char_prof}, {char_appearance}, {char_features}. {char_prehistories}, {char_motivation}. Среди твоих страхов {char_phobias}, но будь отважен и ты сможешь все преодолеть! Вперед! К приключениям!!!"