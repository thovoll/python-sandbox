# Python Intro

## Python Toolchain

### Anaconda, Conda, and Miniconda

Anaconda is a free, open source, high-performance and optimized Python and R distribution. Anaconda includes Python and 100+ automatically installed, open source scientific packages and their dependencies that have been tested to work well together, including SciPy, NumPy and many others. It also includes Conda.

Conda is a Python package and environment manager that installs and updates Python, Python packages, and their dependencies. Conda also lets you easily switch between conda environments on your local computer, including switching Python versions. 

Miniconda is a small bootstrap version of Anaconda that includes only conda, Python, the packages they depend on and a small number of other useful packages, including pip, zlib and a few others.

Install the 64-bit Windows version for Python 3.6 from here: https://conda.io/miniconda.html. Accept the default selections during installation. 

Miniconda will be installed here: `C:\Users\<you>\AppData\Local\Continuum\miniconda3`

### Visual Studio Code

VS Code can be used for working on Python projects. It's free, lighweight, and supports conda environments. It also has auto-complete, IntelliSense, linting, debugging, unit testing, and basic refactoring. 

Install VS Code from here: https://code.visualstudio.com/docs/setup/windows

These extensions are useful for Python development:

- "Anaconda Extension Pack" (also installs "YAML Support by Red Hat")
- "Python"

Install extensions by clicking on the extensions icon in the left navigation sidebar or by entering command mode via Ctrl+Shift+P and typing "Extensions: Install Extensions" (it will auto-complete), followed by hitting Enter. Then search for extensions and click "Install". You might have to "Reload" as well.

### PyCharm

PyCharm can be used for working on Python projects. It has a free version ("Community") and a paid version ("Professional") and supports conda environments. It's more heavyweight than VS Code but has more advanced code navigation and refactoring support. The paid version also has advanced support for data science work, a Python profiler, and much more. 

Install PyCharm from here: https://www.jetbrains.com/pycharm/download

## Python Ecosystem

Python is the most widely used data science and machine learning ecosystem. Some of the most important Python packages for data science are:

* numpy (powerful N-dimensional array)
* pandas (data analysis and preparation)
* matplotlib (2D plotting)
* scikit-learn (basic machine learning)
* keras (advanced machine learning)

All of these packages are covered in this sample project.  

Another important program is Jupyter Notebook (formerly known as IPython), which is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. 

This intro will cover Jupyter Notebooks as well.

## Working with Python Files

### Sample Project

Clone this git repo: https://github.com/thovoll/python-sandbox

### Using Anaconda Prompt

Anaconda Prompt is a Windows application that comes with Anaconda and Miniconda.

* Start Anaconda Prompt
* Go to the directory where you cloned the sample project
* Create a conda environment by entering  `conda create -n python-sandbox`
  * The environment is created here (assuming Miniconda):
    `C:\Users\<you>\AppData\Local\Continuum\miniconda3\envs\python-sandbox`
* Activate the conda environment by entering `conda activate python-sandbox`
* Run first Python file by entering `python 1-helloworld.py`
  * Console output: `Hello World`
* Run second Python file by entering `python 2-numpy.py`
  * Console output: `No module named 'numpy'`
* View installed packages: `conda list`
* Install numpy: `conda install numpy`
  * Around a dozen packages will be installed, including numpy
  * Installed packages are located here (assuming Miniconda): 
    `C:\Users\<you>\AppData\Local\Continuum\miniconda3\envs\python-sandbox\Lib\site-packages`
* Run Python file again by entering `python 2-numpy.py`
  * Console output: `[[ 0  1  2  3  4]`...
* Repeat for all other Python files in sample project

### Using Visual Studio Code

* Start Visual Studio Code
* Open folder where you cloned the sample project
* Enter command mode via Ctrl+Shift+P
* Type `Python:Select Interpreter` (it will auto-complete) and hit enter
* If the extensions mentioned above are installed, a list of Conda environmens are shown to pick from
* Right click on Python file or inside file, select "Run Python File in Terminal"
* To debug, set breakpoint using F9 and start debugging using F5

### Using PyCharm

##### Create a PyCharm project using Conda

1. Select "File, New Project", then "Scientific Project"
2. Select "Conda" under "Project Interpreter"
3. Specify the path of Conda.exe (PyCharm will then auto-fill the location for the environment)
   - Conda.exe is in `C:\Users\<you>\AppData\Local\Continuum\anaconda3\Scripts`
4. When creating the project, PyCharm will create the Conda environment.
   - Environments are created in C:\Users\\*\AppData\Local\Continuum\anaconda3\envs
5. Create Python source file and enter some code using packages like numpy 
6. Imported packages will be underlined in red and can be installed in the environment via Alt+Enter.
   - Packages are stored in C:\Users\\*\AppData\Local\Continuum\anaconda3\envs\\\*\Lib\site-packages

##### Open PyCharm project cloned from repo

* Start PyCharm app from Windows start menu
* Open project and Python file
* Run/debug the Python file 
  * This will create a run/debug configuration that is persistent
* Output will be in a Run/Debug tool window tab
  * After the code runs, the session will stay open at an interactive Python prompt
    * Sessions have to explicitly stopped with the square red stop button
* Matplotlib plots will be captured by PyCharm and displayed in "Plots" tab of the SciView
* Variables can be visualized by PyCharm in "Data" tab of the SciView
  * Either type in the variable name and press enter
  * Or click "View as Array" in the run/debug window section on the right that shows all variables
    * Can also right click on a variable and select "View as Array"
* When sitting on a breakpoint, contents of variables are shown in the editor window in-line with the code

##### Run %## Sections in PyCharm

* Mark start of section with "%##" statement in the code
  * Green run icons show up for each section
* Click run icon to execute section in PyCharm's "Python Console"
  * Console is interactive, so code can be evaluated there at any time, including in between running sections with the green run icon



## Working with Jupyter Notebooks

There are three ways to run Jupyter Notebooks (formerly named "IPython Notebooks"):

* Use the standalone Jupyter Notebook server that comes with Anaconda directly
* Use the standalone Jupyter Notebook server that comes with Anaconda from PyCharm
* Install Jupyter Notebook packages into the project's Conda environment and use from PyCharm

### Use standalone Jupyter Notebook server directly

* Open Anaconda Prompt
* Change directory to your project with ipynb files
* Activate environment by entering "activate <environment_name>"
  - The environment name is the PyCharm project name 
* Run Jupyter Notebook server by entering "jupyter notebook"
  * If Jupyter has been installed into the environment, that installation is used. If not, the Jupyter installation that comes with Anaconda is used.
* Output goes to the console and a browser tab opens with the web interface
* Run notebooks

### Use standalone Jupyter Notebook server from PyCharm

* Run separate "Jupyter Notebook" app (comes with Anaconda) from Windows start menu
  * A console window opens showing the output of the notebook server
  * A token will be shown for use in PyCharm
    * e.g. http://localhost:8888/?token=b62e4c78efec18d4d7eb29848ff895bc864f6471c4b46326
* Open ipynb file in PyCharm and click green run icon in first cell
* PyCharm will ask for notebook server URL with token (see above)
* Notebook output will be displayed inline with notebook code, as usual
  * This includes plots, which are also shown inline (not captured by PyCharm for display in SciView)
* Run the notebook cell by cell, or all cells
* Interaction with the notebook in PyCharm is fairly limited

### Install Jupyter Notebook into project and use from PyCharm

* Make sure separate "Jupyter Notebook" app is not running.
* Open ipynb file in PyCharm and click green run icon in first cell
* PyCharm will say "Cannot connect to Jupyter Notebook. Run Jupyter Notebook".
* Click on "Run Jupyter Notebook"
* A PyCharm run configuration window will appear, at the bottom it will say "Error: Install Jupyter Notebook to the interpreter of the current project.". Click the "Fix" button. This will install the Jupyter package in the current conda environment. Progress is shown in the status line in PyCharm. 
* When installation is complete, click the "Run" button in the run configuration window. An embedded Jupyter Notebook server will be started. Output will be shown inside PyCharm.
* Run the notebook cell by cell, or all cells
* Interaction with the notebook in PyCharm is fairly limited



## Recommendations

* Use Jupyter Notebooks for exploratory data science work
  * Use the standalone Jupyter Notebook server directly
* Use regular Python files for simple sample code and operationalization 
  * Use Visual Studio Code or PyCharm
* Structure the code such that relevant parts can be shared between Jupyter Notebooks and regular Python files
* Another direction to explore is to train the ML model in Python and operationalize in C# using CNTK