import re
import unicodedata


def slugify(value):
    value = unicodedata.normalize("NFKC", value)
    value = re.sub(r"[^\w\s-]", "", value)
    return re.sub(r"[-\s]+", "_", value).strip("-_")
