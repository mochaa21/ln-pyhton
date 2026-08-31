def generate_hashtag(s):
    h = '#' + s.title().replace(' ', '')
    return h if 1 < len(h) <= 140 else False