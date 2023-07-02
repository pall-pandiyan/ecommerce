import Login from "./components/Login";
import Register from "./components/Register";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/register/" Component={Register} />
        <Route path="/login/" Component={Login} />
      </Routes>
    </Router>
  );
}

export default App;
