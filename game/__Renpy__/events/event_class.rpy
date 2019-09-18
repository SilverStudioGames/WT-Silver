init python:
    class quest_class(object):
        def __init__(self, **kwargs):
            self.title = ""
            self.hint = ""

            self.__dict__.update(kwargs)

        def status(self):
            return list(self.__dict__)


    class counter_class(object):
        def __init__(self, **kwargs):
            self.title       = ""
            self.bool        = False # Can me switched to 'True' and 'False' for events
            self.trigger     = False # Can only be switched to 'True'
            self.counter     = 0

            self.hg_counter  = 0 # Hermione
            self.gw_counter  = 0 # Ginny
            self.cc_counter  = 0 # Cho
            self.ll_counter  = 0 # Luna
            self.sb_counter  = 0 # Susan
            self.ag_counter  = 0 # Astoria
            self.dg_counter  = 0 # Daphne
            self.pp_counter  = 0 # Pansy
            self.ss_counter  = 0 # Snape
            self.nt_counter  = 0 # Tonks

            self.__dict__.update(kwargs)

        def status(self):
            return list(self.__dict__)

        def triggered(self):
            self.trigger = True
            self.counter += 1
            return


    class event_class(object):
        def __init__(self, **kwargs):
            self.title     = ""
            self.hint      = ""
            self.counter   = 0

            self.start_label = ""
            self.start_tier = 0
            self.inProgress = False

            self.events = []

            self.icons = []
            self.iconset = []

            # Private attributes
            self._tier     = 0
            self._points    = 0

            self.__dict__.update(kwargs)

            if self.events == []:
                raise Exception('Events: "events" list was not defined in event_class.')

            self._max_tiers = len(self.events)

            if self.iconset == []:
                raise Exception('Events: "iconset" list was not defined in event_class. You need to add at least one set of icons.')
            elif len(self.iconset) < self._max_tiers:
                for i in xrange(self._max_tiers-len(self.iconset)):
                    self.iconset.append([self.iconset[0][0], self.iconset[0][1]])

            for i in xrange(self._max_tiers):
                for j in xrange(len(self.events[i])):
                    self.events[i][j] += [False]

        def start(self):
            self.counter += 1
            self.points += 1
            for i in xrange(len(self.events[self._tier])):
                if self.events[self._tier][i][1] == False:
                    self.events[self._tier][i][1] = True
                    return renpy.jump(self.events[self._tier][i][0])
            events_filtered = filter(lambda x: '_intro' not in x[0], self.events[self._tier])
            random_event = events_filtered[random.randint(0, len(events_filtered)-1)][0]
            return renpy.jump(random_event)

        def start_advance(self):
            self.counter += 1
            self.points += 1
            for i in xrange(self._max_tiers):
                for j in xrange(len(self.events[i])):
                    if self.events[i][j][1] == False:
                        self.events[i][j][1] = True
                        self._tier = i
                        return renpy.jump(self.events[i][j][0])
            events_filtered = filter(lambda x: '_intro' not in x[0], self.events[self._tier])
            random_event = events_filtered[random.randint(0, len(events_filtered)-1)][0]
            return renpy.jump(random_event)

        def getMenuText(self):
            heart_list = []
            imagepath = "interface/icons/small/"
            menu_text = ""
            for event in self.events[self._tier]:
                if event[1] == True:
                    heart_list.append(imagepath+self.iconset[self._tier][1]+".png")
                else:
                    heart_list.append(imagepath+self.iconset[self._tier][0]+".png")

            # Before Text hint
            if self.hint:
                menu_text += "{image=interface/check_True.png} "

            # Before Text icon
            if len(self.icons) > 0:
                if self.icons[self._tier]:
                    menu_text += "{image="+imagepath+self.icons[self._tier]+".png} "

            # Main Text
            if self.title:
                menu_text += "\""+self.title+"\" "

            # After Text heart
            for heart in heart_list:
                menu_text += "{image="+heart+"}"

            return menu_text

        def fail(self):
            self.counter -= max(0, self.counter-1)
            self.points -= 1
            self.events[self._tier][self._points][1] = False
            return

        # Reset the event completely
        def reset(self):
            for i in xrange(self._max_tiers):
                for j in xrange(len(self.events[i])):
                    self.events[i][j][1] = False
            self._tier = 0
            self._points = 0
            self.counter = 0
            self.inProgress = False

        def status(self, value):
            status_list = []
            for item in self.events[value-1]:
                status_list += [item[1]]
            return status_list

        @property
        def points(self):
            return self._points

        @points.setter
        def points(self, value):
            self._points = max(0, min(value, len(self.events[self._tier])))

        @property
        def tier(self):
            return self._tier+1

        @tier.setter
        def tier(self, value):
            if value > self._tier+1:
                self._points = 0
            self._tier = max(0, min(value-1, self._max_tiers-1))

        @property
        def max_tiers(self):
            return self._max_tiers

        @max_tiers.setter
        def max_tiers(self, value):
            pass
