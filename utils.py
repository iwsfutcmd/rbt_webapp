import icu
import csv

ruleset_cache = []

def available_rbts():
    return sorted(icu.Transliterator.getAvailableIDs())


def get_rules(ruleset_name):
    t = icu.Transliterator.createInstance(ruleset_name)
    return t.toRules()


def transliterate(rules, teststrings, reverse=False):
    di = icu.UTransDirection.REVERSE if reverse else icu.UTransDirection.FORWARD
    try:
        t = icu.Transliterator.createFromRules("test", rules, di)
    except icu.ICUError as e:
        raise ValueError(e)
    return [t.transliterate(string) for string in teststrings]


def process_testdata(testdata):
    r = csv.reader(testdata.splitlines(), delimiter="\t")
    return tuple(map(list, zip(*r)))


def register_ruleset(ruleset_id, rules):
    if ruleset_id in icu.Transliterator.getAvailableIDs():
        raise ValueError("Ruleset ID already registered")
    ruleset_cache.append(icu.Transliterator.createFromRules(ruleset_id, rules))
    icu.Transliterator.registerInstance(ruleset_cache[-1])
    return ruleset_id