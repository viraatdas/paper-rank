import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import AddComment from './AddComment';
import './PaperDetails.css';

const PaperDetails = () => {
  const { id } = useParams();
  const [paper, setPaper] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/papers/${id}`)
      .then(response => {
        setPaper(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the paper!', error);
      });
  }, [id]);

  if (!paper) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container">
      <h1 className="my-4">{paper.title}</h1>
      <p className="text-muted">{paper.abstract}</p>
      <p>Votes: {paper.votes}</p>
      <AddComment paperId={id} />
    </div>
  );
};

export default PaperDetails;
