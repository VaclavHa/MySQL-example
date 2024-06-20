import requests

URL = "http://127.0.0.1:5000/"


def get_invoice(url: str):
    response = requests.get(url)

    return print(response.text)


def add_data_to_invoice(url: str, invoice_number: str, employee_id: int, customer_id: int, total_amount: float):
    data = {
        'invoice_number': invoice_number,
        'employee_id': employee_id,
        'customer_id': customer_id,
        'total_amount': total_amount
    }

    url = url + "/add"
    response = requests.post(url, json=data)

    return print(response.text)


def delete_data_invoice(url: str, invoice_id: str):
    data = {
        'invoice_id': invoice_id
    }

    url = url + "/delete"

    response = requests.post(url, json=data)

    return print(response.text)


if __name__ == '__main__':
    pass
