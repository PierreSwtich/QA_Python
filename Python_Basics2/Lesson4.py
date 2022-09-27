# CRUD

"""
C -> Create | new informations
R -> Read/Retrive | reading exisitng data
U -> Update | modifying exisitng data
D -> Delete | Deleting exisitng data

"""

"""
1xx -> Informations
2xx -> Success
3xx -> Redirections
4xx -> Client's error
5xx -> Server error

"""


import requests

# response = requests.get('https://fabrykatestow.pl')

# print(response)

# post = requests.post('http://httpbin.org/post')
# put = requests.put('http://httpbin.org/put')
# delete = requests.delete('http://httpbin.org/delete')

# print('Method post, and status is :' + str(post))
# print('Method put, and status is :'+ str(put))
# print('Method delete, and status is :'+ str(delete))



parameters = {'key1':'value1', 'key2':'value2'}

r = requests.get('https://fabrykatestow.pl', params=parameters)
print(r.url)
print(r.text)
print(r.encoding)


