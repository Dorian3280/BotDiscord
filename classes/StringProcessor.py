from table2ascii import table2ascii, PresetStyle, Merge


def format_str(text: str):
    return text.strip().replace(',', ' ')


def format_long_str(text: str):
    return text\
        .replace(',', ' ')\
        .replace('×', 'x')\
        .replace('[ b ]', '')\
        .strip()\


def from_csv_to_set(csv: str):
    return set(csv.strip().split('\n'))


def from_csv_to_table(body: dict, category: str, header):

    tables = []
    
    for k, v in body.items():
        tables.append(table2ascii(
            header=[f"{k} • {category.title()}"] + [Merge.LEFT] * (len(header) - 1),
            body=v,
            first_col_heading=True,
            style=PresetStyle.thin
        ))
    
    tables = '\n'.join(tables)
    
    return tables
