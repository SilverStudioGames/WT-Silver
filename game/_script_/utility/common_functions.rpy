init -1 python:
    # Import commonly used python modules
    import time
    import math
    import random
    import pygame
    import colorsys
    import itertools
    import os as system

    get_volume_preference = renpy.game.preferences.get_volume

    def num_to_word(n, readable=True):
        """Transcript numbers (integers) into readable words."""
        n = int(n)
        units = ("","one","two","three","four","five","six","seven","eight","nine")
        teens = ("","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen")
        tens = ("","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety")
        thousands = ("","thousand","million","billion","trillion","quadrillion","quintillion","sextillion","septillion","octillion","nonillion","decillion","undecillion","duodecillion","tredecillion","quattuordecillion","sexdecillion","septendecillion","octodecillion","novemdecillion","vigintillion")
        
        output = []
        if n == 0: 
            output.append("zero")
        else:
            s = str(n)
            groups = (len(s)+2)/3
            s = s.zfill(groups*3)

            for i in xrange(0, groups*3, 3):
                h,t,u = int(s[i]), int(s[i+1]), int(s[i+2])
                g = groups-(i/3+1)

                if h > 0:
                    output.append(units[h]+" hundred")
                if t > 1:
                    if u > 0:
                        output.append(tens[t]+"-"+units[u])
                    else:
                        output.append(tens[t])
                elif t == 1:
                    if u > 0:
                        output.append(teens[u])  
                    else:
                        output.append(tens[t])
                else:
                    if u > 0: 
                        output.append(units[u])

                if g > 0 and (h+t+u) > 0:
                    if i == (groups*3)-6:
                        output.append(thousands[g]+" and")
                    else:
                        output.append(thousands[g]+",")
                        
        if readable:
            output = " ".join(output)
        return output
        
    def clamp(n, smallest, largest):
        return max(smallest, min(n, largest))
        
    def white_tint(image):
        return im.MatrixColor(image, im.matrix.tint(1.1, 1.1, 1.1))

    def gray_tint(image):
        return im.Grayscale(image)

    def yellow_tint(image):
        return im.MatrixColor(image,  im.matrix.tint(1.2, 1.1, 0.7))
        
    def get_head_icon(name):
        return "interface/icons/head/head_"+str(name)+"_1.png"

    def get_zoom(image, xsize, ysize):
        if isinstance(image, basestring):
            image = im.Image(image)
        
        r = renpy.render(image, 800, 800, 0, 0)
        x, y = r.get_size()

        if xsize / x < ysize / y:
            return min(1.0, xsize / x)
        return min(1.0, ysize / y)
        
    def image_hover(image):
        """Returns slightly brighter image used during hover events"""
        return im.MatrixColor(image, im.matrix.brightness(0.12))

    def image_alpha(image, alpha=0.5):
        """Returns an image with changed alpha 0 - fully transparent 1 - fully visible"""
        return im.MatrixColor(image, im.matrix.opacity(alpha))
        
    def set_clipboard(txt):
        txt = str(txt)
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, txt.encode("utf-8"))
        
    def get_clipboard():
        clipboard = pygame.scrap.get(pygame.scrap.SCRAP_TEXT)
        if clipboard:
            return clipboard
        return None
        
    def evaluate(txt):
        return __import__('ast').literal_eval(txt)
        
    def set_text_color(day=True):
        # This function must be invoked in a new context by preferences screen
        renpy.show_screen("preferences")
        # Temporarily change interface color
        tmp_color = renpy.store.interface_color
        renpy.call_in_new_context("update_interface_color", "gray")
        if day:
            preferences.text_color_day = color_picker(get_rgb_list(preferences.text_color_day), False, "Day Text Colour")
            preferences.text_color_day = get_hex_string(preferences.text_color_day[0]/255.0, preferences.text_color_day[1]/255.0, preferences.text_color_day[2]/255.0)
        else:
            preferences.text_color_night = color_picker(get_rgb_list(preferences.text_color_night), False, "Night Text Colour")
            preferences.text_color_night = get_hex_string(preferences.text_color_night[0]/255.0, preferences.text_color_night[1]/255.0, preferences.text_color_night[2]/255.0)
        # Reset interface color
        renpy.call_in_new_context("update_interface_color", tmp_color)
    
    def reset_variables(*args):
        """Resets the given variables to their default values."""
        # Refer to renpy.ast.Default.set_default for implementation details
        defaults_set = renpy.store._defaults_set
        changed_set = renpy.store.__dict__.ever_been_changed
        for arg in args:
            if arg in defaults_set:
                if arg in changed_set:
                    defaults_set.remove(arg)
                    changed_set.remove(arg)
            elif config.developer:
                raise Exception("The variable `{}` was not previously set with a default value.".format(arg))
        renpy.execute_default_statement(False)
    
    def disable_game_menu():
        store._tmp_menu = store._game_menu_screen
        store._game_menu_screen = None

    def enable_game_menu():
        if hasattr(store, "_tmp_menu"):
            store._game_menu_screen = store._tmp_menu
            del store._tmp_menu

    def set_use_drawable_resolution():
        config.use_drawable_resolution = preferences.use_drawable_resolution
        config.drawable_resolution_text = preferences.use_drawable_resolution
        renpy.force_full_redraw()
        if preferences.fullscreen:
            renpy.reset_physical_size()
            preferences.fullscreen = True
        else:
            s = renpy.get_physical_size()
            renpy.set_physical_size(s)

    def make_revertable(obj):
      if isinstance(obj, _list):
        return [make_revertable(x) for x in obj]
      elif isinstance(obj, _dict):
        return dict([(make_revertable(k), make_revertable(v)) for (k,v) in obj.iteritems()])
      else:
        return obj