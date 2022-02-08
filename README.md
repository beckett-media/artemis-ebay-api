# ebay-api
Ebay API exploration - This documentation is a work in progress!! 

# Credentials / Gaining Access

## Getting Access to the eBay credentials 

1. Gain access to the eBay developer portal credentials by emailing noah@plainspokendigital, cc'ing chris@plainspokendigital.com and bsutherland@entrustglobalgroup.com
2. After getting the credentials, sign in to https://developer.ebay.com 
3. After the log-in screen, click on your user account (`Hi beckettdev`) and navigate to `Application Access Keys`. Here, you'll find nearly all of the credentials you'll need to login. Things should look like this: 

![image](https://user-images.githubusercontent.com/18645647/152902659-0c5fc332-a304-478d-99d2-e1350dd96f62.png)
 
## Important Notes 
1. Note that different APIs require different credentials! The Finding API, which we'll be using most, only needs the App ID. 
2. Also note that there are keys for "Sandbox" and "Production" - Sandbox does not have real data, and is primarily used for executing fake transactions (which we don't need to do. 
3. **Keep all credentails private. Exposure of Beckett Credentials could mean permanent access loss of the eBay API, per eBay API policy!!!!**


# Setting up this repo

Hopefully, repo setup should be pretty useful! We're going to be using Poetry and Python Virtual Envs. This guide assumes you have set up GitHub access properly, and have Python and Homebrew installed. 

1. Clone the repo 

`git clone git@github.com:plainspokendigital/ebay-api.git` 

2. Install Poetry and set it up 

`brew install poetry` to install Poetry on your machine

`poetry install` to install all the Poetry requirements from the `.toml` file

3. Navigate to the repo directory and install your virtual environment

`cd ebay-api` followed by 

`python3 -m venv ebay-env`, then

`source ebay-env/bin/activate` 

4. Find your eBay credentials from the first half of this guide. For the findingAPI you need the `appid` for the Production environment. Paste the appid into the Beckett_python_api.py file on ~line 6. 
- !WIP! The ebay-config.yaml file is still a work in progress. So is saving credentials in a safe way. 


Information on how to get the oauth-redirect-URI:
https://developer.ebay.com/api-docs/static/oauth-redirect-uri.html# 
