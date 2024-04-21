function send(request, url, success, failed) {
    _send();

    function _send() {
	    fetch(url, request)
            .then( response => {
                if (response.ok) return response.json();
            })
            .then( object => {
                if (object.status === "ok") {
                    success(object);
                } else {
                    failed(object);
                }
            })
            .catch(error => failed(object));
    }
}


async function sendSync(request, url) {
    const response = await fetch(url, request)
            .then( response => {
                if (response.ok) return response.json();
            })
            .then( object => {
                return (object.status === "ok")? object: null;
            })
            .catch(error => console.error(error));
    return response;
}


function buildPostRequest(data, token) {
    const headers = buildHeaders(token);
    return {
        method: 'POST',
        headers: headers,
        body: data? JSON.stringify(data): null
    };
}


function buildGetRequest(token) {
    const headers = buildHeaders(token);
    return {
        method: 'GET',
        headers: headers,
    };
}


function buildHeaders(token = null) {
    const headers = new Headers();
    headers.set("Content-Type", "application/json");
    headers.set("X-CSRFToken", token || getDefaultToken());
    headers.set("Access-Control-Allow-Origin", "same-origin");
    return headers;
}


function getDefaultToken() {
    const divReferences = document.querySelector('div.data-reference');
    const inputToken = divReferences.querySelector('input[name="csrfmiddlewaretoken"]');
    return inputToken.value;
}

// TODO: Replace functions above with the Request class below
class Request {

    constructor(build) {
        this.url = build.url;
        this.body = build.body;
        this.method = build.method;
        this.headers = build.headers;
        this.params = build.params;
    }

    send = async () => {
        const req = this._build();
        const url = this._getUrlWithParamsIfNeeded();
        try {
            return await fetch(url, req);
        } catch (error) {
            console.error(`Error fetching resourse: ${this.url}`, error);
            throw error;
        }
    }

    _getUrlWithParamsIfNeeded = () => {
        if (!this.params) return this.url;
        const params = new URLSearchParams(this.params);
        return `${this.url}?${params}`;
    }

    _build = () => {
        const req = {
            method: this.method,
            headers: this.headers,
            body: this.body ? JSON.stringify(this.body) : null,
        };
        return req;
    }

    static get Builder() {

        class Builder {
            constructor(url) {
                this.url = url;
                this.method = 'GET';
                this.headers = new Headers({ 'Content-Type': 'application/json' });
                this.body = null;
                this.params = null;
            }

            withBody(body) {
                this.body = body;
                return this;
            }

            withGetMethod() {
                this.method = 'GET';
                return this;
            }

            withPostMethod() {
                const csrfToken = this._getCsrfToken();
                this.method = 'POST';
                this.headers.set('X-CSRFToken', csrfToken);
                return this;
            }

            withGetParams(params) {
                this.params = params;
                return this;
            }

            build() {
                return new Request(this);
            }

            _getCsrfToken() {
                const pageData = document.getElementById('page-data');
                const selector = 'input[name="csrfmiddlewaretoken"]';
                const element = pageData.querySelector(selector);

                if (!element) {
                    throw new Error('CSRF token not found');
                }

                return element.value;
            }
        }

        return Builder;
    }
}


export {
    send,
    sendSync,
    buildPostRequest,
    buildGetRequest,
    Request
};