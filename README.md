# DALL·E 2 Image Generator Python App

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)

## [Watch the Tutorial for this Project](https://youtu.be/Ihcb3Lg4twI)

![YouTube Thumbnail](https://github.com/Spidy20/DALLE_Image_Generator/blob/master/yt_thumb.jpg)

## Overview

This project demonstrates the creation of a "Text to Image" application using Python, OpenAI, and Streamlit. The following technologies and services are used:

- `Streamlit` as a server and handling front end.
- OpenAI API key from `OpenAI`.
- `DALL.E-2` model for text-to-image generation. 
- `AWS EC2` for deployment (24/7 running).

## Steps

1. Create free accounts on [OpenAI](https://platform.openai.com/account/api-keys) and [AWS](https://console.aws.amazon.com/).
2. Create a Streamlit App.
3. Create an EC2 instance on AWS.
4. Git clone this repository on the EC2 instance.
5. Install the requirements.
6. Use the `OPENAI_API_KEY` in your code (avoid using static values, use global variables).
7. Run the script on the EC2 instance.

## Usage

To use this project:

1. Clone the repository.
2. Open a terminal in the working directory.
3. Run the following command to install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Set the `OPENAI_API_KEY` as a global variable in your environment (replace `-------API KEY--------` with your actual API key):
    ```
    export OPENAI_API_KEY="-------API KEY--------"
    ```
5. The `App.py` file contains the Streamlit application.
6. Run the script with the following command:
    ```
    nohup python3 streamlit run App.py --server.port 80
    ```
7. To stop the running application:
   - Get the process ID of the running process:
     ```
     ps -ef 
     ```
   - Kill the process using its ID:
     ```
     kill [PROCESS_ID]
     ```

For a more detailed explanation of this project, refer to the tutorial on the Machine Learning Hub YouTube channel.

## Screenshots

<img src="https://github.com/Spidy20/DALLE_Image_Generator/blob/master/sc1.jpg" width="270" height="500">

## Support

If you find this project helpful, consider supporting me:

- [Buy me a Coffee☕](https://www.buymeacoffee.com/spidy20)
- [Donate via PayPal](https://www.paypal.me/spidy1820) (It will inspire me to work on more projects)

Feel free to follow me and star⭐ this repository!
