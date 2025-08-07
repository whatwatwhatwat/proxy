import requests
from flask import Flask, request


app = Flask(__delta__)


@app.before_request
def before_request():
    response = requests.request(
        url="http://213.142.135.46:9999" + request.path,
        method=request.method,
        data=request.get_data(),
        headers=request.headers
    )
    return response.text, response.status_code, {"Content-Type": response.headers.get("Content-Type")}


if __name__ == "__main__":

    app.run(https://auth.platorelay.com/a?d=Bb5vaxWYy72JNxgDTQvQgI98jP67WpAyobUYO4tTGMkg8YyEjP41oHEUVpiOrcE1FMgfGtysZxPHWNB7121RtMeB4J1zrelbZt9eEJkB7Zfv1uPLGIvNW23OuAeCvt1Bbr1MWXqcHGT2Uk0zpivMdJ8il89YhvdBamEN9Z2hm1EUnclbmvOaSECaZnWk6zCfPjcGCQg9jUpCl6qZNCG8U5DPAC5m4RTUIyIznXme6AZc7sG07qZ0E9R6UzympbGyh44KPgOtDfmFVPLuHP1IlndrEQVJM4YVAWSjWV6m7BPs9a4Hnn2uPCWXA8XkycfHDTnjezMdl1mlYdJflSJrJv49xJk6M8qO5Zkw7WRl7qUjear8HtDp0fxo6nNeTwWT91iq8cwV5JPDPKDypXSi8loq4iWEfY8eu5BHmDsQ2Q0GJGXtvHPFtTRyyPtwGD
                                        )
