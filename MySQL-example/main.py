from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Database configuration
config = {
    'user': 'root',
    'password': 'MySQL_testing08',
    'host': '127.0.0.1',
    'database': 'tire_shop',
}


def get_db_connection():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except Exception as e:
        print(f"Error occured: {e}")
        return None


@app.route("/", methods=['GET'])
def get_invoice():
    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM invoice")
            rows = cursor.fetchall()
            invoice = {'invoice': {}}
            for row in rows:
                invoice_id = row[0]
                invoice_number = row[1]
                customer_id = row[2]
                employee_id = row[3]
                total_amount = row[4]

                invoice_details = {
                    'invoice_number': invoice_number,
                    'customer_id': customer_id,
                    'employee_id': employee_id,
                    'total_amount': total_amount
                }

                invoice["invoice"][invoice_id] = invoice_details

            return jsonify(invoice)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({"error": "Connection not established"}), 500


@app.route("/add", methods=['POST'])
def add_invoice():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400

    invoice_number = data.get("invoice_number")
    customer_id = data.get("customer_id")
    employee_id = data.get("employee_id")
    total_amount = data.get("total_amount")

    if not all([invoice_number, customer_id, employee_id, total_amount]):
        return jsonify({"error": "Missing data"}), 400

    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO invoice (invoice_number, customer_id, employee_id, total_amount)"
                "VALUES (%s, %s, %s, %s)", (invoice_number, customer_id, employee_id, total_amount)
            )
            conn.commit()
            return jsonify({"success": "Invoice added"}), 201
        except Exception as e:
            conn.rollback()
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({"error": "Connection not established"}), 500


@app.route("/delete", methods=['POST'])
def delete_invoice():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400

    invoice_id = data.get("invoice_id")
    if not invoice_id:
        jsonify({"Error": "Invoice not found"}), 400

    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM invoice WHERE invoice_id = %s", (invoice_id,))
            conn.commit()
            return jsonify({"success": "Invoice deleted"}), 200
        except Exception as e:
            conn.rollback()
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({"error": "Connection not established"}), 500


if __name__ == '__main__':
    app.run(debug=True)
