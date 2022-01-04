function ClearSearchInput(){
  searchInput.value = "";
}

function FormatText(text){
  text = text.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u");
  text = text.replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U");
  text = text.toUpperCase();
  return text;
}

function SearchWords(){

  let search = searchInput.value,
      formatedSearch = FormatText(search),
      matching = false;
      
  var lengthProductsList = listWordsSearch.length;

  if(search.length > 2){

    containerSearch.innerHTML = "";

    for(var i=0; i < lengthProductsList; i++){
      if(listWordsSearch[i][0].search(formatedSearch) != -1 || listWordsSearch[i][0] == formatedSearch){
        if(listWordsSearch[i][1] !== null ){
          containerSearch.innerHTML = containerSearch.innerHTML + `<li onclick="SearchById('${listWordsSearch[i][3]}', ${i}, ${listWordsSearch[i][2]})">\
          <img class="img-search-results" src="${listWordsSearch[i][1] }" alt="Imagen">\
          <span>${listWordsSearch[i][0].replace(formatedSearch, "<b>" + formatedSearch + "</b>" )}</span></li>`;
        }else{
          // no contiene una imagen, como las marcas
          containerSearch.innerHTML = containerSearch.innerHTML + `<li onclick="SearchById('${listWordsSearch[i][3]}', ${i}, ${listWordsSearch[i][2]})">\
          <span> JUGUETES ${listWordsSearch[i][0].replace(formatedSearch, "<b>" + formatedSearch + "</b>" )}</span></li>`;
        }
        matching = true;
      }
    }
    if(matching){
      HideSearchResults(false);
    }else{
      console.log("false");
      matching = false;
      HideSearchResults(true);
    }

  }else{
    HideSearchResults(true);
  }
}

function Search(){

  // Funcion para buscar lo que se escribe en el input de busqueda
  var value = document.getElementById("searchInput").value;
  let request;

  request = RequestConstruction();
  
  if(request){
    request.onreadystatechange = function(){
      if(request.readyState == 4 && request.status == 200){ 
        document.getElementById("productsContainer").innerHTML = request.responseText;
        RemoveStyleCategories();
        window.setTimeout(function(){
          // Temporizando para que ocurra el evento keyup y luego oculte el cuadro de busquedas
          HideSearchResults(true);
        }, 1000);
      } 
    }   
    request.open("GET", urlSearch+"?q="+value, true);
    request.send();
  }
}

function SearchById(type, i, id){
  // Actua cuando se realiza click en algun resultado de busqueda coincidente con el input de busqueda
  // Los argumentos de la funcion son:
  // *type que indica el tipo de consulta, si es un producto o marca (para buscar en la bases de datos)
  // *i que es el incide de lo clickeado dentro de la lista listWordsSearch, se utiliza para escribir lo clickeado en el input
  // *id de la consulta, puede ser el id de una marca o de un producto
  let request;

  searchInput.value = listWordsSearch[i][0];
  
  request = RequestConstruction();

  if(request){
    request.onreadystatechange = function(){
      if(request.readyState == 4 && request.status == 200){ 
        document.getElementById("productsContainer").innerHTML = request.responseText;
        RemoveStyleCategories(); //Remueve los estilos de las categorias, por si tiene alguna etiqueta seleccionada
      } 
    }
    request.open("GET", urlSearchById+`?q=${id}&t=${type}`, true);
    request.send();
  }
}

function SearchByCategory(id){
  let request;
  request = RequestConstruction();
  if(request){
    request.onreadystatechange = function(){
      if(request.readyState == 4 && request.status == 200){ 
        document.getElementById("productsContainer").innerHTML = request.responseText;
        ChangeStyleCategory(id);
        ClearSearchInput();
      } 
    }   
    request.open("GET", urlSearchByCategory+"?q="+id, true);
    request.send();
  }
}

function KeyPress(e){
  if(e.which === 13){
    Search();
  }
  e.stopPropagation();
}

function ShowResults(e){
  if(containerResults.style.display == "none"){
      SearchWords();
  }
  e.stopPropagation();
}


function HideSearchResults(hide){
  // Si se hace un click en la ventana y el cuadro con resultados de busqueda esta abierto, lo oculta

  if(hide){
    containerResults.style.display = "none";
    searchInput.classList.remove("custom-input-active");
    searchBtn.classList.remove("custom-btn-active");
  }else{
    containerResults.style.display = "block";
    searchInput.classList.add("custom-input-active");
    searchBtn.classList.add("custom-btn-active");
  }
}


function ChangeStyleCategory(id){
  const categories = document.getElementsByClassName("categories"),
        lCategories = categories.length;

  for(var i=0; i < lCategories; i++){
    if(categories[i].getAttribute("idvalue") === id){
      categories[i].classList.add("category-activate");
    }else{
      categories[i].classList.remove("category-activate");
    }
  }
}


function RemoveStyleCategories(){
  const categories = document.getElementsByClassName("categories"),
        lCategories = categories.length;
  for(var i=0; i < lCategories; i++){
    categories[i].classList.remove("category-activate");
  }
}

document.addEventListener("click", function(){HideSearchResults(true)}, false);