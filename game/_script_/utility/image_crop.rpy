init python:
    whitespace_dict = {}
    with renpy.file("images.whitespace") as fp:
        line = fp.readline()
        while line:
            path, area = line.strip("\r\n").split(':')
            whitespace_dict[path] = map(int, area.split(','))
            line = fp.readline()

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
        matrix = SaturationMatrix(0) if grayscale else None
        sprite = Image(path)

        # Image manipulation still looks better than mipmaps at small scales
        sprite = im.Crop(sprite, box)
        sprite = im.FactorScale(sprite, zoom*2)
        # Alternative to the above; pass `crop=box, zoom=zoom` to the transform
        return Transform(sprite, zoom=0.5, matrixcolor=matrix)

    def get_zoom(image, size):
        if isinstance(image, basestring):
            image = Image(image)

        r = renpy.render(image, 800, 800, 0, 0)
        x, y = r.get_size()
        xsize, ysize = size

        return min(ysize / y, xsize / x)

    class CroppedImage(object):
        def __init__(self, sprites, path):
            self.sprites = sprites
            self.path = path
            self.cached = False
            self.sprite = None

        def get_image(self):
            if not renpy.is_skipping() or not self.cached:
                self.cached = True
                # TODO: Fix the math, not every sprite is centred correctly and some margins are too big.

                x, y, w, h = crop_whitespace(self.path)

                xoffset = w/4
                yoffset = h/4

                w = max(w, max(h, 72))
                h = max(h, max(w, 72))

                x = clamp( (x - w/2) + xoffset, 0, 1010)
                w = max(72, w + w/2)

                y = clamp( (y - h/2) + yoffset, 0, 1200)
                h = max(72, h + h/2)

                # Forbid exceeding the image height.
                if y+h > 1200:
                    y = 1200-h

                box = (x, y, w, h)
                self.sprite = Crop(box, Fixed(*self.sprites))
            return self.sprite
