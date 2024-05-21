# UniSwap Global

UniSwap Global is a global student exchange platform built using Django.

## Features

- **Global Reach:** Connect with students from around the world.
- **Exchange Opportunities:** Explore exchange programs with universities worldwide.
- **User Profiles:** Create and manage your profile to showcase your interests and experiences.
- **Secure Messaging:** Communicate safely with other users to plan your exchange.
- **Resource Hub:** Access resources and guides to help plan your exchange journey.

## Dependencies

- [Django](https://www.djangoproject.com/)
- [django-taggit](https://django-taggit.readthedocs.io/en/latest/)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Pillow](https://python-pillow.org/)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ngari-mwaniki/My-World.git
   ```

2. Navigate to the project directory:
   ```
   cd MYWORLD
   ```

3. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

## Running the Server

1. Start the development server:
   ```
   python manage.py runserver
   ```

2. Access the website at `http://127.0.0.1:8000/` in your browser.

## Contributing

Contributions are welcome! If you'd like to contribute to UniSwap Global, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Support

For any inquiries or support, please contact info.datascience.uon@gmail.com
