from io import open


def iob_reader(fn, len_fields, sep='\t'):
    sentence = []
    with open(fn, encoding='utf-8') as fi:
        for line in fi:
            line = line.strip('\n')
            if not line:
                if sentence:
                    yield sentence
                sentence = []
            else:
                fields = line.split(sep)
                if len(fields) != len_fields:
                    raise ValueError(
                        u'Too few fields {} expected {} for \n{}'.format(len(fields), len_fields, line))
                sentence.append(fields)

    if sentence:
        yield sentence
