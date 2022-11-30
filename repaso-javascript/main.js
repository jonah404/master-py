alert('Hola Mundo!')

var nombre = "Jonatan";
var altura = 190;

/*
var concatenacion = nombre + " " + altura;

//document.write(nombre);
//document.write(altura);

document.write(concatenacion)

var datos = document.getElementById("datos");
//datos.innerHTML = concatenacion;

datos.innerHTML = `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Mido: ${altura}</h3>
`;

if (altura >= 190){
    datos.innerHTML += `<h1>Eres una persona alta</h1>`
}else{
    datos.innerHTML += `<h1>Eres una persona baja</h1>`
}

for(var i = 1985; i<=2022; i++){
    //bloque de instrucciones
    datos.innerHTML += "<h2>Estamos en el año: " + i;
}
*/

function MuestraMiNombre(nombre, altura){
    var datos = document.getElementById("datos");
//datos.innerHTML = concatenacion;

    var misDatos = `
        <h1>Soy la caja de datos</h1>
        <h2>Mi nombre es: ${nombre}</h2>
        <h3>Mido: ${altura}</h3>
    `;
    return misDatos;
}

function Imprimir(){
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre("Jonatan", 190);
}

Imprimir()

var nombres = ['Jonatan', 'Paola', 'Paula'];
//alert(nombres[1]);


document.write('<h1>Listado de nombres</h1>');
/*
for (i = 0; i< nombres.length; i++){
    document.write(nombres[i] + '<br>')
};*/

/*
nombres.forEach(function(nombre){
    document.write(nombres + '<br>');
});*/

nombres.forEach((nombre) => {
    document.write(nombres + '<br>');
});
