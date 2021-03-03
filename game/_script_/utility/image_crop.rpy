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

                wmax, hmax = 1010, 1200
                wmin = hmin = 72

                x, y, w, h = crop_whitespace(self.path)
                xoffset, yoffset = w/2, h/2

                w = h = max(w, h, wmin, hmin)

                w = max(wmin, w + w/2)
                h = max(hmin, h + h/2)

                x = clamp( (x - w/2) + xoffset, 0, wmax)
                y = clamp( (y - h/2) + yoffset, 0, hmax)

                # Forbid exceeding the image height.
                if y+h > hmax:
                    y = hmax-h

                self.sprite = Transform(Fixed(*self.sprites), crop=(int(x), int(y), int(w), int(h)))
            return self.sprite
