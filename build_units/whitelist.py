import config_reader as cr


def exist(item):

    wl = 'whitelist.'

    # # # # #
    # blocks
    bl = wl + 'blocks.'
    # ladder
    if item.startswith('ladder') and cr.get(bl + 'ladder'):
        return True
    # wood
    if item.startswith('log') and cr.get(bl + 'wood'):
        return True
    if item.startswith('planks') and cr.get(bl + 'wood'):
        return True
    # wool
    if item.startswith('wool') and cr.get(bl + 'wool'):
        return True
    # bed
    if item.startswith('bed_') and cr.get(bl + 'bed'):
        return True
    # tnt
    if item.startswith('tnt') and cr.get(bl + 'tnt'):
        return True
    # glass and glass pane
    if item.startswith('glass_') and item != 'glass_pane_top.png' and cr.get(bl + 'stained_glass'):
        return True
    if item.startswith('glass') and cr.get(bl + 'glass'):
        return True
    # portal
    if item.startswith('portal') and cr.get(bl + 'portal'):
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

    # # # # #
    # particle
    pa = wl + 'particle.'
    # footage
    if item.startswith('footage') and cr.get(pa + 'footage'):
        return True

    # # # # #
    # entity
    en = wl + 'entity.'
    # living
    livings = ['alex.png', 'bat.png', 'blaze.png', 'cat', 'chicken.png', 'cow', 'creeper',
               'enderdragon', 'enderman', 'endermite.png', 'ghast', 'guardian.png',
               'guardian_beam.png', 'guardian_elder.png', 'horse', 'iron_golem.png',
               'pig', 'rabbit', 'sheep', 'silverfish.png', 'skeleton', 'slime',
               'snowman.png', 'spider', 'spider_eyes.png', 'squid.png', 'steve.png',
               'villager', 'witch.png', 'wither', 'wolf', 'zombie', 'zombie_pigman.png']
    if item in livings and cr.get(en + 'living'):
        return True
    # armorstand
    if item.startswith('armorstand') and cr.get(en + 'armorstand'):
        return True
    # arrow
    if item.startswith('arrow') and cr.get(en + 'arrow'):
        return True
    # chest
    if item.startswith('chest') and cr.get(en + 'chest'):
        return True
    # banner
    if item.startswith('banner') and cr.get(en + 'banner'):
        return True
    # banner_base
    if item.startswith('banner_base') and cr.get(en + 'banner_base'):
        return True
    # beacon_beam
    if item.startswith('beacon_beam') and cr.get(en + 'beacon_beam'):
        return True
    # boat
    if item.startswith('boat') and cr.get(en + 'boat'):
        return True
    # enchanting table book
    if item.startswith('enchanting_table_book') and cr.get(en + 'enchanting_table_book'):
        return True
    # end_portal
    if item.startswith('end_portal') and cr.get(en + 'end_portal'):
        return True
    # endercrystal
    if item.startswith('endercrystal') and cr.get(en + 'endercrystal'):
        return True
    # experience orb
    if item.startswith('experience_orb') and cr.get(en + 'experience_orb'):
        return True
    # explosion particle
    if item.startswith('explosion') and cr.get(en + 'explosion'):
        return True
    # lead-knot
    if item.startswith('lead_knot') and cr.get(en + 'lead_knot'):
        return True
    # minecart
    if item.startswith('minecart') and cr.get(en + 'minecart'):
        return True
    # sign
    if item.startswith('sign') and cr.get(en + 'sign'):
        return True

    return False
