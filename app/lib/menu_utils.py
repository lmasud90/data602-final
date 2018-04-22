def transform_menu(menu):
    menu_items = []
    for category in menu.keys():
        menu_items.append(
            {
                'category': category,
                'items': menu[category]
            }
        )
    return menu_items

def filter_by_calories(menu, calories):
    for category in menu:
        items = menu[category]
        filtered_items = []
        for item in items:
            if float(item['calories']) <= calories:
                filtered_items.append(item)
        
        menu[category] = filtered_items
    return menu