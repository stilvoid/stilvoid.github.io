---
title: Cocktail Generator
permalink: /cocktails/
---
<h3 id="cocktail_name"></h3>
<ul id="ingredients"></ul>

<button id="button">Another</button>

<script>
var button = document.getElementById("button");
var cocktail_name = document.getElementById("cocktail_name");
var ingredients = document.getElementById("ingredients");

function go() {
    cocktail_name.innerHTML = "Loading cocktail...";
    ingredients.innerHTML = "";

    var r = new XMLHttpRequest();
    r.open("GET", "https://bmjl7kqkq9.execute-api.eu-west-1.amazonaws.com/", true);
    r.onreadystatechange = function () {
        cocktail = JSON.parse(r.responseText);

        cocktail_name.innerHTML = cocktail.name;
        ingredients.innerHTML = "";
        cocktail.ingredients.forEach(function(ingredient) {
            var item = document.createElement("li");
            item.innerHTML = ingredient;

            ingredients.appendChild(item);
        });
    };
    r.send();
}

button.onclick = go;
go();
</script>
