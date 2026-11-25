import re
import unicodedata


def slugify(text):
    """Lowercase ASCII words joined by '-': 'Hello, World!' -> 'hello-world'."""
    # Decompose accented letters so the base letter survives the ASCII filter.
    ascii_text = (
        unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    )
    return "-".join(re.findall(r"[a-z0-9]+", ascii_text.lower()))
