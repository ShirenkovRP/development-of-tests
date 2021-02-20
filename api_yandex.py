import requests

token_ynd = "token_ynd_self"

# создание папки
url_yandex = "https://cloud-api.yandex.net/v1/disk/resources"
authorization = {"Authorization": f"OAuth {token_ynd}"}
name_folder = "FGHJ"

result = requests.put(url_yandex,
                      headers=authorization,
                      params={"path": f"/{name_folder}"}
                      )
result_get = requests.get(url_yandex,
                          headers=authorization,
                          params={"path": f"/{name_folder}"}
                          )
