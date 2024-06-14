import requests


def registerwithApi(nama: str, username:str, password:str):
    try:
        url = "http://127.0.0.1:8000/api/v1/data-karyawan/register/"
        data = {
            "nama": nama,
            "username": username,
            "password": password
        }

        res = requests.post(url=url, json=data)
        dt = res.json()
        print(dt)
        if dt.get("statusCode") != "00":
            message = dt.get("message")
            return None, f"register{message}"
        
        data = dt.get("data")
        return data, None
    
    except Exception as e:
        return None, e

def tambahData(nama:str, jabatan:str, department:str):
    try:
        url = "http://127.0.0.1:8000/api/v1/data-karyawan/tambah-data-karyawan/"
        data = {
            "nama": nama,
            "jabatan": jabatan,
            "department": department
        }
        res = requests.post(url = url, json = data)
        dt = res.json()
        print(dt)
        if dt.get("statusCode") != "00":
            message = dt.get("message")
            return None, f"tambah data {message}"
        
        data = dt.get("data")
        return data, None
        
    except Exception as e:
        return None, e
    
def hapusData(id:int):
    try:
        url = "http://127.0.0.1:8000/api/v1/data-karyawan/delete-data-karyawan/"
        data = {
            "id":id
        }
        res = requests.delete(url = url, json = data)
        dt = res.json()
        print(dt)
        if dt.get("statusCode") != "00":
            message = dt.get("message")
            return None, f"tambah data {message}"
        
        data = dt.get("data")
        return data, None
        
    except Exception as e:
        return None, e
    
def loginWithApi(username: str, password: str):
    try:
        # hit api ke service login next meet
        url = "http://127.0.0.1:8000/api/v1/data-karyawan/login/" 
        data = {
            "username": username,
            "password": password
        }       
        res = requests.post(url=url, json=data)
        dt = res.json()
        print(dt)
        if dt.get("statusCode") != "00":
            message = dt.get("message")
            return None, f"login {message}"

        data = dt.get("data")
        return data, None
       
    except Exception as e:
        return None, str(e)

def getData():
    try: 
        url = "http://127.0.0.1:8000/api/v1/data-karyawan/lihat-data-karyawan/"     
        resData = getUrl(url)

        return resData, None
    except Exception as e:
        return None, e
    
def getUrl(url: str):
    try:
        r = requests.get(url)
        data = r.json()
        dataUrl = data.get('data')

        return dataUrl

    except Exception as e:
        return None, e


def getDataId(id:int):
    try:
        url = f"http://127.0.0.1:8000/api/v1/data-karyawan/lihat-data-karyawan-by-id/?id={id}"
        resData = getUrl(url)
        return resData, None

    except Exception as e:
        return None, e
 
def updateData(id:int, nama:str, jabatan:str, department:str):
    try:
        url = "http://127.0.0.1:8000/api/v1/data-karyawan/update-data-karyawan/"
        data = {
            "id":id,
            "nama": nama,
            "jabatan": jabatan,
            "department": department
        }
        res = requests.post(url = url, json = data)
        dt = res.json()
        print(dt)
        if dt.get("statusCode") != "00":
            message = dt.get("message")
            return None, f"tambah data {message}"
        
        data = dt.get("data")
        return data, None
        
    except Exception as e:
        return None, e


