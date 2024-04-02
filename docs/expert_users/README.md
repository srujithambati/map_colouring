# Step 1: Clone the Repository
git clone https://github.com/your-username/your-project.git

# Step 2: Navigate to the Project Directory

# Step 3: Install Dependencies
pip install -r requirements.txt

# Step 4: Create a Virtual Environment (Optional )
python -m venv venv

# Step 5: Activate the Virtual Environment
# On Windows:
venv\Scripts\activate
# On macOS and Linux:
source venv/bin/activate

# Step 6: Set Up the Database
# Create the SQLite database file if it doesn't exist:
touch database.db

# otherwise run the following:
flask db migrate -m "Initial migration"
flask db upgrade

# Step 7: Run the Application
python app.py

# Step 9: Access the Application
# Once the application is running, you can access it by navigating to `http://localhost:5000` in your web browser.
