import requests

def import_gists_to_database(db, username, commit=True):
    url = 'https://api.github.com/users/{}/gists'.format(username)
    response = requests.get(url)
    data = response.json()
    
    for 
    
    
#     import pdb; pdb.set_trace()


#     db.requests.get()
#     query = 'SELECT * FROM gists where github_id=user;'
#     cursor = db.execute(query)
#     return cursor.fetchall()

sql = """INSERT INTO mytable VALUES :github_id, :created_at"""

values = {'github_id': 2, 'created_at': '2019-06-05'}

cursor = db.execute(sql, values)
cursor.commit()