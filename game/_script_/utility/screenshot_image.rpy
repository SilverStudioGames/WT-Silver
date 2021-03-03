
init -10 python:
    class ScreenshotImage(im.ImageBase):
        def __init__(self, root, **properties):
            super(ScreenshotImage, self).__init__(root, **properties)
            self.root = root
            # self.cache = False
            # Sometimes causes segfault, maybe only if cache = True?

        def load(self):
            sw, sh = config.screen_width, config.screen_height
            render = renpy.display.render.render_screen(self.root, sw, sh)
            return renpy.display.draw.screenshot(render)

        @staticmethod
        def capture(retain=True):
            if retain:
                # Prevent the image from being recaptured after load
                renpy.retain_after_load()

            root = renpy.display.core.scene_lists().make_layer("screens", {})
            return ScreenshotImage(root)

    def displayable_to_file(d, path, size=(config.screen_width, config.screen_height), crop=None, coloralpha=(0, 255, 0)):
        crop = crop or (0, 0, size[0], size[1])
        gl_clear = renpy.config.gl_clear_color
        renpy.config.gl_clear_color = coloralpha

        d = d.render(size[0], size[1], 0, 0)
        surf = renpy.display.draw.screenshot(d)
        surf = pygame.transform.smoothscale(surf, (config.screen_width, config.screen_height)).convert()
        surf.set_colorkey(coloralpha)

        psurf = pygame.Surface(size, pygame.SRCALPHA).convert_alpha()
        psurf.blit(surf, (0, 0), crop)

        pygame.image.save(psurf, path)
        renpy.config.gl_clear_color = gl_clear
