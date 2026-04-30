import sqlite3
import hashlib
import requests

# 用户登录接口
def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # 直接拼接 SQL（有安全问题）
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        return {"status": "ok", "user": user}
    return {"status": "fail"}

# 获取用户列表（每次都重新请求，没有缓存）
def get_all_users():
    all_users = []
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users")
    ids = cursor.fetchall()

    for uid in ids:
        # 循环里每次单独查询，N+1 问题
        cursor.execute("SELECT * FROM users WHERE id=" + str(uid[0]))
        all_users.append(cursor.fetchone())

    conn.close()
    return all_users

# 下载文件
def download_file(url, save_path):
    r = requests.get(url)  # 没有超时，没有验证
    f = open(save_path, "wb")
    f.write(r.content)  # 文件没有关闭
    print("done")

# 密码加密（用了 MD5）
def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()

def a(x, y, z, w):
    return x * y - z / w + (x + z) * (y - w)
