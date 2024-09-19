import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

const PublisherDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [publisher, setPublisher] = useState(null);

  useEffect(() => {
    fetch(`http://localhost/books/api/publishers/${id}/`)
      .then(response => response.json())
      .then(data => setPublisher(data));
  }, [id]);

  const handleBackClick = () => {
    navigate('/');
  };

  if (!publisher) return <div>Loading...</div>;

  return (
    <div className="publisher-detail">
      <h1>{publisher.name}</h1>
      <p><strong>Website:</strong> <a href={publisher.website}>{publisher.website}</a></p>
      <button onClick={handleBackClick} className="back-button">Back to Home</button>
    </div>
  );
};

export default PublisherDetail;
