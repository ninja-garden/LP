
""" CLI program for structuring texts """

import click
from LPL.Storage import TextStorage

@click.command()
@click.argument('input_file')
def main(input_file):
    click.echo('CLI interface for language processor library')
    print(input_file)
    with open(input_file, encoding='utf_8_sig') as file:
        text = file.read()
    storage = TextStorage(text)


if __name__ == '__main__':
    main()