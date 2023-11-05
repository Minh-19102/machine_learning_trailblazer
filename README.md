# machine_learning_trailblazer

## Hướng dẫn cài đặt

1. [Download & install Python](https://www.python.org/downloads/) (trên windows cần thêm bin vào Path)
2. [Download & install PIP](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)

3. Tạo fork của project trên github.
4. Clone repo

```bash
git clone https://github.com/{username}/machine_learning_trailblazer.git

cd machine_learning_trailblazer
```

5. Tạo virtual environment

```bash
python -m venv env
```

6. (Chỉ cần chạy lần đầu nếu chưa active) active execution trên window:
   - Mở windows powershell bằng admin

```bash
Set-ExecutionPolicy RemoteSigned

>> y
```

7. Active virtual environment

- windows

```bash
env\Scripts\activate
```

- Linux

```bash
source env/bin/activate
```

6. Install package cần thiết

```bash
pip install -r requirements.txt
```

## Hướng dẫn chạy

1. Install package (nếu có thay đổi file requirements.txt)

```bash
pip install -r requirements.txt
```

2. Vào virtual environment

- windows

```bash
env\Scripts\activate
```

- Linux

```bash
source env/bin/activate
```

3. Chạy jupyter lab

```bash
jupyter lab
```

## Hướng dẫn cài đặt package, thư viện mới

1. Cài đặt package, thư viện

```
pip install {tên package}
```

2. Lưu vào requirements.txt

```
pip freeze > requirements.txt
```
