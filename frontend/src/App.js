// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './components/HomePage';
import BookDetail from './components/BookDetail';
import AuthorDetail from './components/AuthorDetail';
import PublisherDetail from './components/PublisherDetail';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/books/:id" element={<BookDetail />} />
        <Route path="/authors/:id" element={<AuthorDetail />} />
        <Route path="/publishers/:id" element={<PublisherDetail />} />
      </Routes>
    </Router>
  );
}

export default App;
