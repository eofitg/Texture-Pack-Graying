import config_reader as cr


def exist(item):

    wl = 'whitelist.'

    ''' Blocks '''
    bl = wl + 'blocks.'
    # ladder
    if item.startswith('ladder') and cr.get(bl + 'ladder'):
        return True
    # wood
    if item.startswith(('log', 'planks')) and cr.get(bl + 'wood'):
        return True
    # wool
    if item.startswith('wool') and cr.get(bl + 'wool'):
        return True
    # end stone
    if item.startswith('end_stone') and cr.get(bl + 'end_stone'):
        return True
    # bed
    if item.startswith('bed_') and cr.get(bl + 'bed'):
        return True
    # tnt
    if item.startswith('tnt') and cr.get(bl + 'tnt'):
        return True
    # glass and glass pane
    if item in {'glass.png', 'glass_pane_top.png'} and cr.get(bl + 'glass'):
        return True
    # stained-glass and stained-glass pane
    if item.startswith('glass_') and item != 'glass_pane_top.png' and cr.get(bl + 'stained_glass'):
        return True
    # portal
    if item.startswith('portal') and cr.get(bl + 'portal'):
        return True
    # hardened clay
    if item == 'hardened_clay.png' and cr.get(bl + 'hardened_clay'):
        return True
    # stained hardened clay
    if item.startswith('hardened_clay_') and cr.get(bl + 'stained_hardened_clay'):
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

    ''' Entity '''
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
    # banner base
    if item.startswith('banner_base') and cr.get(en + 'banner_base'):
        return True
    # beacon beam
    if item.startswith('beacon_beam') and cr.get(en + 'beacon_beam'):
        return True
    # boat
    if item.startswith('boat') and cr.get(en + 'boat'):
        return True
    # enchanting table book
    if item.startswith('enchanting_table_book') and cr.get(en + 'enchanting_table_book'):
        return True
    # end portal
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

    ''' Environment '''
    envir = wl + 'environment.'
    # clouds
    if item.startswith('clouds') and cr.get(envir + 'clouds'):
        return True
    # end sky
    if item.startswith('end_sky') and cr.get(envir + 'end_sky'):
        return True
    # moon
    if item.startswith('moon') and cr.get(envir + 'moon'):
        return True
    # rain
    if item.startswith('rain') and cr.get(envir + 'rain'):
        return True
    # snow
    if item.startswith('snow') and cr.get(envir + 'snow'):
        return True
    # sun
    if item.startswith('sun') and cr.get(envir + 'sun'):
        return True

    ''' GUI '''
    gu = wl + 'gui.'
    # achievement
    if item.startswith('achievement') and cr.get(gu + 'achievement'):
        return True
    # book
    if item.startswith('book') and cr.get(gu + 'book'):
        return True
    # container
    if item.startswith('container') and cr.get(gu + 'container'):
        return True
    # demo background
    if item.startswith('demo_background') and cr.get(gu + 'demo_background'):
        return True
    # icons
    if item.startswith('icons') and cr.get(gu + 'icons'):
        return True
    # options background
    if item.startswith('options_background') and cr.get(gu + 'options_background'):
        return True
    # preset world icon for new world generation
    if item.startswith('presets') and cr.get(gu + 'presets'):
        return True
    # selection arrow in resource pack menu
    if item.startswith('resource_packs') and cr.get(gu + 'resource_packs'):
        return True
    # server selections
    if item.startswith('server_selections') and cr.get(gu + 'server_selections'):
        return True
    # spectator widgets
    if item.startswith('spectator_widgets') and cr.get(gu + 'spectator_widgets'):
        return True
    # stream indicator
    if item.startswith('stream_indicator') and cr.get(gu + 'stream_indicator'):
        return True
    # title text and background image
    if item.startswith('title') and cr.get(gu + 'title'):
        return True
    # widgets
    if item.startswith('widgets') and cr.get(gu + 'widgets'):
        return True

    ''' Misc '''
    mi = wl + 'misc.'
    # enchanted item glint
    if item.startswith('enchanted_item_glint') and cr.get(mi + 'enchanted_item_glint'):
        return True
    # force-field
    if item.startswith('forcefield') and cr.get(mi + 'forcefield'):
        return True
    # pumpkin-blur
    if item.startswith('pumpkinblur') and cr.get(mi + 'pumpkinblur'):
        return True
    # dark shadow under entities
    if item.startswith('shadow') and cr.get(mi + 'shadow'):
        return True
    # color fog while player is under the water, vanilla is light blue
    if item.startswith('underwater') and cr.get(mi + 'underwater'):
        return True
    # unknown pack icon
    if item.startswith('unknown_pack') and cr.get(mi + 'unknown_pack'):
        return True
    # unknown server icon
    if item.startswith('unknown_server') and cr.get(mi + 'unknown_server'):
        return True
    # black vignette effect around the screen
    if item.startswith('vignette') and cr.get(mi + 'vignette'):
        return True

    ''' Particle '''
    pa = wl + 'particle.'
    # footprint
    if item.startswith('footprint') and cr.get(pa + 'footprint'):
        return True
    # most of the vanilla particles
    if item.startswith('particles') and cr.get(pa + 'particles'):
        return True

    return False
