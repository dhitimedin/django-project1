import React, { useEffect, useState } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';

const BookDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [book, setBook] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/books/api/books/${id}/`)
      .then(response => response.json())
      .then(data => setBook(data));
  }, [id]);

  const handleBackClick = () => {
    navigate('/');
  };

  if (!book) return <div>Loading...</div>;

  return (
    <div className="book-detail">
      <h1>{book.title}</h1>
      <img src={book.cover_image} alt={book.title} />
      <p><strong>Published on:</strong> {book.publication_date}</p>
      <p>
        <strong>Authors:</strong>
        {book.authors.map(author => (
          <Link to={`/authors/${author.id}`} key={author.id}>
            {author.first_name} {author.last_name}
          </Link>
        ))}
      </p>
      <p>
        <strong>Publisher:</strong>
        <Link to={`/publishers/${book.publisher.id}`}>
          {book.publisher.name}
        </Link>
      </p>
      <button onClick={handleBackClick} className="back-button">Back to Home</button>
    </div>
  );
};

export default BookDetail;
