# BrawlhalaMarblesTracker

# Download and set-up

## Step 1:

Clone the repository onto your system. 

Navigate to an empty directory and open a terminal, then paste the following code:

git clone https://github.com/ndungu-kr/BrawlhalaMarblesTracker.git

## Step 2:

In the same directory as tha main.py file, create a virtual environment using the command:

py -m venv .venv

Activate your virtual environment if necessary using:

Windows:
.venv\bin\Activate.bat

## Step 3:

You will now need to install the packages required for the application to run, use the following command:

python -m pip install -r requirements.txt

Upgrade your pip if need be using:

python -m pip install --upgrade pip

# DB Migrations

## Making Changes to the DB

### Step 1:

First you wou would update the models in models.py with your required changes

### Step 2:

After updating your models, generate a new migration script. Make sure your virtual environment is activated and you are in your project directory:

flask db migrate -m "Added new field"

### Step 3:

Navigate to the migrations/versions directory and open the newly created migration script. It should include the necessary SQL commands to add the new field or make other changes to your database.

### Step 4:

Apply the changes to your database by running:

flask db upgrade


