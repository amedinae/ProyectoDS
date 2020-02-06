class Hour{
    PVector time;
    //x va desde 0 a 6, son los días de la semana
    //y va desde 0 a 15, horas desde las 6am hasta las 9pm
        
    Hour(int x, int y){
        float a=100*x+50;
        float b=40*y;
        time=new PVector(a,b);
    }
    
    //Setters
    void setX(int x){
        time.set(x*100+50,time.y);
    }
    void setY(int y){
        time.set(time.x,y*40);
    }
    
    //Getters
    int getX(){
        return int(time.x-50)/100;    
    }
    int getY(){
        return int(time.y)/40;
    }
    PVector getTime(){
        return time;
    }
    //Otros métodos
    void display(){
        fill(255);
        rect(time.x,time.y,100,40);
    }
    
    
}
