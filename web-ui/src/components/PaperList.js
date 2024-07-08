import React, { useEffect, useState } from 'react';
import axios from 'axios';
import PaperItem from './PaperItem';
import './PaperList.css';

const PaperList = () => {
  const [papers, setPapers] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/papers/')
      .then(response => {
        setPapers(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the papers!', error);
      });
  }, []);

  return (
    <div className="container">
      <h1 className="my-4">Paper List</h1>
      {papers.map(paper => (
        <PaperItem key={paper.id} paper={paper} />
      ))}
    </div>
  );
};

export default PaperList;
