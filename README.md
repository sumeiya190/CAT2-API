# E-Commerce Django Project

This project demonstrates a basic implementation of Django models for an e-commerce system, including `Customer` and `Order` models with a one-to-many relationship.

## Features

- `Customer` model stores customer details such as name and email.
- `Order` model tracks orders placed by customers, including order date and total amount.
- One-to-many relationship: A customer can place multiple orders, but each order is associated with a single customer.

---

### Steps to Set Up the Project

1. Create a repository in GitHub and clone it.&#x20;

1) **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

2) **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3) **Create the database migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4) **Run the development server:**

   ```bash
   python manage.py runserver
   ```

5) **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

---

### Testing the Models

1. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up admin credentials.

2. **Access the Django admin interface:**
   Navigate to `http://127.0.0.1:8000/admin/` and log in using the superuser credentials.

3. **Add Customers and Orders:**
   Use the Django admin interface to add customer data and create orders.

---

### Repository Structure

- `models.py`: Contains the `Customer` and `Order` model definitions.
- `migrations/`: Contains migration files for database changes.
- `requirements.txt`: Lists required Python packages for the project.
- `manage.py`: Django's command-line utility for administrative tasks.

---

## Additional Notes

- The `Customer` model ensures email uniqueness to prevent duplicate entries.
- The `Order` model uses a `DecimalField` for precise monetary calculations.
- The `related_name='orders'` in the `Order` model allows easy reverse lookup of orders for a customer.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss the changes.

---

### Author

Your Name

Sumeiya Abass
