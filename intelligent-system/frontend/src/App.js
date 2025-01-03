import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import PdfUpload from './components/PdfUpload';
import WebScrape from './components/WebScrape';
import NlpResults from './components/NlpResults';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <h1>Intelligent System for Information Extraction</h1>
        <Switch>
          <Route path="/upload" component={PdfUpload} />
          <Route path="/scrape" component={WebScrape} />
          <Route path="/results" component={NlpResults} />
          <Route path="/" exact>
            <h2>Welcome to the Intelligent System</h2>
            <p>Select an option from the menu to get started.</p>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;