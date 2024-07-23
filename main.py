import requests, random, string

# Выполните запрос к API cPanel
def generate_email():
    cpanel_url = ')'  # URL вашего cPanel сервера
    cpanel_user = 'usr'       # Ваш логин cPanel
    cpanel_password = '123'
    email_domain = 'gmail.org'            # Домен создаваемого почтового ящика
    email_quota = 10                         # Квота для почтового ящика в МБ

    # Составьте URL для API вызова
    api_url = f'{cpanel_url}/execute/Email/add_pop'

    characters = string.ascii_letters + string.digits
    email_user = ''.join(random.choice(characters) for _ in range(random.randint(8, 20)))
    email_password = ''.join(random.choice(characters) for _ in range(random.randint(15, 20)))

    data = {
        'email': email_user,
        'domain': email_domain,
        'password': email_password,
        'quota': email_quota
    }

    response = requests.post(api_url, data=data, auth=(cpanel_user, cpanel_password), verify=False)

    if response.status_code == 200:
        print(f'Почтовый ящик успешно создан\n{email_user}@{email_domain}:{email_password}')
        return f'{email_user}@{email_domain}:{email_password}'
    else:
        print('Произошла ошибка при создании почтового ящика:', response.json())

