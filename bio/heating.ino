#include <math.h>

void heating(){
    adjustHeating();
}

void outputT(){
    currentT = convertTemperature(analogRead(INPIN));
    Serial.print("CTEM");
    Serial.println(currentT);
}

// to convert the temperature Steinhart- Hart- Thermistor Equation has been used below
// the equation:  1 / {A + B[ln(R)] + C[ln(R)]^3} where A,B and C are constants
// function to convert the temperature from analog(raw) form to celsius
float convertTemperature(int rawADC){
    float Tempo; // temporary variable
    Tempo = logf((10240000/(rawADC - 10)) - 10000); // Modify the input value to calibrate the temperature
    // for 10k thermistor:
    // A = 0.001125308852122, B = 0.000234711863267, C = 0.000000085663516
    //the step below gives the temperature in Kelvins;
    Tempo = 1 / (0.001125308852122 + (0.000234711863267 * Tempo) + (0.000000085663516 * Tempo * Tempo * Tempo));
    return Tempo - 273.15;//subtract 273.15 to get into Celsius
}

void adjustHeating(){
    if (currentT < expectedT - 0.4){
        digitalWrite(OUTPIN, HIGH);
    }else{
        digitalWrite(OUTPIN, LOW);
    }
}