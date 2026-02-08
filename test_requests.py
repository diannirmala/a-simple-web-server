"""
test_requests.py

Mengirim HTTP GET request ke Google dan menampilkan:
- status code
- content length (header jika ada)
- ukuran body aktual
- isi response (HTML)
"""

import requests

def fetch_google_homepage():
    """
    Mengambil halaman utama Google menggunakan HTTP GET.

    Returns:
        response (requests.Response): objek response dari server
    """
    response = requests.get('https://www.google.com/')
    return response

response = fetch_google_homepage()

print('status code:', response.status_code)
print('content length:', response.headers.get('content-length'))
# if none
print('content length manual:', len(response.content))
print(response.text)

"""
202 = success
404 = not found
500 = server error

"""


