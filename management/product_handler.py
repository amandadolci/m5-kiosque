from menu import products


def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError('product id must be an int')
    for dictionary in products:
        _id = dictionary.get('_id')
        if id != _id:
            continue
        elif id == _id:
            return dictionary
    return {}


def get_products_by_type(text: str):
    if not isinstance(text, str):
        raise TypeError('product type must be a str')
    list = []
    for dictionary in products:
        type = dictionary.get('type')
        if text != type:
            continue
        elif text == type:
            list.append(dictionary)
    return list


def add_product(lista: list, **kwargs):
    ids = []
    id = 1
    if len(lista) > 0:
        for dictionary in lista:
            ids.append(dictionary['_id'])
        id = max(ids) + 1
    kwargs['_id'] = id
    lista.append(kwargs)

    return kwargs


def add_product_extra(menu: list[dict], *args, **kwargs):
    id = 1
    if len(menu) > 0:
        index_list = [product["_id"] for product in menu]
        index_list.sort()
        id = index_list[-1] + 1
    new_product = dict(
        [
            (key, kwargs[f"{key}"])
            for key in kwargs
            for req_key in args
            if key == req_key
        ]
    )
    for req_key in sorted(args):
        try:
            new_product[f"{req_key}"]
        except KeyError:
            raise KeyError(f"field {req_key} is required") from None
    new_product["_id"] = id
    menu.append(new_product)
    return new_product


def menu_report():
    products_quantity = len(products)

    price_list = [key['price'] for key in products]
    average = round((sum(price_list) / products_quantity), 2)

    key_type_list = [key['type'] for key in products]
    type_counter = {}
    for type in key_type_list:
        if type in type_counter:
            type_counter[type] += 1
        else:
            type_counter[type] = 1

    most_recurrent_type = ""
    max_count = 0
    for type, count in type_counter.items():
        if count > max_count:
            max_count = count
            most_recurrent_type = type

    return f"Products Count: {products_quantity} - Average Price: ${average} - Most Common Type: {most_recurrent_type}"
