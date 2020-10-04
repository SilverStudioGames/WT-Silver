
default screenshot_image = None

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
            shot = renpy.display.draw.screenshot(render)
            shot = renpy.display.scale.real_transform_scale(shot, (config.screen_width, config.screen_height))
            return shot

        @staticmethod
        def capture(retain=True):
            if retain:
                # Prevent the image from being recaptured after load
                renpy.retain_after_load()

            root = renpy.display.core.scene_lists().make_layer("screens", {})
            return ScreenshotImage(root)

    def displayable_to_file(d, fn="output.webp", w=2048, h=2048):
        import cStringIO

        switch_renderer = renpy.get_renderer_info()["renderer"] != "sw"

        if switch_renderer:
            # Remember the renderer preference
            renderer_pref = renpy.game.preferences.renderer
            renpy.game.preferences.renderer = "sw"

            # Switch to software rendering
            renpy.display.draw.quit()
            renpy.display.draw = None
            renpy.display.interface.set_mode()

        # Render to surface using software rendering
        render = d.render(w, h, 0, 0)
        surf = renpy.display.swdraw.surface(render.width, render.height, True)
        renpy.display.swdraw.draw(surf, None, render, 0, 0, False)

        if switch_renderer:
            # Restore preferred rendering
            renpy.display.draw.quit()
            renpy.display.draw = None
            renpy.game.preferences.renderer = renderer_pref
            renpy.display.interface.set_mode()
            renpy.free_memory()

        # Write surface to PNG file
        sio = cStringIO.StringIO()
        renpy.display.module.save_png(surf, sio, 0)
        with open(fn, "wb") as f:
            f.write(sio.getvalue())
        sio.close()
