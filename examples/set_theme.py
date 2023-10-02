#!/usr/bin/env python3

from pytablewriter import TableWriterFactory


def main():
    writer = TableWriterFactory.create_from_format_name(
        "markdown",
        headers=["INT", "STR", "F", "B"],
        value_matrix=[
            [1, "hoge", 0.1, True],
            [2, "foo", 0.2, True],
            [3, "bar", 0.3, False],
        ],
        margin=1,
    )
    writer.set_theme("altcol", color="yellow")
    writer.write_table()


if __name__ == "__main__":
    main()
