import React from 'react';
import './App.css';
import './BootstrapGrid.css';
import './CustomClassNames.css';
import { CatchAll } from 'features/errorBoundary';
import Main from 'pages/Main/Main';

function App() {
  return (
    <CatchAll>
      <Main />
    </CatchAll>
  );
}

export default App;
