# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: WarehouseMini
def switch_profile():
    """Переключение активного профиля."""
    global active_user_id, current_user_data
    print("\n=== Переключение профиля ===")
    
    # Очистить текущий профиль из памяти
    if current_user_data:
        old_name = current_user_data["name"]
        del current_user_data
        print(f"Профиль '{old_name}' очищен из памяти.")
    
    # Показать доступные профили
    profiles_list = list(user_profiles.keys())
    if not profiles_list:
        print("Нет сохранённых профилей. Создайте новый через /user/add.")
        return
    
    print("\nДоступные профили:")
    for i, pid in enumerate(profiles_list, 1):
        pdata = user_profiles[pid]
        print(f"  {i}. ID: {pid} | Имя: {pdata['name']} | Роль: {pdata.get('role', 'user')}")
    
    choice = input("\nВыберите профиль (или введите 'new' для нового): ").strip()
    
    if choice.lower() == "new":
        print("Создание нового профиля...")
        name = input("Имя: ").strip() or "Безымянный"
        role = input("Роль [user/admin/manager]: ").strip().lower() or "user"
        
        pid = generate_id("profile", prefix="U")
        user_profiles[pid] = {
            "id": pid,
            "name": name,
            "role": role,
            "created_at": datetime.now().isoformat(),
            "last_login": None,
        }
        active_user_id = pid
        current_user_data = user_profiles[pid].copy()
        
        print(f"Новый профиль '{name}' создан и активирован (ID: {pid}).")
    else:
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(profiles_list):
                target_id = profiles_list[idx]
                active_user_id = target_id
                current_user_data = user_profiles[target_id].copy()
                
                # Обновить last_login
                current_user_data["last_login"] = datetime.now().isoformat()
                
                print(f"Переключение на профиль '{current_user_data['name']}' (ID: {target_id}).")
            else:
                print("Некорректный выбор.")
        except ValueError:
            print("Введите число или 'new'.")

switch_profile()
