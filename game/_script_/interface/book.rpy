init python:
    class book_readable_class(object):
        def __init__(self, title, contents=[], **kwargs):
            self.title = title
            self.page = 0
            self.overflow=None

            self.title = title
            self.contents = contents
            self.__dict__.update(**kwargs)

            self.pages = len(self.contents)-1

        def open(self, page=0):
            self.page = max(0, min(page, self.pages))
            self.refresh()
            return

        def close(self):
            self.page = 0
            renpy.hide_screen("book_menu")
            return

        def next(self):
            self.page = min(self.page+2, self.pages)
            self.refresh()
            return

        def prev(self):
            self.page = max(self.page-2, 0)
            self.refresh()
            return

        # Max 882 characters per page.
        def get_text(self):
            if self.pages >= self.page+1:
                return (self.contents[self.page][1][0:880], self.contents[self.page+1][1][0:880])
            return (self.contents[self.page][1][0:880], None)

        def get_title(self):
            if self.pages >= self.page+1:
                return (self.contents[self.page][0], self.contents[self.page+1][0])
            return (self.contents[self.page][0], None)

        def refresh(self):
            renpy.show_screen("book_menu", page=self.page, pages=self.pages, title=self.title, page_title=self.get_title(), page_text=self.get_text(), page_overflow=self.overflow)
            return

        def append(self, new_page):
            self.contents.append(new_page)
            self.pages = len(self.contents)-1
            return

    class diary_class(book_readable_class):
        def __init__(self, title, dictionary):
            super(diary_class, self).__init__(self)

            self.title = title
            self.dictionary = dictionary

        def append(self, entry, id, branches=None):
            for i in self.contents:
                if i[2] == id:
                    return

            entry = list(self.dictionary[entry])

            if branches:
                branches = tuple(self.dictionary[str(x)] for x in branches)
                entry = [entry[0], entry[1].format(*branches)]

            self.contents.append(["Day {}\n{}".format(game.day, entry[0]), str(entry[1]), id])
            self.pages = len(self.contents)-1
            return

label book_handle(book=None):
    $ book.open()
    $ renpy.play('sounds/bookopen.mp3')
    show screen book_animator("book_page_next", 0.5)
    label .after_init:

    $ _choice = ui.interact()

    if _choice == "next":
        $ book.next()
        $ renpy.play('sounds/pageflip.mp3')
        show screen book_animator("book_page_next", 0.5)
        with d1
    elif _choice == "prev":
        $ book.prev()
        $ renpy.play('sounds/pageflip.mp3')
        show screen book_animator("book_page_prev", 0.5)
        with d1
    elif _choice == "back":
        $ book.open()
        $ renpy.play('sounds/pageflipback.mp3')
        show screen book_animator("book_page_start", 0.5)
        with d1
    elif _choice == "Close":
        $ book.close()
        $ renpy.play('sounds/bookclose.mp3')
        return
    jump .after_init

screen book_menu(page, pages, title, page_title, page_text, page_overflow):
    tag book_menu
    zorder 30

    button style "empty" action NullAction()

    add Color("#000", alpha=0.5)
    add "interface/book/book_open.webp"

    frame:
        style "empty"
        pos (280, 130)
        xsize 250
        ysize 300
        text page_title[0] ypos -20 size 16 xalign 0.5
        text page_text[0] size 12 ypos 40
        text "{b}"+str(page+1)+"{/b}" xalign 0.5 ypos 350 size 11 # fix page calc

    frame:
        style "empty"
        xpos 600 ypos 130
        xsize 250
        ysize 300
        if page_title[1] != None:
            text page_title[1] ypos -20 size 16 xalign 0.5
        if page_text[1] != None:
            text page_text[1] size 12 ypos 40
        text "{b}"+str(page+2)+"{/b}" xalign 0.5 ypos 350 size 11

    imagebutton:
        pos (878, 100)
        ysize 400
        xalign 1.0
        # Next
        if page < pages:
            idle im.Alpha("interface/book/hover.webp", 0)
            hover "interface/book/hover.webp"
            action Return("next")
        # Fast Back to start
        else:
            idle "interface/book/back.webp"
            hover "interface/book/back.webp"
            action Return("back")

    # Previous
    if page > 0:
        imagebutton:
            pos (242, 100)
            ysize 400
            idle im.Alpha(Transform("interface/book/hover.webp", xzoom=-1.0), 0)
            hover Transform("interface/book/hover.webp", xzoom=-1.0)
            action Return("prev")

    use close_button

screen book_animator(img, timer):
    tag animator
    zorder 31

    add img
    button style "empty" action [Hide("book_animator"), With(Dissolve(0.05))]
    timer timer action [Hide("book_animator"), With(Dissolve(0.1))]

image book_page_next:
    contains:
        "interface/book/book_open.webp"
    contains:
        #"interface/book_of_secrets/book_anim_01.webp"
        #pause.1
        "interface/book/page_02.webp"
        pause.08
        "interface/book/page_03.webp"
        pause.08
        "interface/book/page_04.webp"
        pause.08
        "interface/book/page_05.webp"
        pause.08
        "interface/book/page_06.webp"
        pause.08
        "interface/book/page_07.webp"
        pause.08
        "blank"

image book_page_prev:
    contains:
        "interface/book/book_open.webp"
    contains:
        xoffset 40
        #"interface/book_of_secrets/book_anim_01.webp"
        #pause.1
        Transform("interface/book/page_02.webp", xzoom=-1.0)
        pause.08
        Transform("interface/book/page_03.webp", xzoom=-1.0)
        pause.08
        Transform("interface/book/page_04.webp", xzoom=-1.0)
        pause.08
        Transform("interface/book/page_05.webp", xzoom=-1.0)
        pause.08
        Transform("interface/book/page_06.webp", xzoom=-1.0)
        pause.08
        Transform("interface/book/page_07.webp", xzoom=-1.0)
        pause.08
        "blank"

image book_page_start:
    contains:
        "interface/book/book_open.webp"
    contains:
        "interface/book/reverse_01.webp"
        pause.07
        "interface/book/reverse_02.webp"
        pause.07
        "blank"
        repeat 3 #book_page_max was too slow
