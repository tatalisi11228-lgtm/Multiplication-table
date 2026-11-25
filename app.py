from flask import Flask, render_template, request, redirect, url_for, session
from decimal import Decimal, InvalidOperation

app = Flask(__name__)

app.secret_key = "my-secret-key-123"

# Initial account balance
balance = Decimal("0.00")

# Transaction history
transactions = []


# LOGIN PAGE
@app.route("/", methods=["GET", "POST"])
def login():

    if session.get("logged_in"):
        return redirect(url_for("bank"))

    error = ""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "legacy" and password == "8134":

            session.clear()
            session["logged_in"] = True

            return redirect(url_for("bank"))

        error = "Username or password is incorrect."

    return render_template("login.html", error=error)


# BANK PAGE
@app.route("/bank", methods=["GET", "POST"])
def bank():

    global balance

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    error = ""
    message = ""

    if request.method == "POST":

        action = request.form.get("action")

        try:

            amount = Decimal(request.form.get("amount", "0"))

            if not amount.is_finite() or amount <= 0:

                error = "Please enter a valid amount."

            elif action == "deposit":

                balance += amount

                transactions.insert(0, {
                    "type": "Deposit",
                    "amount": amount
                })

                message = "Deposit successful!"

            elif action == "withdraw":

                if amount > balance:

                    error = "Insufficient balance!"

                else:

                    balance -= amount

                    transactions.insert(0, {
                        "type": "Withdraw",
                        "amount": amount
                    })

                    message = "Withdrawal successful!"

            else:

                error = "Invalid operation."

        except (InvalidOperation, ValueError):

            error = "Please enter a valid number."

    return render_template(
        "bank.html",
        balance=f"{balance:,.2f}",
        transactions=transactions,
        error=error,
        message=message
    )


# LOGOUT
@app.route("/logout")
def logout():

    session.clear()

    response = redirect(url_for("login"))
    response.headers["Cache-Control"] = "no-store"

    return response


# RUN APPLICATION
if __name__ == "__main__":
    app.run(debug=True)
