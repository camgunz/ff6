def check_only_one(attributes, names):
    if len(list(filter(None, [attributes[name] for name in names]))) > 1:
        msg = 'Only one of %s or %s may be given'
        raise ValueError(msg % (', '.join(names[:1]), names[-1]))

