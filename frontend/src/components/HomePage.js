import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';  // Import the CSS file

const HomePage = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch('/books/api/books/')
      .then(response => response.json())
      .then(data => setBooks(data));
  }, []);

  return (
    <div className="book-list">
      {books.map(book => (
        <div className="book-card" key={book.id}>
          <Link to={`/books/${book.id}`}>
            <img src={book.cover} alt={book.title} />
          </Link>
          <h3>{book.title}</h3>
          <p>
            Author:
            {book.authors.map(author => (
              <Link to={`/authors/${author.id}`} key={author.id}>
                {author.first_name} {author.last_name}
              </Link>
            ))}
          </p>
          <p>
            Publisher:
            <Link to={`/publishers/${book.publisher.id}`}>
              {book.publisher.name}
            </Link>
          </p>
          <p>Date of Publishing: {book.publication_date}</p>
        </div>
      ))}
    </div>
  );
};

export default HomePage;
