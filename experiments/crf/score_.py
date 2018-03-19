def create_tags(sentences):
    tags = []
    for sentence_index, iob_tags in enumerate(sentences):
        i = 0
        current_tag = [None, None, None, None]
        while i < len(iob_tags):
            if iob_tags[i] == "O" and current_tag[0]:
                tags.append(tuple(current_tag))
                current_tag = [None, None, None, None]
            elif iob_tags[i].startswith("B"):
                current_tag[0] = iob_tags[i][2:]
                current_tag[1] = i
                current_tag[2] = i
                current_tag[3] = sentence_index
            elif iob_tags[i].startswith("I"):
                current_tag[2] = i
            i += 1
        if current_tag[0]:
            tags.append(tuple(current_tag))
    tags = set(tags)
    return tags


def iob_score(y_true, y_pred):
    """
    Parameters
    ----------
    y_true : list
        each sublist is a list of tags
    y_pred: list of list
        each sublist is a list of tags
    """
    tags_true = create_tags(y_true)
    tags_pred = create_tags(y_pred)
    ref = len(tags_true)
    true = len(set(tags_true).intersection(tags_pred))
    sys = len(tags_pred)
    if ref == 0 or true == 0 or sys == 0:
        return 0
    p = true / sys
    r = true / ref
    f1 = (2 * p * r) / (p + r)

    return f1
