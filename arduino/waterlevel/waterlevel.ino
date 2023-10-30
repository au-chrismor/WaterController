#include <WiFi.h>
#include <HTTPClient.h>

void setup() {
  Serial.begin(115200)
}

void loop() {
}

void HEC(){
  HTTPClient http;    //Declare object of class HTTPClient
  temp=DHT 
  http.begin("http://<YourIPAddress/URL>:8088/services/collector");      //Specify request destination
  http.addHeader("Content-Type", "text/plain");  //Specify content-type header
  http.addHeader("Authorization", "Splunk xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx");
  String post="{\"event\":{\"Temperature\":"+String(t)+",\"Humidity\":"+String(h)+"}}";
  Serial.println(post);
  int httpCode = http.POST(post);   //Send the request
  String payload = http.getString();                  //Get the response payload

  Serial.println(httpCode);   //Print HTTP return code
  Serial.println(payload);    //Print request response payload

  http.end();  //Close connection
}
