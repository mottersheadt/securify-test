# Setup

## Front-end Application
1. Copy the `/frontend/assets/config.template.json` file and rename to `/frontend/assets/config.json`. 
2. Modify the secureApiurl in the new config.json file to have the appropriate VGS_TENANT_ID.
3. If you are not running the backend locally (e.g. via Heroku), then modify the apiUrl parameter in the config.json to be the address of the deployed server.

To start the frontend application, run the following commands from the root of the directory.
```
cd frontend
npm i
npm run serve
```

## Back-end Server
### Local
Before you can run the backend app locally, you will need to copy the .env file into the root of the repository. This file contains all VGS secure settings. The filw should contain the following settings:
- VGS_USERNAME
- VGS_PASSWORD
- VGS_TENANT_ID
- VGS_PROXY_BASE
- VGS_OUTBOUND_CERT

To start the backend server locally, run the following commands from the root of the repository:
```
pip install -r requirements.txt
python wsgi.py debug
```