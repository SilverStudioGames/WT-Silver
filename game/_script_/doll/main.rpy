init python:
    class Doll(DollMethods):
        def __init__(self, name, clothes, face, body):
            self.wardrobe = {}
            self.wardrobe_list = []
            self.blacklist = []
            self.outfits = []
            self.name = name
            self.clothes = clothes
            self.face = DollFace(self, face)
            self.body = DollBody(self, body)
            self.pose = None
            
            self.rebuild_image()
        
        def rebuild(self, *args):
            """Rebuild all character images. Useful for debugging."""
            self.body.rebuild_image()
            self.face.rebuild_image()
            for o in self.wardrobe_list:
                o.rebuild_image()
                o.build_icon()
            for o in self.outfits:
                o.rebuild_image()
            self.rebuild_image()
            
        def build_image(self):
            # Add body, face, clothes, masks
            masks = []
            sprites = [[self.body.get_image(), 0], [self.face.get_image(), 1]]
            
            for o in self.clothes.itervalues():
                if o[0] and o[2]:
                    sprites.append([o[0].get_image(), o[0].zorder])
                    if o[0].back:
                        sprites.extend([x, -100+n+o[0].zorder] for n, x in enumerate(o[0].get_back()))
                        if o[0].back_outline:
                            sprites.append([o[0].back_outline, -100+o[0].zorder+o[0].layers])
                    if o[0].front:
                        sprites.extend([x, 100+n+o[0].zorder] for n, x in enumerate(o[0].get_front()))
                        if o[0].front_outline:
                            sprites.append([o[0].front_outline, 100+o[0].zorder+o[0].layers])
                    if o[0].armfix:
                        sprites.extend([["{}armleft/{}_fix.png".format(self.body.imagepath, self.body.get_part("armleft")), o[0].zorder+0.5], ["{}armright/{}_fix.png".format(self.body.imagepath, self.body.get_part("armright")), o[0].zorder+0.5]])
                    if o[0].mask:
                        masks.append([o[0].mask, o[0].zorder-1])
                        
            sprites.sort(key=lambda x: x[1])

            back_sprites = [x for x in sprites if x[1] < 0]
            sprites = [x for x in sprites if x[1] >= 0]

            # Apply alpha mask
            for m in sorted(masks, key=lambda x: x[1]):
                for i, s in enumerate(sprites):
                    if m[1] <= s[1]:
                        if i > 0:
                            masked = tuple(itertools.chain.from_iterable(((0,0), x[0]) for x in sprites[:i]))
                            c = AlphaMask(Composite(self.size, *masked), m[0])
                            sprites = sprites[i:]
                            sprites.insert(0, (c, m[1]-1))
                        break
            
            sprites = back_sprites + sprites
            
            sprites = tuple(itertools.chain.from_iterable(((0,0), x[0]) for x in sprites))
            return sprites
            
        def apply_transition(self):
            if renpy.get_screen("{}_main".format(self.name)):
                apply_doll_transition(self, "{}_main".format(self.name), "{}_img".format(self.name), eval("use_{}_head".format(self.name)))
            
        def equip(self, obj):
            """Takes DollCloth or DollOutfit object to equip."""
            if isinstance(obj, DollCloth):
                self.clothes[obj.type][0], self.clothes[obj.type][2] = obj, True
                if self.pose:
                    obj.set_pose(self.pose)
            elif isinstance(obj, DollOutfit):
                self.unequip("all")
                for i in obj.group:
                    self.clothes[i.type][0] = i.parent
                    self.clothes[i.type][0].set_color(i.color)
                    if self.pose:
                        i.parent.set_pose(self.pose)
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)
            
        def unequip(self, *args):
            """Takes argument(s) containing string cloth type(s) to unequip."""
            if "all" in args:
                for k, v in self.clothes.iteritems():
                    if not k.startswith(self.blacklist_unequip):
                        if self.pose:
                            v[0].set_pose(None)
                        v[0], v[2] = None, True
            else:
                for arg in args:
                    if self.pose and self.clothes[arg][0]:
                        self.clothes[arg][0].set_pose(None)
                    self.clothes[arg][0] = None
                
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)
            
        def get_equipped(self, type):
            """Takes argument containing string cloth type. Returns equipped object for cloth type."""
            return self.clothes[type][0]
                    
        def strip(self, *args):
            """Takes argument(s) containing string cloth type(s) to temporarily displace (hide)."""
            if "all" in args:
                for k, v in self.clothes.iteritems():
                    if not k.startswith(self.blacklist_toggles):
                        v[2] = False
            else:
                for arg in args:
                    if arg.startswith(self.blacklist_toggles):
                        for k in self.clothes.iterkeys():
                            if k.startswith(arg):
                                self.clothes[k][2] = False
                    else:
                        self.clothes[arg][2] = False
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)
                    
        def wear(self, *args):
            """Takes argument(s) containing string cloth type(s) to put on (unhide)."""
            if "all" in args:
                for v in self.clothes.itervalues():
                    v[2] = True
            else:
                for arg in args:
                    if arg.startswith(self.blacklist_toggles):
                        for k in self.clothes.iterkeys():
                            if k.startswith(arg):
                                self.clothes[k][2] = True
                    else:
                        self.clothes[arg][2] = True
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)
            
        def toggle_wear(self, type):
            """Takes argument containing string cloth type to toggle visibility (hide/unhide). Used in wardrobe."""
            if type.startswith(self.blacklist_toggles):
                for k, v in self.clothes.iteritems():
                    if k.startswith(type):
                        v[2] = not v[2]
            else:
                self.clothes[type][2] = not self.clothes[type][2]
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)
            
        def is_worn(self, type):
            """Takes argument containing string cloth type. Returns True if worn, False if hidden, None if not equipped at all."""
            if type.startswith(self.blacklist_toggles):
                for k, v in self.clothes.iteritems():
                    if k.startswith(type) and v[0]:
                        return True if v[2] else False
            else:
                if self.clothes[type][0]:
                    return True if self.clothes[type][2] else False
            return None
            
        def set_face(self, **kwargs):
            """Takes keyword argument(s) with the string name of expression file(s)."""
            for arg, value in kwargs.iteritems():
                if value not in (self.face.face[str(arg)][0], False):
                    self.face.face[str(arg)][0] = value
            self.face.rebuild_image()
            self.rebuild_image()
            
        def set_body(self, **kwargs):
            """Takes keyword argument(s) with the string name of body part file(s)."""
            for arg, value in kwargs.iteritems():
                if value != self.body.body[str(arg)][0]:
                    self.body.body[str(arg)][0] = value
            self.body.rebuild_image()
            self.rebuild_image()
            
        def set_pose(self, pose):
            if pose is None or renpy.loadable("characters/{}/poses/{}".format(self.name, pose)):
                self.pose = pose
                self.face.set_pose(pose)
                self.body.set_pose(pose)
                for v in self.clothes.itervalues():
                    if v[0]:
                        v[0].set_pose(pose)
                self.rebuild_image()
                self.apply_transition()
            else:
                raise IOError("'{}' pose doesn't exist for character named '{}'.".format(pose, self.name))
            
        def reset_blacklist(self, unequip=True):
            """Resets wardrobe blacklist based on worn clothes. Takes optional argument that causes blacklisted clothes to be unequipped."""
            self.blacklist = []
            for v in self.clothes.itervalues():
                if v[0] and v[0].blacklist:
                    self.blacklist.extend(x for x in v[0].blacklist if x not in self.blacklist)
            if unequip and self.blacklist:
                self.unequip(*self.blacklist)
                    
        def is_blacklisted(self, type):
            """Takes string cloth type. Returns True if cloth type is blacklisted."""
            return True if type in self.blacklist else False
            
        def create_outfit(self):
            """Creates a copy of the current character clothes and stores it."""
            return DollOutfit([x[0] for x in self.clothes.itervalues() if x[0]], True)
            
        def get_schedule(self):
            """Returns a list of outfits available for current daytime and weather conditions."""
            global daytime, raining, snowing, blizzard, storm, cloudy
            schedule = []
            
            for o in self.outfits:
                if o.unlocked and o.schedule["day" if daytime else "night"]:
                    if (storm or cloudy) and o.schedule["cloudy"]:
                        schedule.append(o)
                    elif raining and o.schedule["rainy"]:
                        schedule.append(o)
                    elif (snowing or blizzard) and o.schedule["snowy"]:
                        schedule.append(o)
                    elif not (cloudy or storm or raining or snowing or blizzard) and not (o.schedule["cloudy"] or o.schedule["rainy"] or o.schedule["snowy"]):
                        schedule.append(o)
            return schedule
                        
        def equip_random_outfit(self):
            """Equips random outfit based on Outfits Schedule."""
            schedule = self.get_schedule()
            
            if schedule:
                self.equip(renpy.random.choice(schedule))
            