# Django Demo Project

A modern Django-based web application that demonstrates best practices in Django development.

## 🚀 Features

- RESTful API endpoints
- Clean architecture
- Easy to extend and maintain
- Well-documented code
- Test coverage
- Automated cron jobs for time-based tasks
- Custom management commands for utility operations

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/imratnesh/django_demo.git
cd django_demo
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📚 Project Structure

```
django_demo/
├── api/                    # API application
│   ├── migrations/        # Database migrations
│   ├── management/        # Custom management commands
│   │   └── commands/     # Command implementations
│   ├── tests.py          # Test cases
│   ├── views.py          # API views
│   └── urls.py           # URL routing
├── sample/               # Main project configuration
│   ├── cron.py          # Cron job definitions
│   └── utils.py         # Utility functions
├── manage.py            # Django management script
└── requirements.txt     # Project dependencies
```

## 🎯 Usage

### API Endpoints

- `GET /api/`: List all available endpoints
- More endpoints will be documented here

### Custom Management Commands

The project includes custom management commands for utility operations:

1. **Add Numbers**
   ```bash
   python manage.py add_number <num1> <num2>
   ```
   Adds two numbers and displays the result.
   Example:
   ```bash
   python manage.py add_number 3 4
   # Output: 7
   ```

2. **Query Prompt**
   ```bash
   python manage.py query_prompt "<your query>"
   ```
   Processes a query and returns an answer using the utility function.
   Example:
   ```bash
   python manage.py query_prompt "What is the weather?"
   ```

### Cron Jobs

The project includes automated cron jobs for time-based tasks:

1. **FetchTimeCronJob**: Runs every minute to fetch and process current time data
   ```bash
   python manage.py runcrons
   ```

2. To run all cron jobs:
   ```bash
   python manage.py runcrons
   ```

3. To run a specific cron job:
   ```bash
   python manage.py runcrons sample.fetch_time_cron
   ```

### Development

1. Make sure you're in the virtual environment
2. Run tests:
```bash
python manage.py test
```

3. Check code style:
```bash
flake8
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Author

**Your Name**
- LinkedIn: [Your LinkedIn Profile](linkedin.com/in/ratneshkushwaha/)
- YouTube: [Your YouTube Channel](https://www.youtube.com/@IndiaAnalytical)

## 🙏 Acknowledgments

- Django Documentation
- Django REST Framework
- All contributors who have helped this project

## 📞 Support

For support, email your.email@example.com or create an issue in the repository. 