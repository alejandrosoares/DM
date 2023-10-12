function getUrl() {
    const href = window.location.href;
    const colonIndex = href.indexOf(':');
    const slashIndex = href.indexOf('/', colonIndex + 3); // slashes after + 1
    return href.substring(0, slashIndex);
}


export {
    getUrl
}