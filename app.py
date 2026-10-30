
from fractions import Fraction
from math import isqrt, sqrt
from flask import Flask, render_template, request

app = Flask(__name__)


def normalize_number(value):
    """Convert Persian and Arabic digits to English digits."""
    translation = str.maketrans(
        "۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩٫٬",
        "01234567890123456789.."
    )
    return value.translate(translation).strip().replace(" ", "")


def parse_fraction(value):
    """Parse integers, decimals, and fractions exactly."""
    value = normalize_number(value)

    if not value:
        raise ValueError("لطفاً تمام ضرایب موردنیاز را وارد کنید.")

    return Fraction(value)


def format_fraction(value):
    """Display a rational number as a fraction."""
    if value.denominator == 1:
        return str(value.numerator)

    return f"{value.numerator}/{value.denominator}"


def is_perfect_square_fraction(value):
    """Check whether a non-negative fraction has a rational square root."""
    if value < 0:
        return False

    numerator_root = isqrt(value.numerator)
    denominator_root = isqrt(value.denominator)

    return (
        numerator_root ** 2 == value.numerator
        and denominator_root ** 2 == value.denominator
    )


def format_decimal(value):
    """Format an approximate decimal result."""
    return f"{value:.8g}"


@app.route("/", methods=["GET", "POST"])
def home():
    result = []
    degree = "1"

    a_input = ""
    b_input = ""
    c_input = ""

    if request.method == "POST":
        degree = request.form.get("degree", "1")
        a_input = request.form.get("a", "")
        b_input = request.form.get("b", "")
        c_input = request.form.get("c", "")

        try:
            if degree not in ("1", "2"):
                raise ValueError("نوع معادله نامعتبر است.")

            # Parse coefficients exactly, without converting to float first.
            a = parse_fraction(a_input)
            b = parse_fraction(b_input)
            c = parse_fraction(c_input) if degree == "2" else Fraction(0)

            if a == 0:
                raise ValueError("ضریب a نباید صفر باشد.")

            # First-degree equation: ax + b = 0
            if degree == "1":
                x = -b / a

                result.append(f"جواب معادله: x = {format_fraction(x)}")
                result.append(
                    f"مقدار تقریبی: {format_decimal(float(x))}"
                )

            # Second-degree equation: ax² + bx + c = 0
            else:
                delta = b * b - 4 * a * c

                result.append(f"دلتا = {format_fraction(delta)}")

                if delta > 0:
                    if is_perfect_square_fraction(delta):
                        sqrt_delta = Fraction(
                            isqrt(delta.numerator),
                            isqrt(delta.denominator)
                        )

                        x1 = (-b + sqrt_delta) / (2 * a)
                        x2 = (-b - sqrt_delta) / (2 * a)

                        result.extend([
                            f"x1 = {format_fraction(x1)}",
                            f"x2 = {format_fraction(x2)}",
                            f"مقدار تقریبی x1 = {format_decimal(float(x1))}",
                            f"مقدار تقریبی x2 = {format_decimal(float(x2))}"
                        ])

                    else:
                        # Irrational roots: calculate decimal approximations.
                        sqrt_delta = sqrt(float(delta))

                        x1 = (-float(b) + sqrt_delta) / (2 * float(a))
                        x2 = (-float(b) - sqrt_delta) / (2 * float(a))

                        result.extend([
                            f"x1 ≈ {format_decimal(x1)}",
                            f"x2 ≈ {format_decimal(x2)}",
                            "ریشه‌ها گنگ هستند؛ جواب‌ها تقریبی‌اند."
                        ])

                elif delta == 0:
                    x = -b / (2 * a)

                    result.append(
                        f"ریشه تکراری: x = {format_fraction(x)}"
                    )

                else:
                    # Complex roots.
                    real = -b / (2 * a)
                    imaginary = sqrt(float(-delta)) / abs(2 * float(a))

                    result.extend([
                        "ریشه حقیقی نداریم؛ دو ریشه مختلط داریم.",
                        (
                            f"x1 ≈ {format_decimal(float(real))} "
                            f"+ {format_decimal(imaginary)}i"
                        ),
                        (
                            f"x2 ≈ {format_decimal(float(real))} "
                            f"- {format_decimal(imaginary)}i"
                        )
                    ])

        except (ValueError, ZeroDivisionError, OverflowError):
            result = [
                "خطا: ضرایب را بررسی کن؛ اعداد باید معتبر باشند و مخرج کسر صفر نباشد."
            ]

    return render_template(
        "index.html",
        result=result,
        degree=degree,
        a=a_input,
        b=b_input,
        c=c_input
    )


if __name__ == "__main__":
    app.run(debug=True)
