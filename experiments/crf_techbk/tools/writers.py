# coding=utf-8
from io import open


def iob_writer(data, fn, len_fields, sep=u'\t'):
    with open(fn, 'w', encoding='utf-8') as fo:
        for sentence in data:
            for fields in sentence:
                if len(fields) != len_fields:
                    # TODO: string error more able understand ... :v
                    raise ValueError(
                        u'Too few fields {} expected {} for \n{}'.format(len(fields), len_fields, fields))

                out_line = sep.join(fields) + u'\n'
                fo.write(out_line)
            fo.write(u'\n')
