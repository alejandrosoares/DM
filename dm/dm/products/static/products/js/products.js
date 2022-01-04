let URL, PRODUCTS;
let START = 0, END = 10;

const containerProducts = document.getElementById("products"),
    loader = document.querySelector("#products .loader"),
    template = document.getElementById("item-product").content,
    fragment = document.createDocumentFragment();


function showLoader(show){
    (show)
    ? loader.classList.remove("d-none")
    : loader.classList.add("d-none");
}

function createProductList(){

    PRODUCTS.forEach(p => {
        const card = template.querySelector("div.card"),
            img = template.querySelector("div.con-img img"),
            name = template.querySelector("div.name > p"),
            price = template.querySelector("div.price > span"),
            code = template.querySelector("div.in-stock > span");
        
        card.setAttribute("data-id", p.id);
        img.src = p.img;
        name.textContent = p.name;
        price.textContent = `$ ${p.price}`;
        code.textContent = `Cód: ${p.code}`;

        const clone = document.importNode(template, true);

        fragment.appendChild(clone);
    })

    containerProducts.appendChild(fragment);

    showLoader(false);
}


function clickProducts(e){

    if(e.target.matches("#products .card *")){
        const card = e.target.closest("div.card"),
            product_id = card.getAttribute("data-id");

        location.href = `/products/${product_id}`;
    }
}

function loadProducts(){
    URL = document.querySelector(
        "#products div.information input"
        ).value;
    
    console.log(URL)
    fetch(URL)
    .then(response =>  {
        if(response.ok) return response.json()
    })
    .then(products => {
        console.log(products);
        PRODUCTS = products;
        createProductList();
    })
    .catch(error => console.error(error));

}   

document.addEventListener("DOMContentLoaded", loadProducts)
document.addEventListener("click", clickProducts)