function normalizeText(text) {
    text = text
       .replaceAll("á", "a")
       .replaceAll("é", "e")
       .replaceAll("í", "i")
       .replaceAll("ó", "o")
       .replaceAll("ú", "u");
    text = text
       .replaceAll("Á", "A")
       .replaceAll("É", "E")
       .replaceAll("Í", "I")
       .replaceAll("Ó", "O")
       .replaceAll("Ú", "U");
    return text.toUpperCase();
}


export {
    normalizeText
}