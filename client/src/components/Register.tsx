import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

export default function Register() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");
  // const [register, setRegister] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    alert("Submited");
    console.log("first name:" + firstName);
    console.log("last name:" + lastName);
    console.log("username:" + username);
    console.log("email:" + email);
    console.log("password:" + password);
    console.log("password2:" + password2);
  };

  return (
    <>
      <h2>Register</h2>
      <Form onSubmit={(e) => handleSubmit(e)}>
        <Form.Group controlId="formBasicFirstName">
          {/* first name */}
          <Form.Control
            type="text"
            name="firstName"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            placeholder="First Name"
          />
        </Form.Group>

        {/* last name */}
        <Form.Group controlId="formBasicLastName">
          <Form.Control
            type="text"
            name="lastName"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            placeholder="Last Name"
          />
        </Form.Group>

        {/* username */}
        <Form.Group controlId="formBasicUserName">
          <Form.Control
            type="text"
            name="userName"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Username"
          />
        </Form.Group>

        {/* email */}
        <Form.Group controlId="formBasicEmail">
          <Form.Control
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email Address"
          />
        </Form.Group>

        {/* password */}
        <Form.Group controlId="formBasicPassword">
          <Form.Control
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
          />
        </Form.Group>

        {/* password2 */}
        <Form.Group controlId="formBasicPassword2">
          <Form.Control
            type="password"
            name="password2"
            value={password2}
            onChange={(e) => setPassword2(e.target.value)}
            placeholder="Confirm Password"
          />
        </Form.Group>
        {/* submit button */}
        <Button
          variant="primary"
          type="submit"
          onClick={(e) => handleSubmit(e)}
        >
          Register
        </Button>
        <LinkContainer to="/">
          <Button variant="secondary">Cancel</Button>
        </LinkContainer>
      </Form>
      <br></br>
      <a href="/login/">Already have an account? Login</a>
    </>
  );
}
