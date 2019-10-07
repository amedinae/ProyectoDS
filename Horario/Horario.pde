JSONObject json, json1; 
JSONArray test, test1;
int master;
String materia;
Subject estructuras, prueba, prueba1;
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
    size(900,650);
    background(255,255,255);
    textAlign(CENTER);
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
    
    Hour[] cheat=new Hour[2];
    cheat[0]=new Hour(0,13);
    cheat[1]=new Hour(0,14);
    
    //prueba=new Subject("Prueba",test.getJSONObject(0).getString("master"),2015666,4,cheat);
    prueba=new Subject("Prueba",test.getJSONObject(0).getString("master"),2015666,4,test);
    prueba1=new Subject("Prueba",test1.getJSONObject(0).getString("master"),2015666,4,test1);
    
    Hour[] estr=new Hour[2];
    estr[0]=new Hour(3,1);
    estr[1]=new Hour(3,2);
    estructuras=new Subject("Estructuras","Luis Niño",2016699,4,estr);
}


void draw(){
   
  
  estructuras.display();
  prueba.display();
  prueba1.display();
    
    
}




    
