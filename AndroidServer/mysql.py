import pymysql


def mysql(sql, ty=0):
    conn = pymysql.connect(host="47.98.116.174",user="root", port=3306, passwd="ssy123456s", database="android")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    if ty==1:
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    else:
        cur.close()
        conn.close()
        return