import axios from "axios";
import { useState } from "react";
import { Form, Button } from "react-bootstrap";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const onSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    alert("Login clicked");
    console.log("username:" + username);
    console.log("password:" + password);

    const loginCall = {
      method: "post",
      url: "http://ecommerce_server:8000/accounts/login/",
      data: {
        username: username,
        password: password,
      },
    };
    axios(loginCall)
      .then((result) => {
        console.log("result:" + result);
      })
      .catch((err) => {
        console.log("error:" + err);
      });
  };

  return (
    <>
      <h2>Login</h2>
      <Form>
        {/* username */}
        <Form.Group controlId="formBasicUsername">
          <Form.Control
            type="text"
            placeholder="Username"
            name="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </Form.Group>

        {/* password */}
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </Form.Group>

        {/* submit button */}
        <Button variant="primary" type="submit" onClick={(e) => onSubmit(e)}>
          Login
        </Button>
      </Form>
    </>
  );
}
