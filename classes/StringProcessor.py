from table2ascii import table2ascii, PresetStyle, Merge
from itertools import groupby

def format_str(text: str):
    return text.strip().replace(',', ' ')

def format_long_str(text: str):
    return text.strip().replace(',', ' ').replace('×', 'x')

def from_csv_to_table(file_txt: str, category: str, header: str):
    categories, header = header.strip().split('\n')
    categories = categories[3:].split(',')
    header = header.split(',')

    body = map(lambda row: row.split(','), file_txt.splitlines())
    body = map(list, (group for key, group in groupby(body, lambda x: "--" in x) if not key))
    body = {category: block for category, block in zip(categories, body)}

    tables = []
    
    for k, v in body.items():
        tables.append(table2ascii(
            header=["", f"{k} • {category.title()}"] + [Merge.LEFT] * (len(header) - 2),
            body=v,
            first_col_heading=True,
            style=PresetStyle.thin
        ))
    
    tables = '\n'.join(tables)
    
    return tables
