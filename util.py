import constants as cte


def get_summoning_zone(field):
    for index, monster_zone in enumerate(field.monster_zones,0):
        if monster_zone:
            field.monster_zones[index] = False
            return cte.MONSTER_ZONES_STR[index]
    return None
