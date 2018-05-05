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

- "Python"
- "Anaconda Extension Pack" (also installs "YAML Support by Red Hat")
- "VS Code Jupyter Notebook Previewer"

Install extensions by clicking on the extensions icon in the left navigation sidebar or by entering command mode via Ctrl+Shift+P and typing "Extensions: Install Extensions" (it will auto-complete), followed by hitting Enter. Then search for extensions and click "Install". You might have to "Reload" as well.

### PyCharm

PyCharm can be used for working on Python projects. It has a free version ("Community") and a paid version ("Professional") and supports conda environments. It's more heavyweight than Visual Studio Code but has more advanced code navigation and refactoring support. The paid version also has advanced support for data science work, a Python profiler, and much more. 

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

## Interactive Python

* Start Anaconda Prompt
* Start the Python interpreter by entering `python`
* Enter python code and press enter :-)
  * For example: `print("Hello World")`
* To exit the interpreter, enter `exit()`

## Working with Python Files

### Using Anaconda Prompt

Note: Anaconda Prompt is a Windows application that comes with Anaconda and Miniconda.

* Start Anaconda Prompt
* Change directory to where you cloned this repo
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

Note: Visual Studio Code cannot create Conda environments. Please create a Conda environemnt using Anaconda Prompt as described above.

* Start Visual Studio Code
* Open folder where you cloned this repo
* Enter command mode via Ctrl+Shift+P
* Type `Python:Select Interpreter` (it will auto-complete) and hit enter
* Pick "python-sandbox" from the list of Conda environmens that are shown
* Right click on any Python file (or inside the file) and select "Run Python File in Terminal"
* To debug, set a breakpoint using F9 and start debugging using F5

### Using PyCharm

This is left as an exercise for the reader. PyCharm can use an existing Conda environment, or create a new one.

## Working with Jupyter Notebooks

* Open Anaconda Prompt
* Change directory to where you cloned this repo
* Activate environment by entering `conda activate python-sandbox`
* Install Jupyter Notebook by entering `conda install jupyter`
* Run Jupyter Notebook server by entering `jupyter notebook`
  * Notebook server output goes to the console and a browser tab opens with the web interface
* In the Jupyter Notebook web interface:
  * Click on `polyfit.ipynb`
    * The notebook opens and a notebook kernel will automatically start in the notebook server
  * Click the "Run" button to run the notebook cell by cell
  * Select "Kernel", "Shutdown" to shut down the kernel
* Back in the Anaconda Prompt
  * Press Ctrl+C to exit the notebook server

## 
