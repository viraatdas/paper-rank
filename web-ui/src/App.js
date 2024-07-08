import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PaperList from './components/PaperList';
import PaperDetails from './components/PaperDetails';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<PaperList />} />
          <Route path="/papers/:id" element={<PaperDetails />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
