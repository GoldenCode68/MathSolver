# MathSolver 🧮

**MathSolver** is a simple web-based equation solver built with Python and Flask.

It helps users solve linear and quadratic equations through a clean and user-friendly interface.

## ✨ Features

- Solve linear equations (degree 1).
- Solve quadratic equations (degree 2).
- Enter integer, decimal, and fractional coefficients (e.g. `2`, `1.5`, `3/4`).
- Display equation solutions.
- Handle equations with real or complex roots (depending on the current implementation).
- Responsive web interface.
- Simple and lightweight Python backend.

## 🛠️ Technologies

- Python
- Flask
- HTML5
- CSS3
- JavaScript

## 📋 Requirements

Before running MathSolver, make sure you have:

- Python 3 installed.
- pip (Python package installer).
- A modern web browser.
- Git (optional, for cloning the repository).

## 🚀 Installation & Setup

### 1. Clone the repository

Replace `YOUR_USERNAME/YOUR_REPOSITORY` with your actual GitHub repository path.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Alternatively, download the repository as a ZIP file and extract it.

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install Flask
```

If the project includes a `requirements.txt` file, install dependencies with:

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

If `python` is not recognized on macOS or Linux, try:

```bash
python3 app.py
```

### 5. Open MathSolver

Open your browser and visit:

http://127.0.0.1:5000

The application should now be ready to use.

To stop the development server, press `Ctrl + C` in the terminal.

## 📖 How to Use

### Linear Equations

Choose **Degree 1** and enter the coefficients.

A linear equation has the following form:

`ax + b = 0`

Example:

`2x - 6 = 0`

Enter:

- `a = 2`
- `b = -6`

The solution is:

`x = 3`

### Quadratic Equations

Choose **Degree 2** and enter the coefficients.

A quadratic equation has the following form:

`ax² + bx + c = 0`

Example:

`x² - 5x + 6 = 0`

Enter:

- `a = 1`
- `b = -5`
- `c = 6`

The solutions are:

`x₁ = 2`

`x₂ = 3`

### Entering Fractions

You can enter fractional coefficients using `/`.

Examples:

- `1/2`
- `3/4`
- `-5/3`

Decimal examples:

- `0.5`
- `1.25`
- `-2.75`

Use the input format supported by your current application.

## 📁 Project Structure

```text
MathSolver/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── ...
```

The exact contents of `static/` may vary depending on your implementation.

## ⚠️ Notes

- This project is intended for learning, experimentation, and educational use.
- Run Flask's development server locally.
- Do not expose Flask's debug mode or development server directly to the public internet.
- For production deployment, use a production-ready WSGI server and appropriate security settings.

## 🔮 Future Improvements

- Step-by-step equation solving.
- Improved mathematical notation and fraction rendering.
- Equation history.
- More equation types.
- Improved input validation and error messages.
- Automated tests.

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## 📄 License

Choose a license before publishing the project.

If you want others to use, modify, and distribute your code, consider adding an appropriate open-source license, such as the MIT License.

---

**Developed as a personal learning project.**
