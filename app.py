import requests
from flask import Flask, request, Response

app = Flask(__name__)
TARGET = "http://213.142.135.46:9999"  

@app.before_request
def proxy():
    
    url = f"{TARGET}{request.full_path}"
    if url.endswith("?"):  
        url = url[:-1]

    
    headers = dict(request.headers)
    headers.pop("Host", None)
    headers.pop("Content-Length", None)

    
    resp = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
        stream=True,
    )

    
    excluded_headers = ["content-encoding", "transfer-encoding", "content-length", "connection"]
    response_headers = [(name, value) for name, value in resp.raw.headers.items()
                        if name.lower() not in excluded_headers]

    return Response(resp.content, resp.status_code, response_headers)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
