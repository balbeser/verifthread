def get_paginate_rows(data: list, height: int = 3, end: int = 1) -> list[int, int]:
    len_data = len(data)
    ceil_data = len_data // height
    return [*[height] * ceil_data, end]
