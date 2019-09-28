void setup()
{
    size(640,650);
    background(255,255,255);
    textAlign(CENTER);
    textSize(15);
}


void draw(){
    
    /*Hour[] monday=new Hour[15];
    for(int i=0; i<16; i++){
        monday[i]=new Hour(0,i);
        monday[i].display();    
    }*/
    Hour[] tuesday=new Hour[15];
    for(int i=0; i<15; i++){
        tuesday[i]=new Hour(1,i);
        tuesday[i].display();    
    }
    
    Hour[] digital=new Hour[2];
    digital[0]=new Hour(3,1);
    digital[1]=new Hour(3,2);
    fill(255);
    digital[0].display();
    digital[1].display();
    fill(0);
    print(digital[0].getTime());
    fill(0);
    textSize(15);
    text("Digital",digital[0].getTime().x+50,digital[0].getTime().y+15);
    textSize(10);
    text("Henrry Moreno",digital[0].getTime().x+50,digital[0].getTime().y+25);
    text("2016498 - 1",digital[0].getTime().x+50,digital[0].getTime().y+35);
    
    Hour[] estr=new Hour[2];
    estr[0]=new Hour(3,3);
    estr[1]=new Hour(3,4);
    
    Subject estructuras=new Subject("Estructuras","Luis Niño",2016699,4,estr);
    estructuras.display();
    
    
}




    
