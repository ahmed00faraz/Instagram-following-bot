# Instagram Follower Bot

This Python script automates the process of finding and following Instagram followers of a specified account. It uses Selenium to interact with Instagram's web interface and follows users from the follower list of a similar account.

## Features

- Automates the login process to Instagram.
- Finds and scrolls through followers of a specified account.
- Automatically follows users from the follower list.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver
- Google Chrome browser installed

## Installation

1. Clone this repository or download the script.

2. Install the required dependencies using pip:
    ```bash
    pip install selenium
    ```

3. Ensure that Chrome WebDriver is installed. You can download it from the [official Chrome WebDriver website](https://sites.google.com/a/chromium.org/chromedriver/downloads).

4. Make sure the Chrome WebDriver is in your system's `PATH` or specify the location in the script.

## Usage

1. Replace the `USERNAME` and `PASSWORD` variables in the script with your Instagram credentials:
    ```python
    USERNAME = "your username"
    PASSWORD = "your password"
    ```

2. Replace the `SIMILAR_ACCOUNT` variable with the Instagram username of the account whose followers you want to follow:
    ```python
    SIMILAR_ACCOUNT = "pubity"
    ```

3. Run the script:
    ```bash
    python insta_follower_bot.py
    ```

4. The script will log in to your Instagram account, navigate to the followers of the specified account, scroll through them, and follow those you haven't followed yet.

## How it Works

1. **Login**: The script navigates to Instagram's login page, enters your username and password, and logs in.

2. **Find Followers**: The script navigates to the followers page of a specified account and scrolls through the list to load more followers.

3. **Follow Users**: The script finds all users in the followers list and clicks the "Follow" button for each one that is not already followed.

## Notes

- The script is tailored for Instagram's current layout. Changes to Instagram's interface may require modifications to the script.
- Using automation to follow accounts in bulk may violate Instagram's terms of service, so use this script responsibly and at your own risk.

## Troubleshooting

- If the script fails to log in, ensure that your credentials are correct and that you are using the latest version of Chrome and Chrome WebDriver.
- Adjust the sleep times depending on your internet speed and the responsiveness of Instagram.
