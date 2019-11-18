const siajs = require('siajs');
var p5 = require('p5');

function busquedaGrupos(codigo){
  siajs.getGroups(codigo).then(res => {

  }).catch(err => {
    console.log(err);
  });
}

let inp, x, deshacer, rehacer, page, buscar, gh, c, home, dia, opciones, t, salidas, cm, verm, verg, ayuda, prueba, materia, data, ayuda1, next, prev, h;
let horarioF = [];
let descartadas = [];
var busquedas = [];
var materias = [];
let horario = [];
let jsons = [];
let jsones = [];
let count = 0;
let resultados = [];
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
  this.preload = function preload(){
	  data = loadJSON('assets/data.json');
	  busquedas.push(loadJSON('assets/diferencial.json'));
	  busquedas.push(loadJSON('assets/sistemas.json'));
	  busquedas.push(loadJSON('assets/varias va.json'));
	  busquedas.push(loadJSON('assets/calculo integral.json'));
	  busquedas.push(loadJSON('assets/Dinamica.json'));
	  busquedas.push(loadJSON('assets/digital.json'));
	  busquedas.push(loadJSON('assets/grafica.json'));
	  busquedas.push(loadJSON('assets/Latín.json'));
	  busquedas.push(loadJSON('assets/sistemas ii.json'));
	  busquedas.push(loadJSON('assets/intensive.json'));
	  busquedas.push(loadJSON('assets/electivo.json'));
	  busquedas.push(loadJSON('assets/materias.json'));
	  busquedas.push(loadJSON('assets/estadistica.json'));
	  busquedas.push(loadJSON('assets/intensivo.json'));
	  busquedas.push(loadJSON('assets/Latin.json'));
	  materias.push(loadJSON('assets/9941.json'));
	  materias.push(loadJSON('assets/10680.json'));
	  materias.push(loadJSON('assets/16214.json'));
	  materias.push(loadJSON('assets/16706.json'));
	  materias.push(loadJSON('assets/16707.json'));
	  materias.push(loadJSON('assets/20580.json'));
	  materias.push(loadJSON('assets/22969.json'));
	  materias.push(loadJSON('assets/21949.json'));
	  materias.push(loadJSON('assets/18473.json'));
	  materias.push(loadJSON('assets/16809.json'));
	  materias.push(loadJSON('assets/2023238.json'));
	}
  this.setup = function setup () {
	  j = 0;
	  t = 0;
	  h = 1;
	  //changeData(h);
	  horario = [];
	  horarioF = [];
	  opciones = [];
	  salidas = [];
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
	  createGH(15*height/20);
	  createCM();
	  home.hide();
  }
  this.draw = function draw () {
	  if(page == 'home' && c == false){
	    drawHome();
	  }else if(page == 'horarios' && c == false){
	    //crearHorarioP();
	    readData(1);
	    schedule();
	    drawData();
	  }else if(page == 'cm' && c == false){
	    schedule();
	    //calificarM();
	  }
  }
})

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
  if(page == 'home'){
     setup();
  }else if (page == 'horarios'){
    goHorarios();
  }
}

//---------------------------------------------
//----------- CREATING STUFF ------------------
//---------------------------------------------

function createNext(){
  next = createButton('Siguiente');
  next.position(width-next.width,10);
  next.mouseClicked(nextH);
}

function nextH(){
  if(h<9){
    changeData(h+1);
    h++;
  }
  c = false;
  schedule();
  drawData();
}

function createPrev(){
  prev = createButton('Anterior');
  prev.position(next.x-next.width,10);
  prev.mouseClicked(prevH);
}

function prevH(){
  if(h>1){
    changeData(h-1);
    h--;
  }
  c = false;
  schedule();
  drawData();
}

function crearHorarioP(){
  if (opciones[0] != null){
    opciones.forEach(
      function(element){
        let materia = new Subject(splitTokens(element.value(),'()')[0], int(splitTokens(element.value(),'()')[1]), 1);
        horario.push(materia);
        jsons.push(materia.json);
      }  
    )
  }
  saveJSON(jsons,'noCalificados.json');
}

function createVerm(){
  let k = 1;
  verm = createSelect();
  verm.position(width/8,height/50);
  opciones.forEach(function(element){
        verm.option(k+'-'+element.value());
        k++;
      }
    )
  ayuda = new Subject( splitTokens(verm.value(),'()')[0], int(splitTokens(verm.value(),'()')[1]), 1);
  verm.changed(vermC);
}

function createVerg(){
  if(verg != null){
    verg.remove();
  }
  verg = createSelect();
  calcg = createInput();
  calcButton = createButton('Calificar');
  verg.position(verm.x+7*verm.width,height/50);
  calcg.position(verg.x+1.4*verg.width,height/50);
  calcButton.position(calcg.x+0.9*calcButton.width,height/50);
  calcButton.mousePressed(calificar);
  calcg.size(verg.width,height/35);
  calcg.value(1);
  let help = ayuda.json.count;
  for (var t = 0; t < help; t++){
    verg.option(t+1);
  }
  setM();
  verg.changed(setM);
}

function calificar(){
  jsones[ splitTokens(verm.value(),'-')[0]-1 ].C_G[verg.value()-1] = int(calcg.value());
  console.log(jsones);
}

function setM(){
  if(materia==null){
  materia = new Subject (splitTokens(verm.value(),'()')[0], int(splitTokens(verm.value(),'()')[1]), verg.value()-1);
}else{
  materia.setGroup(verg.value()-1);
}
  schedule();
  materia.display();
}

function createInp(){
 inp = createInput();
 inp.size(5*width/8,height/35);
 inp.position(width/8,6*height/20,6*width/8,height/7)
}

function createGH(y){
  gh = createButton('Generar Horario');
  gh.position(inp.x + inp.width,y);
  gh.size(buscar.size)
  gh.mousePressed(goHorarios);
}

function createHome(){
  home = createButton('Home');
  home.position(0, 0);
  home.size(width/15,height/16);
  home.mousePressed(goHome);
}

function createBuscar(){
 buscar = createButton('Buscar');
 buscar.size(width/8,inp.height);
 buscar.position(inp.x + inp.width, inp.y);
 buscar.mousePressed(busqueda);
}

function createCM(){
  cm = createButton('Calificar Cursos')
  cm.position(gh.x,gh.y-gh.height);
  cm.mousePressed(goCM);
}

function createResults(resultado){
  opciones.push(createSelect());
  resultado.list.forEach(function(element) {
    opciones[opciones.length-1].option(element.name + ' (' + element.code + ')');
    opciones[opciones.length-1].position(inp.x,inp.y+inp.height*(opciones.length));
    opciones[opciones.length-1].size(inp.width, inp.height);
  });
  if(opciones.length-1==0){
    deshacer = createButton('Deshacer');
    deshacer.mouseClicked(backward);
    deshacer.hide();
  }
  deshacer.show();
  deshacer.position(inp.x, gh.y);
  j++;
}

//---------------------------------------------
//----------- GOING SOMEWHERE -----------------
//---------------------------------------------


function goHorarios(){
  if (page=='home'){
    removeElements();
    background(255);
    c = false;
    page = 'horarios';
    createHome(); 
    createNext();
    createPrev();
  }else if(page=='cm'){
    saveJSON(jsones,'calificados.json');
  }
}


function goCM(){
  c = false;
  removeElements();
  schedule();
  page = 'cm';
  createHome();
  if(opciones[0] != null){
    createVerm();
    createVerg();
    createGH(height/50);
    materia.display();
    opciones.forEach(
      function(element){
        let materia = new Subject(splitTokens(element.value(),'()')[0], int(splitTokens(element.value(),'()')[1]), 2);
        let a = materia.json;
        jsones.push(a);
      }  
    )
  }
  c = true;
}

//Se debe cambiar esto para no borrar todo
function goHome(){
  setup();
}

//---------------------------------------------
//----------- DRAWING FUNCTIONS ---------------
//---------------------------------------------

function drawHome(){
 background(255);
 textSize(2*(height*width)/(13*(height+width)));
 textAlign(CENTER);
 strokeWeight(3);
 textStyle(BOLD);
 text('¡Bienvenido a Poredak!', width/2,height/7);
 textStyle(NORMAL);
 textSize(2*(height*width)/(17*(height+width)));
 strokeWeight(0);
 text('Tu Organizador de Horarios', width/2,2*height/9);
 textSize(2*(height*width)/(35*(height+width)));
 text('Por favor ingresa el nombre de la materia que deseas inscribir', width/8,4*height/17,6*width/8,height/7);
  c = true;
}

function schedule(){
  background(255);
  stroke(0);
  strokeWeight(0.5);
  textSize((height*width)/(20*(height+width)));
  for(var i=0;i<=15;i++){
       fill(255);
       rect(0,height/16*(i+1),width/15,height/16);
       for(var j=0; j<=6; j++){
         rect(width/15+j*2*width/15,height/16*(i+1),2*width/15,height/16);
       }        
    }
  
  for(i=1;i<=15;i++){
      fill(0);
      textAlign(CENTER);
      textSize((height*width)/(25*(height+width)));
      text(i+5+" - "+String(i+6),0,height/16*(i+1)+height/50,width/15,height/16);
    }
    
  for(i=0;i<7;i++){
      text(dia[i],width/15+i*2*width/15,10+1*height/16,2*width/15,height/16);
  }
  for(var t = 0; t < horario.length; t++){
    horario[t].display();
  }
  c = true;
  //ayuda.display();
}

function calificarM(){
  //schedule();
  //home.show();
  /*
  verm = createSelect();
  verm.position(width/7,height/50);
  createVerg();
  ayuda = new Subject('Diferencial', 16706, 1);
  ayuda.display();
  if(opciones != null){
    opciones.forEach(
      function(element){
        verm.option(element.value());
      }
    )
    ayuda = new Subject(splitTokens(verm.value(),'()')[0], int(splitTokens(verm.value(),'()')[1]), 1);
    let help = ayuda.json.count;
    for (var t = 0; t < help; t++){
      verg.option(t+1);
    }
    print(verg.value());
    ayuda.setGroup(verg.value());
    ayuda.display();
  }*/
  
}

function drawData(){
  for(var i = 0; i < horarioF.length; i++){
    horarioF[i].display();
  }  
}

//---------------------------------------------
//----------- OTHER STUFF ------------------
//---------------------------------------------

function readData(x){
  for(var i = 0; i < 5; i++){
    let y = new Subject(data[x][1].asignaturas[i], data[x][1].codigos[i], data[x][1].grupos[i]);
    horarioF.push(y);
  }
}

function changeData(x){
  for(var i = 0; i < horarioF.length; i++){
    horarioF[i].setGroup(data[x][1].grupos[i]);
  }
}

function vermC(){
  ayuda = new Subject( splitTokens(verm.value(),'()')[0], int(splitTokens(verm.value(),'()')[1]), 1);
  createVerg();
}

function probando(){
  ayuda = new Subject('Diferencial', 16706, 5);
  ayuda.setGroup(5);
  ayuda.display();
  //c = true;
}

function removeItemFromArr( arr, item ) {
    return arr.filter( function( e ) {
        return e !== item;
    } );
}

function backward(){
    if(descartadas.length==0){
      rehacer = createButton('Rehacer');
      rehacer.position(inp.x+deshacer.width, gh.y);
      rehacer.mousePressed(forward);
    }
    descartadas.push(opciones[opciones.length-1]);  
    opciones.pop().hide();
    if (opciones.length==0){
      this.remove();  
    }   
}

function forward(){
    opciones.push(descartadas[descartadas.length-1]);
    descartadas[descartadas.length-1].show();
    descartadas = removeItemFromArr(descartadas,descartadas[descartadas.length-1]);
    if (descartadas.length==0){
      this.remove();  
    }
}

function busqueda(){
  const palabra = inp.value();
  switch (palabra){
    case 'diferencial':
      createResults(busquedas[0]);
      break;
    case 'sistemas':
      createResults(busquedas[1]);
      break;
    case 'varias va':
      createResults(busquedas[2]);
      break;
    case 'calculo integral':
      createResults(busquedas[3]);
      break;
    case 'Dinamica':
      createResults(busquedas[4]);
      break;
    case 'digital':
      createResults(busquedas[5]);
      break;
    case 'grafica':
      createResults(busquedas[6]);
      break;
    case 'Latín':
      createResults(busquedas[7]);
      break;
    case 'sistemas ii':
      createResults(busquedas[8]);
      break;
    case 'intensive':
      createResults(busquedas[9]);
      break;
    case 'electivo':
      createResults(busquedas[10]);
      break;
    case 'materias':
      createResults(busquedas[11]);
      break;
    case 'estadistica':
      createResults(busquedas[12]);
      break;
    case 'intensivo':
      createResults(busquedas[13]);
      break;
    case 'Latin':
      createResults(busquedas[14]);
      break;
  }
}

//---------------------------------------------
//--------------- CLASSES----------------------
//---------------------------------------------

class Hour {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.time = createVector(width/15+x*2*width/15,height/16*(y+2));
  }

  getTime(){
    return this.time;
  }

  display(){
    fill(240);
    stroke(0);
    strokeWeight(0);
    rect(this.time.x,this.time.y,2*width/15,height/16);
  }
}

class Subject {
  constructor(tempTitle, x, code){
    this.setJSON(x);
    this.materia = tempTitle;
    this.test = this.json.list;
    this.json.materia = tempTitle;
    this.json.code = x;
    this.code = x;
    this.setGroup(code);
    this.json.C_M = 1;
    this.setCG();
  }
  
  setGroup(codigo){
    this.group = codigo;
    this.setMaster();
    this.setWeek();
    this.setHours();
  }
  
  getGroup(){
    return this.group+1;
  }
  
  setMaster(){
    this.master = this.test[this.group].master;
  }
  
  setWeek(){
    this.week = this.test[this.group].week;
  }
  
  setJSON(x){
    switch (x){
      case 9941:
        this.json = materias[0];
        break;
      case 10680:
        this.json = materias[1];
        break;
      case 16214:
        this.json = materias[2];
        break;
      case 16706:
        this.json = materias[3];
        break;
      case 16707:
        this.json = materias[4];
        break;
      case 20580:
        this.json = materias[5];
        break;
      case 22969:
        this.json = materias[6];
        break;
      case 21949:
        this.json = materias[7];
        break;
      case 18473:
        this.json = materias[8];
        break;
      case 16809:
        this.json = materias[9];
        break;
      case 2023238:
        this.json = materias[10];
        break;
    }
  }
  
  setCG(){
    this.json.C_G = [];
    for(let i = 0;i<this.json.count;i++){
      this.json.C_G.push(1);
    }
  }

  countClasses(){
    let c = [];
    for(let i = 0; i < 7; i++){
      c[i] = this.week[i].length;
      if(c[i] == 1 && this.week[i][0][0] == '-'){
        c[i]=0;
      }
    }
    return c;
  }

  setHours(){
    let tempHours = [];
    let ap=0;
    let c = this.countClasses();
    for(let i = 0; i < 7; i++){
      if(c[i] != 0){
        let y = int(this.week[i][0])-6;
        let x1 = new Hour(i,y);
        tempHours.push(x1);
        let x2 = new Hour(i,y+1);
        tempHours.push(x2);
      }
    }
    this.hours = tempHours;
  }

  display(){
    for(let i = 0; i < this.hours.length; i++){
      this.hours[i].display();
      fill(0);
      strokeWeight(0.5);
      textSize(1*(height*width)/(35*(height+width)));
      text(this.materia, this.hours[i].getTime().x + 2, this.hours[i].getTime().y + 2, 2*width/15, height/(16*2));
      textSize((height*width)/(35*1.2*(height+width)));
      text(this.master, this.hours[i].getTime().x + 2, this.hours[i].getTime().y + 4*height/(169), 2*width/15, 3*height/(169));
      text(this.code + " - " + (this.group+1), this.hours[i].getTime().x + 2, this.hours[i].getTime().y+7*height/(169), 2*width/15, height/16);
    }
  }

}