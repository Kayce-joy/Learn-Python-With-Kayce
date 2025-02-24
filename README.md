Setting Up Python on Linux and Windows: Step-by-Step
Guide
1. Install Python
   On Windows
      ● Download Python
○ Visit python.org and download the Windows installer.
○ Choose the appropriate version (32-bit or 64-bit) based on your
system.
      ● Install Python
○ Run the installer.
○ Check the box "Add Python to PATH" to make Python accessible
from the Command Prompt.
○ Choose Customize Installation for optional features like pip, IDLE,
and development tools.
○ Complete the installation process.
      ● Verify Installation
○ Open Command Prompt.
Run:
python --version
pip --version


    On Linux
Update System Packages
sudo apt update && sudo apt upgrade -y # For Debian/Ubuntu
       ● Install Python
For Debian/Ubuntu:
sudo apt install python3 python3-pip -y
For Red Hat/CentOS:
sudo yum install python3 python3-pip -y
       ●Verify Installation
python3 --version
pip3 --version





2. Choose an Editor
Recommended Editors for Both Linux and Windows
● VS Code (Visual Studio Code)
○ Download from code.visualstudio.com.
○ Install the Python Extension for debugging, syntax highlighting, and
more.
Command to install on Linux (Debian/Ubuntu):
sudo apt install code

● PyCharm
○ Download from jetbrains.com/pycharm.
○ Offers a free Community Edition.

● Jupyter Notebook
Install via pip:
pip install notebook
Launch:
jupyter notebook



3. Verify Python and Pip Installation
     On Windows
Open Command Prompt and run:
python --version
pip --version

     On Linux
Open a terminal and run:
python3 --version
pip3 --version



4. Set Up Virtual Environments (Optional but
Recommended)
     On Windows
Create a virtual environment:
python -m venv myenv
Activate the environment:
myenv\Scripts\activate
Deactivate with:
deactivate

     On Linux
Create a virtual environment:
python3 -m venv myenv
Activate the environment:
source myenv/bin/activate
Deactivate with:
deactivate



5. Install Essential Libraries
Use pip to install Python libraries.
Example Commands

     Install libraries:
pip install numpy pandas matplotlib
     Upgrade pip:
python -m pip install --upgrade pip # Windows
python3 -m pip install --upgrade pip # Linux


Script Mode: Save a file as script.py and run it with:
python script.py 