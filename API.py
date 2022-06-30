import request

get_phone=requests.get('http://localhost:5000/api?action=phone&name=Urban')
get_name=requests.get('http://localhost:5000/api?action=name&phone=0435-4355438')


