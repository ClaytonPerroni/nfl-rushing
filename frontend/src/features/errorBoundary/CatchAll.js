import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { Row, Col } from 'styledComponents';

export default class CatchAll extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI.
    return { hasError: true, error };
  }

  // eslint-disable-next-line no-unused-vars
  componentDidCatch(error) {
    // You can also log the error to an error reporting service
    // logErrorToMyService(error, errorInfo);
  }

  render() {
    const { children } = this.props;
    const { hasError } = this.state;

    if (hasError) {
      // You can render any custom fallback UI
      return (
        <Row>
          <Col style={{ textalign: 'center' }}>
            <h1 data-testid="errorBoundary">Oops! Something went wrong.</h1>
          </Col>
        </Row>
      );
    }

    return children;
  }
}

CatchAll.propTypes = {
  children: PropTypes.node.isRequired,
};
