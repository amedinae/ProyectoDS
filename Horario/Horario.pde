JSONObject json, json1; 
JSONArray test, test1;
int master;
String materia;
Subject estructuras, prueba, prueba1, estructuras1;
//No es posible para materias que duren 3 horas, tengan cuidado
/*int[] indexH(JSONArray week){
      int[] contador=new int[7];
      
      for(int i=0; i<7; i++){
        if(week.getString(i)!="--"){
          contador[i]++;
        }
      }
      return contador;
    }


  int[] indexH(JSONArray week){
      int[] contador=new int[7];
      for(int i=0; i<7; i++){
        contador[i]=week.getJSONObject(0).getJSONArray("week").getJSONArray(i).getString(0).indexOf('-');
      }
      return contador;
   }
   int contar(int[] idx){
      int contador=0;
      for(int i=0; i<idx.length; i++){
        if (idx[i]!=0)
          contador++;
      }
      return contador;
    }*/

void setup()
{
    size(751,641);
    background(255,255,255);
    //textAlign(CENTER);
    textSize(15);
    json=loadJSONObject("22969.json");
    test=json.getJSONArray("list");
    json1=loadJSONObject("18473.json");
    test1=json1.getJSONArray("list");
    //println(contar(indexH(test)));
    //println(test1.getJSONObject(0).getJSONArray("week"));
    //println(test.getJSONObject(0).getJSONArray("week").getJSONArray(0).getString(0));
    //println(test.getJSONObject(0).getJSONArray("week").getJSONArray(1).getString(0)==test.getJSONObject(0).getJSONArray("week").getJSONArray(2).getString(0));
    //println(test1.getJSONObject(0).getJSONArray("week").getJSONArray(0).getString(0).indexOf('-'));
    //println(test1.getJSONObject(0).getJSONArray("week").getJSONArray(0).getString(0));
    //println(test1.getJSONObject(0).getJSONArray("week").getJSONArray(0).getString(0).substring(0,1));
    //println(test.getJSONObject(0).getJSONArray("week").getJSONArray(3).getString(0));
    //println(test.getJSONObject(0).getJSONArray("week").getJSONArray(4).getString(0));
    //println(test.getJSONObject(0).getJSONArray("week").getJSONArray(5).getString(0));
    //println(test.getJSONObject(0).getJSONArray("week").getJSONArray(6).getString(0));
    //println(Integer.valueOf(test.getJSONObject(0).getJSONArray("week").getJSONArray(0).getString(0).substring(0,2))/2);
    
    for(int i=0;i<=15;i++){
       fill(255);
       rect(0,40*i,50,40);
       for(int j=0; j<=6; j++){
         rect(50+100*j,40*i,100,40);
       }        
    }
    for(int i=1;i<=15;i++){
      fill(0);
      textAlign(CENTER);
      text(Integer.toString(i+5),0,40*i+10,50,40);
    }
    String[] dia={"Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"};
    for(int i=0;i<7;i++){
      text(dia[i],50+100*i,10,100,40);
    }
    
    
    
    
    
    
    Hour[] cheat=new Hour[2];
    cheat[0]=new Hour(0,13);
    cheat[1]=new Hour(0,14);
    
    //prueba=new Subject("Prueba",test.getJSONObject(0).getString("master"),2015666,4,cheat);
    prueba=new Subject("Cátedra manuel",test.getJSONObject(0).getString("master"),2015666,4,test);
    prueba1=new Subject("Señales II",test1.getJSONObject(0).getString("master"),2015970,1,test1);
    
    Hour[] estr=new Hour[4];
    estr[0]=new Hour(3,4);
    estr[1]=new Hour(3,5);
    estr[2]=new Hour(1,4);
    estr[3]=new Hour(1,5);
    estructuras=new Subject("Estructuras de datos","LUIS FERNANDO NIÑO",2016699,2,estr);
    
    Hour[] estr1=new Hour[4];
    estr1[0]=new Hour(0,4);
    estr1[1]=new Hour(0,5);
    estr1[2]=new Hour(2,4);
    estr1[3]=new Hour(2,5);
    estructuras1=new Subject("Métodos Numéricos","SANDRA LILIANA ROJAS MARTINEZ",2015970,2,estr1);

    Hour[] estr2=new Hour[6];
    estr2[0]=new Hour(1,6);
    estr2[1]=new Hour(1,7);
    estr2[2]=new Hour(3,6);
    estr2[3]=new Hour(3,7);
    estr2[4]=new Hour(4,6);
    estr2[5]=new Hour(4,7);
    estructuras1=new Subject("Procesos de Manufactura I","EDGAR ESPEJO MORA",2017273,2,estr2);


}


void draw(){
   
  
  estructuras.display();
  estructuras1.display();
  prueba.display();
  prueba1.display();
    
    
}




    
