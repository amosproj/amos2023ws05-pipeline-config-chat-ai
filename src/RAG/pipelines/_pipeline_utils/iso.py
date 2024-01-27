"""
    Unpivot the data. Convert column values into rows.

    Args:
        df: Data to be unpivot.
        id_vars: Columns to keep after unpivot.
        value_vars: Columns to be converted into rows.
        var_name: New column name to store previous column names.
        value_name: New column name to store values of unpivoted columns.

    Returns: Data after unpivot process.

    """