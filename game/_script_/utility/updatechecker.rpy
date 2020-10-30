
define update_available = check_for_updates()

init python:
    config.after_load_callbacks.append(update_savefile)

init -1 python:
    import urllib2

    def check_for_updates():
        if persistent.lastupdatechecktime == None:
            persistent.lastupdatechecktime = __import__('time').time()

        if persistent.lastupdatechecktime+86400.0 < __import__('time').time():
            updt_website = urllib2.Request(binascii.unhexlify("68747470733a2f2f706173746562696e2e636f6d2f7261772f424e354261647639"))
            try:
                updt_website2 = urllib2.urlopen(updt_website, timeout=5)
                version_check = updt_website2.read()
                return False if float(config.version) >= float(version_check) else True
            except:
                pass
        return False

    # Groundwork for future save compatibility patches
    def check_save_compatibility(slot, page=None):
        save_version = FileJson(slot, "_version", missing=0, page=page)
        if save_version is not None:
            try:
                return float(save_version) >= compatible_version
            except ValueError: # (Old version fallback with letters)
                return False
        else:
            return True # Slot is empty

    # Save compatibility patches
    def update_savefile():
        global save_internal_version

        try:
            if save_internal_version:
                pass
        except NameError:
            save_internal_version = 1.39

        # Apply update to old save

        if float(save_internal_version) < 1.391:

            # Fix cardgame images
            for card in cards_dynamic:
                if renpy.loadable(card.imagepath):
                    continue

                card.imagepath = card.imagepath.split("_v")[0] + "_v{}.webp".format(geniecard_level)

            # Fix events with empty event tiers and/or zero start_tier
            all_events = [hg_pf_talk_tonks] + list(hg_favor_list) + list(hg_requests_list) + list(cc_favor_list) + list(cc_requests_list) + [ag_st_imperio, ag_se_imperio_sb] + [ll_pf_masturbate, ll_pf_blowjob, ll_pf_sex] + [nt_he_drink, nt_he_story] + list(nt_requests_list)

            for ev in all_events:
                if ev.start_tier == 0:
                    ev.start_tier = 1
                for i, l in enumerate(ev.events):
                    if not l:
                        del ev.events[i]

            # Update bra and glasses

            # Remove old references to avoid doubling items.
            for c in (her_accessory4_vintage_glasses, her_bra_base1):
                cat, subcat = c.categories

                hermione.wardrobe_list.remove(c)
                hermione.wardrobe[cat][subcat].remove(c)

            # Re-initialize
            her_accessory4_vintage_glasses.__init__("hermione", ("head", "glasses"), "accessory4", "vintage_glasses", [[255, 255, 255, 50], [36, 36, 36, 255], [116, 116, 116, 255]], unlocked=True, zorder=3)
            her_bra_base1.__init__("hermione", ("bras", "bras"), "bra", "basic_bra_1", [[232, 232, 232, 255], [202, 60, 1, 255]], unlocked=True)

            # Replace old clones in outfits that contain the above items.
            for o in hermione.outfits:
                for item in o.group:
                    if any((x.type == item.type and x.id == item.id) for x in (her_accessory4_vintage_glasses, her_bra_base1)):
                        indx = o.group.index(item)

                        if item.id == "vintage_glasses":
                            o.group[indx] = her_accessory4_vintage_glasses.clone()
                        elif item.id == "basic_bra_1":
                            o.group[indx] = her_bra_base1.clone()

            hermione.rebuild()

            # Need to update the screen scope or face IOErrors
            if renpy.get_screen("hermione_main"):
                scope = renpy.get_screen("hermione_main").scope
                scope["hermione_img"] = apply_doll_transition(hermione.get_image(), "hermione_main", use_hermione_head)

            save_internal_version = 1.391
            renpy.block_rollback()

        if float(save_internal_version) < 1.392:

            # Fix events with empty event tiers and/or zero start_tier, but do it properly this time...
            # We need to iterate over a copy of the events list if we aim to remove elements from the original list.
            all_events = [hg_pf_talk_tonks] + list(hg_favor_list) + list(hg_requests_list) + list(cc_favor_list) + list(cc_requests_list) + [ag_st_imperio, ag_se_imperio_sb] + [ll_pf_masturbate, ll_pf_blowjob, ll_pf_sex] + [nt_he_drink, nt_he_story] + list(nt_requests_list)

            for ev in all_events:
                # Remove empty lists
                for l in list(ev.events):
                    if not l:
                        ev.events.remove(l)

                # Fix start_tiers
                if ev.start_tier == 0:
                    ev.start_tier = 1

                # Fix max tiers integer
                if ev._max_tiers != len(ev.events):
                    ev._max_tiers = len(ev.events)

                # Fix actual tier integer, using correct setter function
                if ev._tier > (ev._max_tiers-1):
                    ev.tier = ev._max_tiers

            save_internal_version = 1.392
            renpy.block_rollback()

        if float(save_internal_version) < 1.393:

            cho_outfits_list.append(cc_japanese_school_uniform_ITEM)
            outfit_linking[cc_japanese_school_uniform_ITEM.id] = "cho_outfit_j_school"

            # Update fixed clothes
            ast_gloves_ann.armfix = False
            ton_panties_base.armfix = True
            cho_stockings_sailor1.armfix = True
            cho_stockings_lace1.armfix = True
            cho_stockings_pantyhose.armfix = True
            cho_stockings_fishnet.armfix = True

            astoria.rebuild()
            tonks.rebuild()
            cho.rebuild()

            misc_deco_list.append(fireplace_halloween_ITEM)
            misc_deco_list.append(cupboard_halloween_ITEM)
            misc_deco_list.append(phoenix_halloween_ITEM)

            mr_evs_list.insert(0, mr_ev_SNR)

            if hg_pr_flirt.is_event_complete(1, 1) and her_reputation < 6:
                her_reputation = 6

            save_internal_version = 1.393
            renpy.block_rollback()
