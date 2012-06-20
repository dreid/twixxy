from StringIO import StringIO

import twiggy


def stringIOTwiggySetup():
    out = StringIO()

    twiggy.addEmitters((
        '*',
        twiggy.levels.DEBUG,
        True,
        twiggy.outputs.StreamOutput(twiggy.formats.line_format, stream=out)
    ))

    return out
