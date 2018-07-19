import io


def concat_text_files(inputs, output):
    with io.open(output, 'w', encoding='utf-8') as outfile:
        for fname in inputs:
            with io.open(fname, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
