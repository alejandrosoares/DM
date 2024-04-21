const buildApiResponseObject = (expectedCode, receivedCode, data) => {
    return {
        isOk: expectedCode === receivedCode,
        data
    };
};

export default buildApiResponseObject;