import RushingStatsPage from 'components/RushingStats/RushingStatsPage';
import React, { useState } from 'react';
import styled from 'styled-components';
import { Row, Col } from 'styledComponents';

const DownloadButton = styled.button`
  border: none;
  background-color: white;
  padding: 10px;
  float: right;
  ${({ isNotActive }) =>
    isNotActive &&
    `
  background-color: grey;
  `}
`;

const Main = () => {
  const [tab, setTab] = useState('RushingStats');
  return (
    <div>
      <Row style={{ backgroundColor: '#1e1f21' }}>
        <Col style={{ padding: 15 }}>
          <div>
            <h1 style={{ color: 'white' }}>
              <i>theScore</i>
            </h1>
            <div
              style={{
                backgroundColor: '#f9bf02',
                width: '1.1%',
                height: 3,
                position: 'relative',
                left: 41,
                bottom: 5,
              }}
            />
          </div>
        </Col>
        <Col
          style={{ padding: 15, display: 'flex', justifyContent: 'flex-end' }}
        >
          <DownloadButton
            onClick={() => setTab('RushingStats')}
            isNotActive={tab !== 'RushingStats' ? 'yes' : undefined}
          >
            Rushing Stats
          </DownloadButton>
          <DownloadButton
            onClick={() => setTab('Other')}
            isNotActive={tab !== 'Other' ? 'yes' : undefined}
          >
            Other Stats
          </DownloadButton>
        </Col>
      </Row>
      {tab === 'RushingStats' && <RushingStatsPage />}
    </div>
  );
};

export default Main;
