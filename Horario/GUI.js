const siajs = require('siajs');
var p5 = require('p5');

function busquedaGrupos(codigo){
  siajs.getGroups(codigo).then(res => {

  }).catch(err => {
    console.log(err);
  });
}

let inp, page, buscar, gh, c, home, dia;
function drawResults(){
	const palabra = inp.value();
	siajs.getSubjects(palabra).then(res => {
		//if(res.count>=0){
			// result = createElement('h3', 'Su busqueda tiene ' + res.count + ' resultados');
			// result.position(20, 70);
			// result.addClass('resultado');
			// textAlign(CENTER);
			// textSize(30);
		//}
	 //  	for (var i = 0; i <=res.count-1; i++) {	
		// 	rect(250,150+i*50,300,50);
		// 	textSize(15);
		// 	textAlign(CENTER, CENTER);
		// 	text(res.list[i].name,500,150+i*50);
		// }	  		
	}).catch(err => {
	    console.log(err);
	});	
}
module.exports = new p5(function () {
  this.setup = function setup () {
	createCanvas(windowWidth, windowHeight);
	removeElements();
	dia=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];
	page = 'home';
	c = false;
	stroke(0);
	fill(0);

	//Creación de Botones
	createHome();
	createInp();
	createBuscar();
	createGH();  
	home.remove();
  }
  this.draw = function draw () {
	if(page == 'home' && c == false){
		drawHome();
	}else if(page == 'horarios' && c == false){
		schedule();
	}
  }
})

function drawHome(){
  background(221);
  textSize(2*(height*width)/(13*(height+width)));
  textAlign(CENTER);
  strokeWeight(3);
  textStyle(BOLD);
  text('¡Bienvenido a Poredak!', width/2,height/5);
  textStyle(NORMAL);
  textSize(2*(height*width)/(17*(height+width)));
  strokeWeight(0);
  text('Tu Organizador de Horarios', width/2,2*height/7);
  textSize(2*(height*width)/(35*(height+width)));
  text('Por favor ingresa el nombre de la materia que deseas inscribir', width/8,5*height/15,6*width/8,height/7);
}

function goHome(){
  
}

function createHome(){
  home = createButton('Home');
  home.position(0, 0);
  home.size(width/15,height/16);
  home.mousePressed(setup);
}

function createBuscar(){
  buscar = createButton('Buscar');
  buscar.size(width/8,inp.height);
  buscar.position(inp.x + inp.width, 8*height/20);
}

function createInp(){
  inp = createInput();
  inp.size(5*width/8,height/35);
  inp.position(width/8,8*height/20,6*width/8,height/7)
}

function createGH(){
  gh = createButton('Generar Horario');
  gh.position(inp.x + inp.width,15*height/20);
  gh.size(buscar.size)
  gh.mousePressed(goHorarios);
}


function schedule(){
  background(255);
  stroke(0);
  strokeWeight(0.5);
  textSize((height*width)/(20*(height+width)));
  for(var i=0;i<=15;i++){
       fill(255);
       rect(0,height/16*i,width/15,height/16);
       for(var j=0; j<=6; j++){
         rect(width/15+j*2*width/15,height/16*i,2*width/15,height/16);
       }        
    }
  
  for(i=1;i<=15;i++){
      fill(0);
      textAlign(CENTER);
      textSize((height*width)/(25*(height+width)));
      text(i+5+" - "+String(i+6),0,height/16*i+height/50,width/15,height/16);
    }
    
    for(i=0;i<7;i++){
      text(dia[i],width/15+i*2*width/15,10,2*width/15,height/16);
    }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
  if(page = 'home'){
    setup();
  }
}

function goHorarios(){
  c = true;
  removeElements();
  background(255);
  page = 'horarios';
  createHome();
  c = false;
}

class Hour {
  constructor(x, y) {
    this.x = x*2*width/15;
    this.y = y*height/16;
  }
}

class Subject {
  constructor(x){
    json=loadJSONObject(x);
    test=json.getJSONArray("list");
    this.title = test.getJSONObject(0).getString("title"); //Si tan solo el título estuviera en el JSON :'v
    this.group = test.getJSONObject(0).getInt("code");
    this.master = test.getJSONObject(0).getString("master");
    this.hours = test;
    
  }
}