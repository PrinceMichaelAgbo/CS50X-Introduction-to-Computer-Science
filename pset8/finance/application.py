import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

from datetime import datetime
import re


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    balance = db.execute("SELECT cash FROM users WHERE id = :id",
                          id=session['user_id'])
    balance = balance[0]["cash"]
    cash_row = ["CASH", "", "", "", usd(balance)]
    all_rows = []
    final_total = balance

    #update totalvalue with current price from lookup, in totalshares table
    all_shares = db.execute("SELECT symbol, numshares FROM totalshares WHERE id = :id",
                          id=session['user_id'])
    if all_shares != None and len(all_shares) > 0:
        for row in all_shares:
            update_totvalue = row["numshares"] * lookup(row["symbol"])["price"]
            db.execute("UPDATE totalshares SET totalvalue = :update_totvalue WHERE id = :id AND symbol = :symbol",
            update_totvalue=update_totvalue, id=session["user_id"], symbol=row["symbol"])

    rows = db.execute("SELECT symbol, numshares, totalvalue FROM totalshares WHERE id = :id",
                          id=session['user_id'])
    if rows==None or len(rows) < 1:
        all_rows.append(cash_row)
        return render_template("index.html", all_rows=all_rows, final_total=usd(final_total))
    else:
        for row in rows:
            if row["numshares"] > 0:
                share_row = []
                share_row.append(row["symbol"])
                share_row.append(lookup(row["symbol"])["name"])
                share_row.append(row["numshares"])
                share_row.append(usd(lookup(row["symbol"])["price"]))
                share_row.append(usd(row["totalvalue"]))
                final_total = final_total + row["totalvalue"]
                all_rows.append(share_row)
        all_rows.append(cash_row)
        return render_template("index.html", all_rows=all_rows, final_total=usd(final_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Must enter a symbol", 400)
        num_shares = request.form.get("shares")
        if not num_shares:
            return apology("Must enter some number of shares to buy", 400)
        company_quote = lookup(symbol)
        if company_quote == None:
            return apology("Invalid Symbol", 400)
        num_shares = int(num_shares)
        if num_shares <= 0:
            return apology("Must enter a positve number of shares to buy", 400)
        balance = db.execute("SELECT cash FROM users WHERE id = :id",
                          id=session['user_id'])
        balance = balance[0]["cash"]
        cost = num_shares * company_quote["price"]
        if balance < cost:
            return apology("Insufficient cash", 400)
        else:
            new_balance = balance - cost
            date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            # Update history in history table
            return_val = db.execute("INSERT INTO 'history' (id, symbol, shares, price, transacted) VALUES (:id, :symbol, :shares, :price, :transacted)",
            id=session["user_id"], symbol=company_quote["symbol"], shares=num_shares, price=company_quote["price"], transacted = date_time)
            if return_val == None:
                return apology("something went wrong", 403)


            #Update total number and value of each shares (symbol) held in totalshares table
            rows = db.execute("SELECT id, symbol, numshares, totalvalue FROM totalshares WHERE id = :id AND symbol = :symbol",
            id=session["user_id"], symbol=company_quote["symbol"])
            if len(rows) != 1: #if nothing is returned i.e id and symbol combination does not already exist, insert it
                return_val = db.execute("INSERT INTO totalshares (id, symbol, numshares, totalvalue) VALUES (:id, :symbol, :numshares, :totalvalue)",
                                        id=session["user_id"], symbol=company_quote["symbol"], numshares=num_shares, totalvalue=cost)
                if return_val == None:
                    return apology("something went wrong", 403)
            else: #if id, symbol combination exists already, update numshares and totalvalue
                new_numshares = rows[0]["numshares"] + num_shares
                new_totalvalue = rows[0]["totalvalue"] + cost
                return_val = db.execute("UPDATE totalshares SET numshares = :new_numshares, totalvalue = :new_totalvalue WHERE id = :id AND symbol = :symbol",
                                        new_numshares=new_numshares, new_totalvalue=new_totalvalue, id=session["user_id"], symbol=company_quote["symbol"])
                if return_val == None:
                    return apology("something went wrong", 403)

            #Update balance in users table
            return_val = db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=new_balance, id=session["user_id"])
            if return_val != None:
                return redirect("/")
            else:
                return apology("something went wrong", 403)

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    """Show portfolio of stocks"""
    all_rows = []
    rows = db.execute("SELECT * FROM history WHERE id = :id",
                          id=session['user_id'])
    if rows==None or len(rows) < 1:
        return render_template("history.html", all_rows=all_rows)
    else:
        for row in rows:
            share_row = []
            share_row.append(row["symbol"])
            share_row.append(row["shares"])
            share_row.append(usd(row["price"]))
            share_row.append(row["transacted"])
            all_rows.append(share_row)
        return render_template("history.html", all_rows=all_rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("quote")
        if not symbol:
            return apology("Must enter a symbol to get quote", 400)
        company_quote = lookup(symbol)
        if company_quote == None:
            return apology("Invalid Symbol", 400)
        company_quote = "A share of " + company_quote["name"] + ",Inc. (" + company_quote["symbol"] + ") costs " + usd(company_quote["price"]) + "."
        return render_template("quoted.html", company_quote=company_quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        #Ensure username does not already exist
        if len(rows) != 0:
            return apology("username already exists, try a different username", 403)


        # Ensure password and confirmation was submitted
        if not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide BOTH password and confirmation", 403)

        #Ensure password contains letter and number
        password = request.form.get("password").upper()
        if len(password) < 5 or re.search('[0-9]', password) is None or re.search('[A-Z]', password) is None:
            return apology("Password requirements: at least 5 characters, at least one letter and one number", 400)

        #Ensure password and confirmation match
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("password does not match confirmation", 403)

        #Insert user into users database
        username = request.form.get("username")
        password_hash = generate_password_hash(request.form.get("password"))
        return_val = db.execute("INSERT INTO users (username, hash) VALUES (:username, :password_hash)", username=username, password_hash=password_hash)

        #redirect user to homepage
        if return_val != None:
            return redirect("/")
        else:
            return apology("something went wrong", 403)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Must enter a symbol", 400)
        num_shares = request.form.get("shares")
        if not num_shares:
            return apology("Must enter some number of shares to sell", 400)
        company_quote = lookup(symbol)
        if company_quote == None:
            return apology("Invalid Symbol", 400)
        num_shares = int(num_shares)
        if num_shares <= 0:
            return apology("Must enter a positve number of shares to sell", 400)

        rows = db.execute("SELECT id, symbol, numshares FROM totalshares WHERE id = :id AND symbol = :symbol",
            id=session["user_id"], symbol=company_quote["symbol"])
        if len(rows) != 1:
            return apology("You do not have shares of " + symbol, 400)
        if num_shares > rows[0]["numshares"]:
            return apology("You cannot sell more shares than you have", 400)

        sale_value = num_shares * company_quote["price"]

        balance = db.execute("SELECT cash FROM users WHERE id = :id",
                          id=session['user_id'])
        balance = balance[0]["cash"]
        new_balance = balance + sale_value
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # Update history in history table
        return_val = db.execute("INSERT INTO 'history' (id, symbol, shares, price, transacted) VALUES (:id, :symbol, :shares, :price, :transacted)",
        id=session["user_id"], symbol=company_quote["symbol"], shares=num_shares*-1, price=company_quote["price"], transacted = date_time)
        if return_val == None:
            return apology("something went wrong", 403)

        #Update total number and value of each shares (symbol) held in totalshares table
        rows = db.execute("SELECT id, symbol, numshares, totalvalue FROM totalshares WHERE id = :id AND symbol = :symbol",
        id=session["user_id"], symbol=company_quote["symbol"])
        new_numshares = rows[0]["numshares"] - num_shares
        new_totalvalue = rows[0]["totalvalue"] - sale_value
        return_val = db.execute("UPDATE totalshares SET numshares = :new_numshares, totalvalue = :new_totalvalue WHERE id = :id AND symbol = :symbol",
                                new_numshares=new_numshares, new_totalvalue=new_totalvalue, id=session["user_id"], symbol=company_quote["symbol"])
        if return_val == None:
            return apology("something went wrong", 403)

        #Update balance in users table
        return_val = db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=new_balance, id=session["user_id"])
        if return_val != None:
            return redirect("/")
        else:
            return apology("something went wrong", 403)
    else:
        rows = db.execute("SELECT symbol, numshares FROM totalshares WHERE id = :id", id=session["user_id"])
        symbol_options = []
        if rows != None and len(rows) > 0:
            for row in rows:
                if row["numshares"] > 0:
                    symbol_options.append(row["symbol"])
        return render_template("sell.html", symbol_options=symbol_options)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
