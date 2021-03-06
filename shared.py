# Shared Python information for the Red Panda Lineage scripts

LINKS_PATH = "./links"
MEDIA_PATH = "./media" 
PANDA_PATH = "./pandas"
OUTPUT_PATH = "./export/redpanda.json"
WILD_PATH = "./wild" 
ZOO_PATH = "./zoos"

# Go back no more than this amount of time to get commits
COMMIT_AGE = 7 * 24 * 60 * 60   # 7 days

# IG alphabet for hashes, time ordering oldest to newest
HASH_ORDER = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-"

# Exceptions
class AuthorError(ValueError):
    pass

class CommitError(IndexError):
    pass

class DateConsistencyError(ValueError):
    pass

class DateFormatError(ValueError):
    pass

class GenderFormatError(ValueError):
    pass

class IdError(KeyError):
    pass

class LinkError(IndexError):
    pass

class NameFormatError(ValueError):
    pass

class SectionNameError(ValueError):
    pass