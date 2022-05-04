<h1>ENGI301</h1>
Repository for ENGI301 course work
<h3>Project 1</h3>
The project_1 folder contains the code for the PocketBeagle Medication Dispenser, found on my Hackster: https://www.hackster.io/sarajbarker/pocketbeagle-medication-dispenser-ca1f8f </br> </br>
All of the hardware can be found on the Hackster page. For the code, the only file needed is <a href=https://github.com/saraJbarker/ENGI301/blob/main/project_1/main_code3.py"">main_code3.py</a>. 
To set up and run this code: </br>
<ol>
  <li> Wire everything up according to the directions on Hackster (also see <a href="https://github.com/saraJbarker/ENGI301/blob/main/project_1/sketch_bb.png"> sketch_bb.png</a> for a Fritzing diagram) </li>
  <li> Connect the PocketBeagle to the internet </li>
  <li> Set up the PocketBeagle to run Python: 
    <ul>
      <li><code>sudo apt-get update </code></li>
      <li><code>sudo apt-get install build-essential python-dev python-setuptools python-smbus -y </code></li>
      <li><code>sudo apt-get install python-pip python3-pip -y</code></li>
    </ul>
  <li>Install Adafruit BBIO:
    <ul><code>sudo pip3 install --upgrade Adafruit_BBIO</code></ul>
    </li>
  <li>Drag and drop <a href=https://github.com/saraJbarker/ENGI301/blob/main/project_1/main_code3.py>main_code3.py</a> into your PocketBeagle directory.</li>
  <li>Press "Run".</li>
  </ol>
  </br>
  Included in the Project 1 folder are the STL and Solidworks files for the pillbox - the STL can go into a 3D printing software like 3DprinterOS, or you can modify the Solidworks file and make a new STL file. <a href="https://github.com/saraJbarker/ENGI301/blob/main/project_1/boxv3all.ai">boxv3all.ai</a> is the Illustrator file for the sides of the wooden box. This can be used with a laser cutter to cut the wood out. <a href="https://github.com/saraJbarker/ENGI301/blob/main/project_1/sketch_bb.png">sketch_bb.png</a> is a picture of the Fritzing file. <code>code_skeleton</code>, <code>main_code.py</code>, and <code>main_code2.py</code> are just in progress versions of the currently updated code, <code>main_code3.py</code> - there isn't a need to download these.
  <h3>Project 2</h3>
  The project_2 folder contains files for a PCB that would control the medication dispenser described in Project 1. The library, schematic, and board files in EAGLE are included in the EAGLE subfolder, and there is also a PDF version of the schematic and a Bill of Materials. 




