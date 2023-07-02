import { Navbar, Nav, Container } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

export default function Header() {
  return (
    <header>
      <Navbar bg="dark" variant="dark">
        <Container>
          <LinkContainer to="/">
            <Navbar.Brand>Ecommerce</Navbar.Brand>
          </LinkContainer>
          <Nav className="mr-auto">
            <LinkContainer to="/cart">
              <Nav.Link>
                {" "}
                <i className="fa fa-shopping-cart"></i> Cart
              </Nav.Link>
            </LinkContainer>
            <LinkContainer to="/login/">
              <Nav.Link>
                {" "}
                <i className="fa fa-user"></i> Login
              </Nav.Link>
            </LinkContainer>
            <LinkContainer to="/register/">
              <Nav.Link>
                {" "}
                <i className="fa fa-user"></i> Register
              </Nav.Link>
            </LinkContainer>
          </Nav>
        </Container>
      </Navbar>
    </header>
  );
}
