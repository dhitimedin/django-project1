// src/components/AuthorDetail.js

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const AuthorDetail = () => {
  const { id } = useParams();
  const [author, setAuthor] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/books/api/authors/${id}/`)
      .then(response => response.json())
      .then(data => setAuthor(data));
  }, [id]);

  if (!author) return <div>Loading...</div>;

  return (
    <div className="author-detail">
      <h1>{author.first_name} {author.last_name}</h1>
      <img src={author.headshot} alt={`${author.first_name} ${author.last_name}`} />
      <p><strong>Email:</strong> {author.email}</p>
    </div>
  );
};

export default AuthorDetail;
