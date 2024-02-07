import { BrowserRouter, Routes, Route } from "react-router-dom";

import "./App.css";
import { HomePage, Redirect } from "./components/pages";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage/>}/>
        <Route path="/:alias" element={<Redirect/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
