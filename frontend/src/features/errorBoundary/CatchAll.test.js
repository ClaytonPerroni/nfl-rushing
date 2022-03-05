/* eslint-disable */
import React from 'react';
import { render, screen } from 'testUtils/testUtils';
import { CatchAll } from '.';

// class BuggyCounter extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = { counter: 5 };
//   }

//   render() {
//     if (this.state.counter === 5) {
//       // Simulate a JS error
//       throw new Error('I crashed!');
//     }
//     return <h1 onClick={this.handleClick}>{this.state.counter}</h1>;
//   }
// }

const BuggyCounter = () => {
  const error = true;

  if (error) {
    // Simulate a JS error
    throw new Error('I crashed!');
  }
  return <h1>Hello world</h1>;
};

describe('Error boundary', () => {
  it('error id is present', () => {
    render(
      <CatchAll>
        <BuggyCounter />
      </CatchAll>
    );
    const errorBoundaryId = screen.getByTestId('errorBoundary');
    expect(errorBoundaryId).toBeInTheDocument();
  });
});
