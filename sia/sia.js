const siajs = require('siajs');
var fs = require('fs');

function busquedaMaterias(palabra){
  siajs.getSubjects(palabra).then(res => {
    fs.writeFile('./'+palabra+'.json',JSON.stringify(res),error => {
      if (error)
        console.log(error);
      else
        console.log('El archivo fue creado');
    });
    /*var x, txt = "";
    obj = { table: "customers", limit: 20 };
    txt += "<table border='1'>"
    for (x in res) {
      txt += "<tr><td>" + res[x].name + "</td></tr>";
    }
    txt += "</table>"    
    document.getElementById("demo").innerHTML = txt;*/
    console.log(res);
  }).catch(err => {
    console.log(err);
  });
}

busquedaMaterias("estadistica");
busquedaGrupos("9941");
function busquedaGrupos(codigo){
  siajs.getGroups(codigo).then(res => {
  	fs.writeFile('./'+codigo+'.json',JSON.stringify(res),error => {
      if (error)
        console.log(error);
      else
        console.log('El archivo fue creado');
    });
    console.log(res);
  }).catch(err => {
    console.log(err);
  });
}

