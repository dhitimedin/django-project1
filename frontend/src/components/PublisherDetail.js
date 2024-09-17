// src/components/PublisherDetail.js

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const PublisherDetail = () => {
  const { id } = useParams();
  const [publisher, setPublisher] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/books/api/publishers/${id}/`)
      .then(response => response.json())
      .then(data => setPublisher(data));
  }, [id]);

  if (!publisher) return <div>Loading...</div>;

  return (
    <div className="publisher-detail">
      <h1>{publisher.name}</h1>
      <p><strong>Website:</strong> <a href={publisher.website}>{publisher.website}</a></p>
    </div>
  );
};

export default PublisherDetail;
