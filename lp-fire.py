#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" CLI program for structuring texts """

import click

@click.command()
def main():
    click.echo("CLI interface for language processor library")

if __name__ == "__main__":
    main()