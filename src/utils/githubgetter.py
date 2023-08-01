from requests import get


def githubgetterpopular():
    url = "https://api.gitterapp.com/repositories?language=python&since=daily"
    in_info = get(url).json()

    return in_info[0]["description"]


if __name__ == "__main__":
    print(githubgetterpopular())
