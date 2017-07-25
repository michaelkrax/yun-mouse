#include "Mouse.h"

void setup() {
    delay(90000); // wait until linux side finishes to boot
    Serial1.begin(115200);
}

void loop() {
    if (Serial1.available() >= 2) {   
        char command = Serial1.read();
        char value = Serial1.read();
     
        switch (command) {
            case 'X': Mouse.move(value, 0, 0);  break;
            case 'Y': Mouse.move(0, value, 0);  break;
            case 'W': Mouse.move(0, 0, value);  break;            
            case 'L':  
                if(value ==1){ Mouse.press(MOUSE_LEFT);   } else { Mouse.release(MOUSE_LEFT); }
                break;   
            case 'M':  
                if(value ==1){ Mouse.press(MOUSE_MIDDLE); } else { Mouse.release(MOUSE_MIDDLE); }
                break;   
            case 'R':  
                if(value ==1){ Mouse.press(MOUSE_RIGHT);  } else { Mouse.release(MOUSE_RIGHT); }
                break;   
        }
    }
}
