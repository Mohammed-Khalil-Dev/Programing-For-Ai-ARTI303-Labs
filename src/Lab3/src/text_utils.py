"""TODO: describe this module."""


def clean_name(raw:str):
    """TODO: describe this function."""
    # TODO: collapse whitespace, then title-case
    raw = raw.strip()
    raw = " ".join(raw.split())
    raw = " ".join([word.capitalize() for word in raw.split()])
    return raw
