# Using API Collection BB-9218-OEX

The collection allows you to:
- Create a content library  
- View, add, update, and remove library team members  

## Prerequisites

- [Postman](https://www.postman.com/downloads/) installed on your laptop  
- Access to an Open edX instance (e.g., `http://studio.local.openedx.io:8001`)  
- A valid user account with permissions to manage libraries  

## Files Provided

| File | Description |
|------|-------------|
| `BB-9218-OEX-EnvironmentVariables.postman_environment.json` | Environment template with reusable variables |
| `DiscoveryCollection-BB-9218-OEX.postman_collection.json` | API request collection for library operations |

## Step 1: Import Files into Postman

### Import the Environment
1. Open Postman  
2. Click **Environments** (left sidebar) → **Import**  
3. Choose `BB-9218-OEX-EnvironmentVariables.postman_environment.json`  
4. The environment `BB-9218-OEX-EnvironmentVariables` will appear in your environments list  

### Import the Collection
1. Click **Collections** (left sidebar) → **Import**  
2. Choose `DiscoveryCollection-BB-9218-OEX.postman_collection.json`  
3. The collection `DiscoveryCollection-BB-9218-OEX` will be added  

## Generate JWT
Access admin page: (http://local.openedx.io:8000/admin/oauth2_provider/application/)
- Add an aplication 
Note: Please keep note of Client id and Client secret you will use them in the next step.

- Use  `jwtGenerator.py`, it generates a valid jwt_token to access open edx rest api
 In order to run this file follow the following instructions.

 1. Install required packages
    ```bash
    pip install requests
 2. Access the `jwtGenerator.py` and replace the following placeholders with your actual values noted from the above step.
 `REPLACE_ME_1`: Your OAuth2 application's Client ID.
 `REPLACE_ME_2`: Your OAuth2 application's Client Secret.
 `RPLACE_ME_3`: The domain of your Open edX LMS (e.g., myuniversity.edx.org).
3. run `python3 jwtGenerator.py` if you are using JWT or `bearerGenerator.py` if you are using Bearer Authentication

 Reference: [Please refer to this link for a complete documentation.](https://github.com/openedx/openedx-platform/blob/master/docs/how-tos/use_the_api.rst)

## Step 2: Configure Environment Variables

Fill in the following required variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `base_url` | Base URL of your Open edX Studio instance | e.g. `http://studio.local.openedx.io:8001` |
| `jwt_token` | A valid JWT token | e.g. `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...` |
| `bearer` | A valid JWT token | e.g. `HSPHrenGfcny9DW3471SMpkg3dHzWz` |
| `library_id` | ID of an existing library – used for team management | e.g. `lib:MynewLibrary2ORG:MynewLibrary2ID` |
| `teammember` | Username or email of a team member to modify/delete | e.g. `testuser` |

### Available Requests

| Request Name | Method | Description |
|--------------|--------|-------------|
| **CreateLibrary** | POST | Creates a new library. You must provide `title`, `org`, and `slug` in the request body. |
| **GetLibraryTeamMembers** | GET | Retrieves the current team members of a library. |
| **AddLibraryTeamMember** | POST | Adds a new member (by email) with a specified `access_level` (`read`, `admin`). |
| **UpdateLibraryMemberRole** | PUT | Updates the role of an existing team member. |
| **DeleteLibraryTeamMember** | DELETE | Removes a team member from the library. |

