const siajs = require('siajs');
var p5 = require('p5');

function busquedaGrupos(codigo){
  siajs.getGroups(codigo).then(res => {

  }).catch(err => {
    console.log(err);
  });
}

let input, button, greeting;
function drawResults(){
	background(255);
	const palabra = input.value();
	siajs.getSubjects(palabra).then(res => {
		if(res.count>=0){
			// result = createElement('h3', 'Su busqueda tiene ' + res.count + ' resultados');
			// result.position(20, 70);
			// result.addClass('resultado');
			// textAlign(CENTER);
			// textSize(30);
		}
	  	for (var i = 0; i <=res.count-1; i++) {	
			rect(250,150+i*50,300,50);
			textSize(15);
			textAlign(CENTER, CENTER);
			text(res.list[i].name,500,150+i*50);
		}	  		
	}).catch(err => {
	    console.log(err);
	 //    result = createElement('h3', 'Ocurrio un error');
		// result.position(20, 70);
		// textAlign(CENTER);
		// textSize(30);
	});	
}

module.exports = new p5(function () {
  this.setup = function setup () {
    this.createCanvas(700, 800)
	input = createInput();
	input.position(20, 65);

	button = createButton('Buscar');
	button.position(input.x + input.width, 65);
  	button.mousePressed(drawResults);

	greeting = createElement('h2', 'Materias a Buscar:');
	greeting.position(20, 5);
	textAlign(CENTER);
	textSize(50);
	textSize(50);
	textAlign(CENTER);
	strokeWeight(3);
	textStyle(BOLD);
	text('¡Bienvenido a Poredak!', width/2,height/5);
	textStyle(NORMAL);
	textSize(40);
	strokeWeight(0);
	text('Tu Organizador de Horarios', width/2,2*height/7);
	textSize(20);
	text('Por favor ingresa el nombre de la materia que deseas inscribir', width/8,5*height/15,6*width/8,height/7);
  }
  this.draw = function draw () {
  }
})