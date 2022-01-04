function ShowProduct(code, pathImg, name, price, inStock, description){

const codeContainer = document.getElementById("showProductCode"),
imgContainer = document.getElementById("showProductImg"),
nameContainer = document.getElementById("showProductName"),
inStockContainer = document.getElementById("showProductStock"),
priceContainer = document.getElementById("showProductPrice");
descriptionContainer = document.getElementById("showProductDescription");

  codeContainer.innerHTML = "Cod: "+ code;
  imgContainer.src = pathImg;
  nameContainer.innerHTML = name;
  priceContainer.innerHTML = "$ " + price;
  if(inStock){
    inStockContainer.innerHTML = "En Stock";
  }else{
    inStockContainer.innerHTML = "Agotado";
  }

  if(!description === false){
    descriptionContainer.innerHTML = description.replace(";","<br>");
    document.querySelector("hr.hr-description").style.display = "block";
    document.querySelector("div.row-description.row").style.display = "block";
  }else{
    document.querySelector("hr.hr-description").style.display = "none";
    document.querySelector("div.row-description.row").style.display = "none";
  }

 InsertCodeDisplayed(code);
}

function CloseModalBtn(){
  $("#modalQuickView").modal("hide");
  const body = document.querySelector("body");
  body.style = "overflow:auto";
}