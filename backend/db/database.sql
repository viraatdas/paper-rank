-- Paper Tables Schema
CREATE TABLE Papers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    abstract TEXT NOT NULL,
    url VARCHAR(255) NOT NULL,
    arxiv_id VARCHAR(50) UNIQUE NOT NULL,
    votes INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Votes Tables
CREATE TABLE Votes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    paper_id UUID NOT NULL REFERENCES Papers(id),
    user_id UUID REFERENCES Users(id), -- Allow NULL for anonymous votes
    vote_value INTEGER NOT NULL, -- 1 for upvote, -1 for downvote
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES Users(id)
);
