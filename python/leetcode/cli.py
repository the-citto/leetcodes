"""CLI."""

import rich_click as click

from . import __version__


@click.group(
    context_settings={
        "help_option_names": ["-h", "--help"],
        "show_default": True,
    },
)
@click.version_option(__version__, "-V", "--version")
def cli() -> None:
    """CLI."""


@cli.group()
def easy() -> None:
    """Easy."""

@cli.group()
def medium() -> None:
    """Medium."""

@cli.group()
def hard() -> None:
    """Hard."""


@easy.command()
def two_sum() -> None:
    """1. Two Sum."""

@easy.command()
def add_two_numbers() -> None:
    """2. Add Two Numbers."""

@medium.command()
def longest_substring_withouut_characters() -> None:
    """3. Longest Substring Without Repeating Characters."""

@hard.command()
def median_of_two_sorted_arrays() -> None:
    """4. Median of Two Sorted Arrays."""

@medium.command()
def longest_palindromic_substring() -> None:
    """5. Longest Palindromic Substring."""





