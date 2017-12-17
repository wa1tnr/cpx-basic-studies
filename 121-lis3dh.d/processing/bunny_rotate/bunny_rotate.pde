// Sun Dec 17 09:29:32 UTC 2017

// Seems to be about the best one can do with this kind of a Z axis. - 09:29:32 UTC on Sun 17 Dec 2017.

// Processing 2.2.1

// chair.obj is similar to rocket.obj from the Processing Examples > Shape > LoadDisplayOBJ

// bunny.obj is an Adafruit thing.

// All three files were required in the rocket variant of this sketch:
// processing-2.2.1/modes/java/examples/Basics/Shape/LoadDisplayOBJ/data/rocket.mtl
// processing-2.2.1/modes/java/examples/Basics/Shape/LoadDisplayOBJ/data/rocket.png
// processing-2.2.1/modes/java/examples/Basics/Shape/LoadDisplayOBJ/data/rocket.obj

// old instrux read: place copies of them in the same directory as this simple_rotate.pde program file.

// The CircuitPython code running on the CPX is exactly the same as
// the simple_rotate sketch for Processing.  17 Dec 02:25 UTC  << still true

import processing.serial.*;
import java.awt.datatransfer.*;
import java.awt.Toolkit;
import processing.opengl.*;
import saito.objloader.*;
import g4p_controls.*;


// PShape bunny;
float ry;

float roll  = 0.0F;
float pitch = 0.0F;
float yaw   = 0.0F;
float temp  = 0.0F;
float alt   = 0.0F;

OBJModel model;

// Serial port state.
Serial       port;
final String serialConfigFile = "serialconfig.txt";
// boolean      printSerial = false;
boolean      printSerial = true;
// UI controls.
GPanel    configPanel;
GDropList serialList;
GLabel    serialLabel;
GLabel    calLabel;
GCheckbox printSerialCheckbox;

public void setup()
{
//  size(640, 480, OPENGL);
  size((1920-80), (1080-80), P3D);
  frameRate(30);
  model = new OBJModel(this);
  model.load("bunny.obj");
  model.scale(34);


  // bunny = loadShape("bunny.obj");
  

// 30   size(640, 480, OPENGL);
// 31   frameRate(30);
// 32   model = new OBJModel(this);
// 33   model.load("bunny.obj");
// 34   model.scale(20);





  // Serial port setup.
  // Grab list of serial ports and choose one that was persisted earlier or default to the first port.
  int selectedPort = 0;
  String[] availablePorts = Serial.list();
  if (availablePorts == null) {
    println("ERROR: No serial ports available!");
    exit();
  }
  String[] serialConfig = loadStrings(serialConfigFile);
  if (serialConfig != null && serialConfig.length > 0) {
    String savedPort = serialConfig[0];
    // Check if saved port is in available ports.
    for (int i = 0; i < availablePorts.length; ++i) {
      if (availablePorts[i].equals(savedPort)) {
        selectedPort = i;
      } 
    }
  }
  // Build serial config UI.
configPanel = new GPanel(this, 10, 10, width-20, 90, "Configuration (click to hide/show)");
serialLabel = new GLabel(this,  0, 20, 80, 25, "Serial port:");
configPanel.addControl(serialLabel);
serialList = new GDropList(this, 90, 20, 200, 200, 6);
serialList.setItems(availablePorts, selectedPort);
configPanel.addControl(serialList);
calLabel = new GLabel(this, 300, 20, 350, 25, "Calibration: Sys=? Gyro=? Accel=? Mag=?");
configPanel.addControl(calLabel); 
printSerialCheckbox = new GCheckbox(this, 5, 50, 200, 20, "Print serial data");
printSerialCheckbox.setSelected(printSerial);
configPanel.addControl(printSerialCheckbox);
  // Set serial port.
setSerialPort(serialList.getSelectedText());
}
 
void draw()
{
  background(33, 74, 101);
  // background(55, 55, 55);
  lights();

  // Simple 3 point lighting for dramatic effect.
  // Slightly red light in upper right, slightly blue light in upper left, and white light from behind.
       pointLight(255, 200, 200,  400, 400,  500);
       pointLight(200, 200, 255, -400, 400,  500);
       pointLight(255, 255, 255,    0,   0, -500);
  
  // Move bunny from 0,0 in upper left corner to roughly center of screen.

  // BEST chair: translate(960, 490, 410);  // establishes observing camera's location

  // translate(960, 540, 610);  // establishes observing camera's location
  
  // ------------------------------------------
  // translate(701, 501, 601);
  
  translate(900, 600, 200);
  
  //  --------------------------------------------
  // n3 seems related to how close to the object the camera is.
  // n1 and n2 seem related to x and y offset from a directly-behind perspective.

  // Rotate shapes around the X/Y/Z axis (values in radians, 0..Pi*2)
  // rotateZ(radians(roll));
  // z yaw  x pitch  y roll
  // x yaw  z pitch  y roll
  // y yaw  z pitch  x roll
  // z yaw  y pitch  x roll
  

  // rotateZ(yaw * .04);  // if any Z use this for now.

  //  rotateZ(1.2);  // odd result for chair
  //  rotateZ(3.17); // chair flipped upside down, with other effects, perhaps
 
  // - ----------------------------------------------
   // reenable 17 dec 0729z:
      // Don't know what to do about this axis.

   // PROBLEMATIC AXIS

   //  rotateY(1*((yaw * 3.1415)+3.1415));
     // that's about it for now. 17 Dec 08:29z.

   // re-enable the above for a single-axis lagomorph.
   
   // neutered with a multiplier of 0.0001 to dull the effect considerably:
   
  //   rotateY(0.0001*(1*((yaw * 3.1415)+3.1415)));


  // - ----------------------------------------------
  // pre-chair (for rocket):
  // rotateX((-1* (1.6 * pitch)+(3+1.6) ));  // 1.6 makes for 90 degrees roughly


  // BEST rotateX((-1* (1.6 * pitch)+(2.9+1.6) ));  // 1.6 makes for 90 degrees roughly
   
   
   // - ---------------------------------------------------------------
   // reenable 17 dec 0729z:  
   // CERTIFIED SINGLE AXIS
   // good if statement against yaw.  Commented out for simplification 17 Dec Sun 09:13z
   if (yaw > 0) { // was > previous several iterations.  17 Dec 09:23z
      rotateX((-1* (1.6 * pitch)+(0.01) ));  // 1.57 makes for 90 degrees roughly
   } else { // flip it
      // this was commented-out in the singleton version:
      rotateX((1* (1.6 * pitch)+(3.1415) ));  // 1.57 makes for 90 degrees roughly
   }
   // his left ear and his face are directed our way.  His head is to the left.
   // he faces us.

   // - ---------------------------------------------------------------
// 31415
// 1520500
// 0050025
// 1570525

  // rotateX(3*1.6);

  // nice for chair:
  // BEST:   rotateY((-1* (0.53 * (3.2 *  roll))+(1.55+1.6) ));


  // - ------------------------------------------------------
  // Now it rolls properly.  Maybe.  Rolls like an airplane, anyway.
  // reenable 17 Dec 07:46z:
  // CERTIFIED SINGLE AXIS
       // this is pitch in the real world:



// new trial on if/yaw stuff 17 Dec 09:17z to see if other axis can do this as well.

// YES IT CAN.  09:21z 17 Dec.  Probably not in tandem with the other, though.

  // CLEAN // if (yaw > 0)
  // CLEAN // {
      rotateZ((1* (1.6 * roll)+(0.01) ));  // 1.57 makes for 90 degrees roughly
  // CLEAN //  } else {
  // CLEAN //  singleton //    rotateZ((-1* (1.6 * roll)+(3.1415) ));  // 1.57 makes for 90 degrees roughly
  // CLEAN //  }


  // - ---------------------------------------------------------

  // rotateX(radians(pitch)); // extrinsic rotation
  // rotateY(radians(yaw));
//  float c1 = cos(radians(roll));
//  float s1 = sin(radians(roll));
//  float c2 = cos(radians(pitch)); // intrinsic rotation
//  float s2 = sin(radians(pitch));
//  float c3 = cos(radians(yaw));
//  float s3 = sin(radians(yaw));
//  applyMatrix( c2*c3, s1*s3+c1*c3*s2, c3*s1*s2-c1*s3, 0,
//               -s2, c1*c2, c2*s1, 0,
//               c2*s3, c1*s2*s3-c3*s1, c1*c3+s1*s2*s3, 0,
//               0, 0, 0, 1);

//  pushMatrix();
//  noStroke();
    model.draw();
//  popMatrix();
//  popMatrix();
  //print("draw");

// This statement controls point of view to some extent.
// Rocket is slightly off-axis in neutral view.  Perhaps
// this 'shape' statement can correct for that.

//  shape(rocket, 100, 100, 80, 380);

//                 n1   n2  n3   n4


// BEST chair:   shape(chair, 15, 15, 190, 400);  // n4 is length related

//  shape(chair, 55, -55, 40, 50);  // n4 is length related

// said bunny not model here
//    shape(model, 10, 10, 80, 80);

//  shape(rocket);

//  shape(rocket, 100, 100, 80, -460);
}


void serialEvent(Serial p) 
{
  String incoming = p.readString();
  if (printSerial) {
    println(incoming);
  }
  
  if ((incoming.length() > 8))
  {
    String[] list = split(incoming, " ");
    if ( (list.length > 0) && (list[0].equals("Orientation:")) ) 
    {
      // incoming: pitch, roll, yaw: x, y and z.
      yaw   = float(list[3]); // Roll = Z
      roll  = float(list[2]); // Pitch = Y 
      pitch = float(list[1]); // Yaw/Heading = X
    }
  }
}

// Set serial port to desired value.
void setSerialPort(String portName) {
  // Close the port if it's currently open.
  if (port != null) {
    port.stop();
  }
  try {
    // Open port.
    port = new Serial(this, portName, 115200);
    port.bufferUntil('\n');
    // Persist port in configuration.
    saveStrings(serialConfigFile, new String[] { portName });
  }
  catch (RuntimeException ex) {
    // Swallow error if port can't be opened, keep port closed.
    port = null; 
  }
}

// flarg argon
