// src/components/AuthorDetail.js

import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import './AuthorDetail.css';  // Import the CSS file

const AuthorDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [author, setAuthor] = useState(null);

  useEffect(() => {
    fetch(`http://localhost/books/api/authors/${id}/`)
      .then(response => response.json())
      .then(data => setAuthor(data));
  }, [id]);

  const handleBackClick = () => {
    navigate('/');
  };

  if (!author) return <div>Loading...</div>;

  return (
    <div className="author-detail">
      <img src={author.headshot} alt={`${author.first_name} ${author.last_name}`} />
      <h1>{author.first_name} {author.last_name}</h1>
      <p><strong>Email:</strong> {author.email}</p>
	  <button onClick={handleBackClick} className="back-button">Back to Home</button>
    </div>
  );
};

export default AuthorDetail;
