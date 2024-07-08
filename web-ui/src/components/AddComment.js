import React, { useState } from 'react';
import axios from 'axios';
import './AddComment.css';

const AddComment = ({ paperId }) => {
  const [comment, setComment] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post(`http://127.0.0.1:8000/papers/${paperId}/comment/`, { text: comment })
      .then(response => {
        setComment('');
        console.log('Comment added:', response.data);
      })
      .catch(error => {
        console.error('There was an error adding the comment!', error);
      });
  };

  return (
    <form onSubmit={handleSubmit} className="add-comment-form">
      <div className="form-group">
        <textarea
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          placeholder="Add a comment"
          className="form-control"
        ></textarea>
      </div>
      <button type="submit" className="btn btn-primary mt-2">Submit</button>
    </form>
  );
};

export default AddComment;
