# :shoe: Steps
Author: [Eduardo Correia](https://github.com/edu-correia)

## Install the necessary libraries
(I presume you already have GCC compiler)\
First, install python and its tools on your computer: https://www.python.org/downloads/
<br>

Then, install "cython", used for converting your python file to a C file:\
`pip3 install cython`
<br>

## Write your python code
This part has no secret, you just go and write your python code according to your project ideas.\
Follow my [example file](drawing_library.py).\
If you need help with writing basic Python code, you can study this official [documentation](https://docs.python.org/3/tutorial/).\
If you need help with the drawing library(Turtle), you can study this official [documentation](https://docs.python.org/3/library/turtle.html).

## Convert your python file
To convert your python file, you will need to use cython:\
`cython --embed <your-file-name>.py`

## Compile it
Before compiling it, we will need to set a variable:\
`PYTHONLIBVER=python$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')$(python3-config --abiflags)`
<br><br>

Now you compile it using python libraries:
`gcc -Os $(python3-config --includes) <your-file-name>.c -o <your-output-file> $(python3-config --ldflags) -l$PYTHONLIBVER`

## Use it on your own project
Now, to call your own fractal drawing code binary, you just need to use the following C line:\
`system("./<your-output-file>");`
<br>

Be creative with it!