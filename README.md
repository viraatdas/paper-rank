# Paper Rank
Hackerrank for research papers

## High-Level Design

For now, lets not worry about authentication. 

Lets allow anyone to comment and like.
### Functional Requirements:
1. Main Page:
   - Shows top-ranked papers.
   - Allows interaction (view, vote) without logging in.
	- Requires login for commenting and saving posts.
2.	Paper Details Page:
  - Shows paper details and comments. 
  - Allows interaction (view, vote) without logging in.
	- Requires login for commenting and saving posts.
3.	User Authentication:
	- Sign up, log in, and manage user profiles.
4.	Voting System:
	- Anyone can vote on papers.
5.	Commenting System:
	- Only logged-in users can comment on papers.
6.	Search Functionality:
	- Search for papers on arxiv
7.	User-Specific Features:
	- Logged-in users can save posts.



## Backend
Based on FastAPI

### Endpoints
**User Authentication:**
- POST /register: Register a new user.
- POST /login: Log in a user.
- GET /profile: Get user profile.

**Papers:**

- GET /papers/top: Get top-ranked papers.
- GET /papers/{paper_id}: Get paper details and comments.
- POST /papers/{paper_id}/vote: Vote for a paper.
- POST /papers/{paper_id}/comment: Comment on a paper (requires login).
- POST /papers/search: Search for papers.

## Database

### Database Schema
**Paper:**
- id (Primary Key)
- title
- abstract
- url
- arxiv_id (Unique)
- votes
- created_at

**Comment:**
- id (Primary Key)
- user_id (Foreign Key)
- paper_id (Foreign Key)
- content
- created_at



## Frontend
React


