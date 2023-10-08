#!/usr/bin/env python3

from pathlib import Path

import pytablewriter as ptw
from tblfaker import TableFaker


def main() -> None:
    faker = TableFaker(seed=1)
    data = faker.generate(["name", "email", "address", "color", "md5"], rows=8)

    writer = ptw.TableWriterFactory.create_from_format_name(
        "html",
        table_name="pytablewriter-altrow-theme example",
        margin=1,
    )
    writer.from_tabledata(data, is_overwrite_table_name=False)
    writer.set_theme("altcol")
    with open(Path(__file__).parent.parent.joinpath("docs", "example.html"), "w") as f:
        writer.stream = f
        writer.write_table(write_css=True)


if __name__ == "__main__":
    main()