const siajs = require('siajs');
var fs = require('fs');

function busquedaMaterias(palabra){
  siajs.getSubjects(palabra).then(res => {
    // fs.writeFile('./'+palabra+'.json',JSON.stringify(res),error => {
    //   if (error)
    //     console.log(error);
    //   else
    //     console.log('El archivo fue creado');
    // });
    console.log(res);
  }).catch(err => {
    console.log(err);
  });
}

function busquedaGrupos(codigo){
  siajs.getGroups(codigo).then(res => {
  	// fs.writeFile('./'+codigo+'.json',JSON.stringify(res),error => {
   //    if (error)
   //      console.log(error);
   //    else
   //      console.log('El archivo fue creado');
   //  });
    console.log(res);
  }).catch(err => {
    console.log(err);
  });
}

busquedaMaterias("");
busquedaGrupos("");
