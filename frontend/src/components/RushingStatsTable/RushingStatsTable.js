/* eslint-disable */
import React from 'react';
import styled from 'styled-components';
// import PropTypes from 'prop-types';

const TableCell = styled.td`
  padding: 9px;
  border-style: none;
`;

const TableHeader = styled.td`
  padding: 9px;
  background-color: #1e1f21;
  ${({ isButton }) =>
    isButton &&
    `
    &:hover {
      cursor: pointer;
      background-color: grey;
    }
  `}
`;

const Table = styled.table`
  width: 100%;
  text-align: left;
  border-collapse: collapse;
  padding: 5px;
`;

const TableRow = styled.tr`
  border-style: none;
  &:hover {
    background-color: rgb(54, 54, 54);
    color: white;
  }
`;

const tableOrder = [
  { title: 'Player', key: 'player' },
  { title: 'Team', key: 'team' },
  { title: 'Pos', key: 'pos' },
  { title: 'Att/G', key: 'att_g' },
  { title: 'Att', key: 'att' },
  { title: 'Yds', key: 'yds', sort: true },
  { title: 'Avg', key: 'avg' },
  { title: 'Yds/G', key: 'yds_g' },
  { title: 'TD', key: 'td', sort: true },
  { title: 'Lng', key: 'lng', sort: true },
  { title: '1st', key: 'first' },
  { title: '1st%', key: 'first_percent' },
  { title: '20+', key: 'twenty_plus' },
  { title: '40+', key: 'forty_plus' },
  { title: 'FUM', key: 'fum' },
];

function RushingStatsTable({ players, sort, setSort }) {
  const handleSort = key => {
    setSort({
      sortBy: key,
      sortOrder: sort?.sortOrder === 'desc' ? 'asc' : 'desc',
    });
  };
  return (
    <Table>
      <thead>
        <tr style={{ borderBottom: '1px solid lightGrey' }}>
          {tableOrder.map(item => {
            const sortingCol = item.sort && sort?.sortBy === item.key;
            const arrow = sortingCol && sort?.sortOrder === 'desc' ? '↓' : '↑';
            return (
              <TableHeader
                key={`${item.key}-tableheader`}
                onClick={item.sort ? () => handleSort(item.key) : undefined}
                isButton={item.sort ? 'isButton' : undefined}
              >
                <b>{`${item.title}${sortingCol ? arrow : ''}`}</b>
              </TableHeader>
            );
          })}
        </tr>
      </thead>
      <tbody>
        {players?.length > 0 &&
          players.map(player => (
            <TableRow key={`${player.player}`}>
              {tableOrder.map(item => (
                <TableCell key={`${player.player}-${item.key}`}>
                  {player[item.key]}
                </TableCell>
              ))}
            </TableRow>
          ))}
      </tbody>
    </Table>
  );
}

// RushingStatsTable.propTypes = {
//   // eslint-disable-next-line react/forbid-prop-types
//   players: PropTypes.array(PropTypes.shape({})).isRequired,
// };

export default RushingStatsTable;
