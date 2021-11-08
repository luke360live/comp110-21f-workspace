def read_csv_rows(DATA_FILE_PATH: str) -> list[dict[str, str]]:
    """Implementing read_csv_rows function."""  
    result: list[dict[str, str]] = []
    file_handle = open(DATA_FILE_PATH, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Column values function."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]], column: str) -> dict[str, list[str]]:
    """Columnar function."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Head Function."""
    result: dict[str, list[str]] = {}
    for key in table:
        result[key] = table[key][:rows]
    return result


def select(table: dict[str, list[str]], cols: list[str]) -> dict[str, list[str]]:
    """Select function."""
    result: dict[str, list[str]] = {}
    for col in cols:
        result[col] = table[col]
    return result
    

def concat(table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concat Function.""" 
    result: dict[str, list[str]] = {}
    for cols in table:
        result[cols] = table[cols]
    for col in second_table:
        if col in result:
            result[col] += second_table[col]
        else:
            result[col] = second_table[col]
    return result


def count(numbers: list[str]) -> dict[str, int]:
    """Count function."""
    result: dict[str, int] = {}
    for number in numbers:
        if number in result:
            result[number] += 1
        else:
            result[number] = 1
    return result