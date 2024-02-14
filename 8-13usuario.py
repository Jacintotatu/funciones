def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Jacinto', 'Conesa', location = 'Cartagena', edad = 48,
                                pelo='Negro', cuerpo='Musculoso')
for c, v in user_profile.items():
    print(c, ':', v)