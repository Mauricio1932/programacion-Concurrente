
import time
import requests


def url_ok(url_site, timeout):
    respuesta = requests.head(url_site, timeout=timeout)
    if respuesta.status_code != 200:
        print (str(i) + " " + str(respuesta.status_code) +"Pagina no establecida")
    else:
        print(str(i) + " " + str(respuesta.status_code) + "Pagina funcionando")


link = ["https://github.com/", "https://platinum.upchiapas.edu.mx/alumnos/login", "https://www.amazon.com/", "https://www.amazon.com/",
        "https://www.ebay.com/", "https://www.mercadolibre.com.mx/", "https://www.wish.com/mx", "https://www.shein.com.mx/",
        "https://www.oracle.com/mx/", "https://discord.com/", "https://www.python.org/", "https://www.parrotsec.org/",
        "https://developer.mozilla.org/es/docs/Web/JavaScript", "https://www.ruby-lang.org/es/", "https://www.Yahoo.es",
        "https://www.wikipedia.org", "https://www.google.com.mx/", "https://www.rae.es/", "https://www.postgresql.org/",
        "https://mariadb.org/", "https://www.mongodb.com/", "https://www.npmjs.com/", "https://react-bootstrap.github.io/", "https://getbootstrap.com/"
        ]


if __name__ == "__main__":

    while True:
        for i in link:
            url_ok(i, timeout=5)
        time.sleep(240)
