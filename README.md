This project is a task management tool designed to help you organize your daily activities 
and accomplish your goals efficiently. With this app, you can create a to-do list, 
mark tasks as done, add personal tags to categorize them as per your preferences, 
such as home, work, personal, or any other category you want. 

The project offers a clean and intuitive interface that makes it easy to use, even for beginners. 
It also provides you with the option to set deadline to help you stay on top of your tasks. 
Whether you need to track your work projects or plan your household chores, this project is a handy 
tool to keep your life organized and productive.

To run this projects locally, use the following steps:

1. Clone repo from GIT:


    git clone git@github.com:natalie-goriela/to-do-list.git

2. If you are using PyCharm - it may propose you to automatically create venv for your project 
and install requirements in it, but if not: 


    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt
   
The secret key to this project is saved within .env file, which is hidden.
You can create your own .env file to store your secret key like it is shown in .env_sample file. 