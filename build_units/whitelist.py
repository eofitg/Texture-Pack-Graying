import config_reader as cr


def exist(item):

    wl = 'whitelist.'
    #
    # blocks
    bl = wl + 'blocks.'
    # ladder
    if item.startswith('ladder') and cr.get(bl + 'ladder'):
        return True
    # wool
    if item.startswith('wool') and cr.get(bl + 'wool'):
        return True
    # bed
    if item.startswith('bed') and cr.get(bl + 'bed'):
        return True
    # tnt
    if item.startswith('tnt') and cr.get(bl + 'tnt'):
        return True
    # glass and glass pane
    if item.startswith('glass_') and item != 'glass_pane_top.png' and cr.get(bl + 'stained_glass'):
        return True
    if item.startswith('glass') and cr.get(bl + 'glass'):
        return True
    # harden clay
    if item.startswith('hardened_clay_') and cr.get(bl + 'stained_hardened_clay'):
        return True
    if item.startswith('hardened_clay') and cr.get(bl + 'hardened_clay'):
        return True
    # water
    if item.startswith('water_flow') and cr.get(bl + 'water.flow'):
        return True
    if item.startswith('water_still') and cr.get(bl + 'water.still'):
        return True
    # lava
    if item.startswith('lava_flow') and cr.get(bl + 'lava.flow'):
        return True
    if item.startswith('lava_still') and cr.get(bl + 'lava.still'):
        return True

    return False
