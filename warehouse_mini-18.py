# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: WarehouseMini
class TagManager:
    def __init__(self, db):
        self.db = db

    def add_tag(self, tag_name):
        if not any(t['name'] == tag_name for t in self.db.get('tags', [])):
            self.db.setdefault('tags', []).append({'id': len(self.db.get('tags', [])) + 1, 'name': tag_name})

    def remove_tag(self, tag_name):
        tags = [t for t in self.db.get('tags', []) if t['name'] != tag_name]
        return not any(t['name'] == tag_name for t in tags)

    def assign_tags_to_item(self, item_id, tag_names):
        existing_tags = {t['id']: t['name'] for t in self.db.get('tags', [])}
        new_tag_ids = []
        for name in tag_names:
            if name not in existing_tags:
                self.add_tag(name)
                existing_tags[name] = len(self.db.get('tags', []))
            else:
                existing_tags[name] = next(t['id'] for t in self.db.get('tags', []) if t['name'] == name)

        item = self.db.setdefault('items', {}).get(item_id, {})
        current_tag_ids = {t['tag_id']: 1 for t in item.get('tags', [])}
        new_tags_to_add = []
        tags_to_remove = []

        for tag_name, tag_id in existing_tags.items():
            if tag_name not in [item.get('tags', {}).get(tid) for tid in current_tag_ids]:
                new_tags_to_add.append({'tag_id': tag_id})
            elif tag_name == item.get('tags', {}).get(tag_id):
                pass
            else:
                tags_to_remove.append(tag_id)

        if new_tags_to_add:
            self.db.setdefault('items', {})[item_id].setdefault('tags', []).extend(new_tags_to_add)
        if tags_to_remove:
            self.db.setdefault('items', {})[item_id]['tags'] = [t for t in self.db.setdefault('items', {})[item_id].get('tags', []) if t['tag_id'] not in tags_to_remove]

    def unassign_tags_from_item(self, item_id, tag_names):
        existing_tags = {t['id']: t['name'] for t in self.db.get('tags', [])}
        items_tags = self.db.setdefault('items', {}).get(item_id, {}).get('tags', [])
        tags_to_remove = []

        for tag_name in tag_names:
            if tag_name in existing_tags:
                tag_id = next((t['id'] for t in self.db.get('tags', []) if t['name'] == tag_name), None)
                if tag_id and any(t['tag_id'] == tag_id for t in items_tags):
                    tags_to_remove.append(tag_id)

        if tags_to_remove:
            self.db.setdefault('items', {})[item_id]['tags'] = [t for t in items_tags if t['tag_id'] not in tags_to_remove]
