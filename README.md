# 📱 Django Referral System

Простая реферальная система на Django + DRF с авторизацией по номеру телефона и генерацией инвайт-кодов.

---

## 🚀 Функциональность

- Авторизация по номеру телефона (эмуляция отправки кода).
- Верификация пользователя по 4-значному коду.
- Генерация уникального инвайт-кода при первой авторизации.
- Активация чужого инвайт-кода (только один раз).
- Профиль пользователя с:
  - его инвайт-кодом,
  - активированным чужим кодом (если был),
  - списком пользователей, введших его код.

---

## 🛠️ Стек технологий

- Python 3.12
- Django 4.2+
- Django REST Framework
- PostgreSQL

---
## 📂 Установка

```bash
git clone https://github.com/yourusername/referral-system.git
cd referral-system
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
Структура проекта

HammerTest/
├── accounts/           # Основное приложение
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
├── HammerTest/   # Настройки проекта
├── .env
├── requirements.txt
├── README.md
├── templates/
├   ├── swaggerui/


Swagger UI доступен по адресу:
[http://localhost:8000/swagger-ui/](http://localhost:8000/swagger-ui/)

Сырые схемы:
- JSON: `/swagger.json`
- YAML: `/swagger.yaml`

Postman коллекция:
https://web.postman.co/workspace/My-Workspace~2911fb63-164e-4ee1-8167-5e8daf6f64e6/request/45701736-cfcf7385-b9a5-4aaf-b5fa-0a75da16f035?action=share&creator=45701736&ctx=documentation

Получение кода:
http://127.0.0.1:8000/api/auth/request-code/
Подтверждение кода:
http://127.0.0.1:8000/api/auth/verify-code/
Активация инвайт кода:
http://127.0.0.1:8000/api/activate-invite/
Получение профиля:
http://127.0.0.1:8000/api/profile/?phone=%2B79991234567