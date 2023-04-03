import requests

def githubgetterpopular():
    url = 'https://api.gitterapp.com/repositories?language=python&since=daily'
    in_info = requests.get(url).json()


    return(in_info[0]["description"])