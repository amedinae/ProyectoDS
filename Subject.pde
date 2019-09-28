class Subject{
    String title, master;
    int group, code;
    Hour[] hours;
    
    Subject(String tempTitle, String tempMaster, int tempCode, int tempGroup, Hour[] tempHours){
        setTitle(tempTitle);
        setMaster(tempMaster);
        setCode(tempCode);
        setGroup(tempGroup);
        setHours(tempHours);
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
    
}    
