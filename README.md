# Hand-Written NIST Digits Classification 🧠✍️

A deep learning project focused on classifying hand-written digits using the **NIST Special Database**. This project utilizes Convolutional Neural Networks (CNNs) to accurately recognize digits from 0 to 9, commonly used in digit recognition and OCR systems.

---

## 📂 Dataset

-   **Source:** [NIST Special Database](https://www.nist.gov/srd/nist-special-database-19)
-   Contains labeled images of hand-written digits from thousands of users.
-   Preprocessed and split into training and testing sets.

---

## 🏗️ Project Structure

├── AI/
│   ├── finetunnig.ipynb
│   └── Model_data.ipynb
├── api/
│   ├── pycache/
│   ├── init.py
│   ├── urls.py
│   └── views.py
├── core/
│   ├── pycache/
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
│   └── images/
│       ├── hsf_2_00040_2Dkloxl.png
│       ├── hsf_2_00040.png
│       └── hsf_8_00001.png
├── myapp/
│   ├── pycache/
│   ├── migrations/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── Classifier.py
│   ├── db_handlers.py
│   ├── models.py
│   ├── serializer.py
│   ├── tests.py
│   └── views.py
├── env/
├── manage.py
├── Test Images/
└── requirements.txt

### Explanation of Key Directories and Files:

* **AI/**: Contains Jupyter notebooks (`.ipynb`) likely used for model fine-tuning, training, and data preparation.
* **api/**: This directory probably handles API endpoints for the web application, exposing functionalities like prediction.
* **core/**: Contains the core Django project settings, URL configurations, and ASGI/WSGI settings.
* **media/images/**: Stores example images, possibly used for testing or as part of the application's content.
* **myapp/**: This is a Django application within the project, likely containing the main logic for digit classification, database interactions, and views.
    * `Classifier.py`: Suggests the main logic for the digit classification model integration and prediction.
    * `models.py`: Defines the database models for the application.
    * `views.py`: Handles the rendering of web pages or API responses.
* **env/**: Typically holds the Python virtual environment for the project dependencies.
* **manage.py**: Django's command-line utility for administrative tasks.
* **Test Images/**: Likely contains images used for testing the model or the application's functionality.
* **requirements.txt**: Lists all the Python dependencies required for the project.

---

## 🚀 Installation

To set up this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/HAND_DIGITS.git](https://github.com/your-username/HAND_DIGITS.git)
    cd HAND_DIGITS
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    # On Windows
    .\env\Scripts\activate
    # On macOS/Linux
    source env/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations (if using Django database models):**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The application should now be accessible at `http://127.0.0.1:8000/`.

---

## 💡 Usage

Once the server is running, you can interact with the web application through your browser or via its API endpoints.

* **Web Interface**: Navigate to the root URL or specific paths defined in `urls.py` for any user-facing pages.
* **API Endpoints**: Use tools like `curl` or Postman to interact with the API (e.g., to send images for classification and receive predictions). The specific endpoints will be defined in `api/urls.py` and handled by `api/views.py`.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

1.  **Fork** the repository.
2.  Create a new feature branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes and ensure they adhere to the project's coding style.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a **Pull Request** explaining your changes.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For any questions or inquiries, please contact Muhammad-Saaad / javed.iqbal12458@gmail.com.
