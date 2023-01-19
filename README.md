# Abstract_Cipher_App
Assignment for NuageBiz
1.Clone the projet using below command: git clone https://github.com/jagritisingh1102/NuageAssignment.git
2.Open the project in any python editor NOTE: Before doing below steps please check you are or correct path i.e., ../NuageAssignment
3.create virtual environment for the project using below command: python3 -m virtualenv venv
4.Select the correct interpreter for the project
5.Activate the virtual environment using below command: source venv/bin/activate
6.Install all the project requirements using below command: pip install -r requirements.txt
7.Now to run the Command Line Application, a setup.py file has been created to run it use command pip install .
8. If any data is updated in setup.py file, to apply the changes we need to reinstall it using command pip install -e .
9.For testing the application there is already a txt file added in the project named sample_file.txt
10. Now to run the project use this command in the terminal- abs_cipher sample_file.txt output_file.txt, Here output_file.txt will be created by the program and it will contain the output
11. This program also contains unittest using Pytest to test it run pytest test.py
