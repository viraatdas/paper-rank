import sqlite3
import random
import os

# Remove existing database if it exists
db_filename = 'local_test.db'
if os.path.exists(db_filename):
    os.remove(db_filename)

# Set up the database connection
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# Read and execute the database schema from the file
def create_schema_from_file():
    with open('database.sql', 'r') as f:
        sql_script = f.read()
    cursor.executescript(sql_script)

# Seed the database with random data
def seed_database():
    # Seed Papers table with 10 records
    for i in range(10):
        paper_title = f"Paper {i+1} Title"
        paper_abstract = f"This is abstract for Paper {i+1}"
        paper_url = f"http://example.com/paper{i+1}"
        paper_arxiv_id = f"arxiv{i+1}"
        cursor.execute("INSERT INTO Papers (title, abstract, url, arxiv_id) VALUES (?, ?, ?, ?)",
                       (paper_title, paper_abstract, paper_url, paper_arxiv_id))

    # Seed Votes table with some sample votes
    papers = [row[0] for row in cursor.execute("SELECT id FROM Papers").fetchall()]

    for i in range(50):  # add 50 random votes
        paper_id = random.choice(papers)
        vote_value = random.choice([1, -1])
        cursor.execute("INSERT INTO Votes (paper_id, vote_value) VALUES (?, ?)",
                       (paper_id, vote_value))

    # Commit the changes
    conn.commit()

# Function to display all papers
def display_papers():
    cursor.execute("SELECT * FROM Papers")
    papers = cursor.fetchall()
    for paper in papers:
        print(paper)

# Function to display all votes
def display_votes():
    cursor.execute("SELECT * FROM Votes")
    votes = cursor.fetchall()
    for vote in votes:
        print(vote)

# Create schema from the file and seed the database
create_schema_from_file()
seed_database()

# Display data
print("Papers:")
display_papers()
print("\nVotes:")
display_votes()

# Close the connection
conn.close()
