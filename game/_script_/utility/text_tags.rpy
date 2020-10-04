
# Custom text tags
# https://www.renpy.org/doc/html/custom_text_tags.html

init python:
    @renpy.pure
    def text_tag_unicode(tag, argument, contents):
        """Render contents using a font that supports all/most Unicode characters. Usage {unicode}☺{/unicode}"""
        # DejaVuSans is included by default in Ren'py
        return [(renpy.TEXT_TAG, "font=DejaVuSans.ttf")] + contents + [(renpy.TEXT_TAG, "/font")]

    def text_tag_name(tag, argument):
        """Use the name provided by a variable, or a contextual name. Usage {name=genie_name|Dude}"""
        name_var, context_name = argument.split("|", 1)
        name = getattr(renpy.store, name_var, None)
        #TODO Contextual name logic
        return [(renpy.TEXT_TEXT, name)]

    @renpy.pure
    def text_tag_heart(tag, argument):
        """Insert a unicode heart symbol. Usage {heart}"""
        return [
            (renpy.TEXT_TAG, "unicode"), (renpy.TEXT_TAG, "size=-2"),
            (renpy.TEXT_TEXT, "❤"),
            (renpy.TEXT_TAG, "/size"), (renpy.TEXT_TAG, "/unicode")
        ]

    @renpy.pure
    def text_tag_number(tag, argument):
        """Convert a number to words if lower than 100 or a multiple of 100. Usage {number=expression}"""
        num = int(renpy.store.eval(argument))
        words = num_to_word(num) if num < 100 or num % 100 == 0 else str(num)
        return [(renpy.TEXT_TEXT, words)]

define config.custom_text_tags = {
    "unicode": text_tag_unicode,
}

define config.self_closing_custom_text_tags = {
    "name": text_tag_name,
    "heart": text_tag_heart,
    "number": text_tag_number,
}
