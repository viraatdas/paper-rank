import React from 'react';
import { Link } from 'react-router-dom';
import './PaperItem.css';

const PaperItem = ({ paper }) => {
  return (
    <div className="paper-item mb-3 p-3 bg-light border rounded">
      <h2 className="h5">
        <Link to={`/papers/${paper.id}`}>{paper.title}</Link>
      </h2>
      <p className="text-muted">{paper.abstract}</p>
    </div>
  );
};

export default PaperItem;
