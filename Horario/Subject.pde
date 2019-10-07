class Subject{
    String title, master;
    int group, code;
    Hour[] hours;
    
    Subject(String tempTitle, String tempMaster, int tempCode, int tempGroup, JSONArray tempWeek){
        setTitle(tempTitle);
        setMaster(tempMaster);
        setCode(tempCode);
        setGroup(tempGroup);
        setHours(tempWeek);
    }    
    
    Subject(String tempTitle, String tempMaster, int tempCode, int tempGroup, Hour[] tempHours){
        setTitle(tempTitle);
        setMaster(tempMaster);
        setCode(tempCode);
        setGroup(tempGroup);
        setHours(tempHours);
    }
    
    Subject(String x){
        JSONObject json=loadJSONObject(x);
        JSONArray test=json.getJSONArray("list");
        //Es necesario corregir que se escriba el título adecuado
        setTitle(x);
        setMaster(test.getJSONObject(0).getString("master"));
        setGroup(test.getJSONObject(0).getInt("code"));
        setHours(test);
        //Corregir también obtención código
        setCode(000000);
    }
    
    //Setters
    void setTitle(String tempTitle){
        title=tempTitle;
    }
    
    void setMaster(String tempMaster){
        master=tempMaster;
    }
    
    void setGroup(int tempGroup){
        group=tempGroup;
    }
    
    void setCode(int tempCode){
        code=tempCode;
    }
    
    void setHours(Hour[] tempHours){
        int size=tempHours.length;
        hours=new Hour[size];
        for(int i=0; i<size; i++){
            hours[i]=tempHours[i];
        }
    }
   
    //Getters
    String getTitle(){
        return title;
    }
    
    String getMaster(){
        return master;
    }
    
    int getGroup(){
        return group;
    }
    
    int getCode(){
        return code;
    }
    
    Hour[] getHours(){
        return hours;
    }
    //Other methods
    void display(){
      //println(hours.length);
        for(int i=0; i<hours.length; i++){
            fill(255);
            hours[i].display();
            fill(0);
            textSize(15);
            text(title,hours[i].getTime().x+50,hours[i].getTime().y+15);
            textSize(10);
            text(master,hours[i].getTime().x+50,hours[i].getTime().y+25);
            text(code+" - "+group,hours[i].getTime().x+50,hours[i].getTime().y+35);
        }
        
    }
    
    //Integer.valueOf(test.getJSONObject(0).getJSONArray("week").getJSONArray(0).getString(0).substring(0,2));
    
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
    }
    
    
    void setHours(JSONArray week){
      int[] tempIndx=indexH(week);
      Hour[] tempHours=new Hour[2*contar(tempIndx)];
      int ap=0;
      int y=0;
      println(tempIndx);
      for(int i=0; i<7; i++){
        if(tempIndx[i]!=0){
          println(week.getJSONObject(0).getJSONArray("week").getJSONArray(i).getString(0).substring(0,tempIndx[i]));
          y=Integer.valueOf(week.getJSONObject(0).getJSONArray("week").getJSONArray(0).getString(0).substring(0,tempIndx[i]))-6;
          println("y="+y);
          tempHours[ap]=new Hour(i,y);
          ap++;
          y++;
          tempHours[ap]=new Hour(i,y);
          ap++;
        }
          
      }
      setHours(tempHours);
      
    }
    
}    
