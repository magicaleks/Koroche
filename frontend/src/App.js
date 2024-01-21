import './App.css';
import './reset.css';

import React, {useState} from 'react';

import Header from './Header';

import Landing from './Landing';
import ServicePage from './ServicePage';

const pages = {
  landing: Landing,
  servicePage: ServicePage
};

function App() {

  let [current_page, setPage] = useState("landing");

  let [timeValue, setTimeValue] = useState(1);
  let [linkName, setLinkName] = useState("");
  let [newLinkName, setNewLinkName] = useState("");

  
	return <div id="app">
    {Header(current_page, setPage)}
		{current_page === "servicePage" ? pages[current_page](timeValue, setTimeValue, linkName, setLinkName, newLinkName, setNewLinkName): pages[current_page]()}
	</div>;

}

export default App;