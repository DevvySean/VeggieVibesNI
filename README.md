# VeggieVibesNI

A community forum for vegetable growers in Northern Ireland 🥕🥬🌱

## About

VeggieVibesNI is a Django-based forum where gardeners across Northern Ireland can share knowledge, tips, success stories, and advice about growing vegetables in our unique climate.

## Features

- **Categories** - Organized discussions by vegetable type
- **Posts & Replies** - Create threads and engage in conversations
- **User Profiles** - Share your location and gardening bio
- **Admin Panel** - Easy content management
- **Photo Uploads** - Share your garden successes (coming soon)

## Setup

1. **Install dependencies:**
```bash
pip install django pillow
```

2. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Create a superuser:**
```bash
python manage.py createsuperuser
```

4. **Run the development server:**
```bash
python manage.py runserver
```

5. **Visit the site:**
- Forum: http://localhost:8000/
- Admin: http://localhost:8000/admin/

## Getting Started

1. Login to the admin panel
2. Create some categories (e.g., Potatoes, Tomatoes, Carrots, etc.)
3. Start creating posts and building your community!

## Tech Stack

- Django 6.0
- Python 3.12
- SQLite (development)

## Contributing

This is a community project - contributions welcome!

---

Happy Growing! 🌱
