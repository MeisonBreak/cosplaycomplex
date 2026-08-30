# === Stage 43: Добавь пагинацию длинных списков ===
# Project: WarehouseMini
def paginate(items, page_size=20, page=1):
    total_pages = (len(items) + page_size - 1) // page_size if items else 0
    return {
        "items": items[(page - 1) * page_size : page * page_size],
        "total": len(items),
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
    }
