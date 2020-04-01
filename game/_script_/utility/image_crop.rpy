init python:
    import threading

    whitespace_dict = {}
    with renpy.file("images.whitespace") as fp:
        line = fp.readline()
        while line:
            path, area = line.strip("\r\n").split(':')
            whitespace_dict[path] = map(int, area.split(','))
            line = fp.readline()

    def start_image_crop():
        # Start loop in worker thread
        threading.Thread(target=image_crop_loop).start()

    def image_crop_loop():
        for cloth in hermione.wardrobe_list:
            # Call to ensure whitespace is calculated
            crop_whitespace(cloth.ico.path)

    def crop_whitespace(path):
        # Return box from whitespace_dict, or calculate and store it
        if path in whitespace_dict:
            box = whitespace_dict[path]
        else:
            surf = Image(path).load()
            box = surf.get_bounding_rect() # Does not return a list/tuple but an object!
            box = tuple(x for x in box)
            whitespace_dict[path] = box
        return box

    def crop_image_zoom(path, xsize, ysize, grayscale=False):
        box = crop_whitespace(path)
        zoom = min(1.0, min(float(xsize)/box[2], float(ysize)/box[3]))

        sprite = Image(path)
        if grayscale:
            sprite = im.Grayscale(path)
        sprite = im.Crop(sprite, box)
        sprite = im.FactorScale(sprite, zoom*2)
        return (sprite, 0.5)

    def get_zoom(image, xsize, ysize):
        if isinstance(image, basestring):
            image = im.Image(image)

        r = renpy.render(image, 800, 800, 0, 0)
        x, y = r.get_size()

        return min(1.0, min(ysize / y, xsize / x))

    class CroppedImage(object):
        size = (1010, 1200)

        def __init__(self, sprites, path):
            self.sprites = sprites
            self.path = path
            self.cached = False
            self.sprite = None

        def get_image(self):
            if not self.cached:
                self.cached = True
                box = crop_whitespace(self.path)
                self.sprite = Crop(box, Composite(self.size, *self.sprites))
            return self.sprite

    config.after_load_callbacks.append(start_image_crop)
