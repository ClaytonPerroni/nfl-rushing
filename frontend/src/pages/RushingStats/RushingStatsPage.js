/* eslint-disable react/function-component-definition */
import { RushingStatsTable } from 'components/RushingStatsTable';
// import { debounce } from 'features/debounce';
import { handleSearchCall } from 'features/rushingStats';
import { handleCSVCall } from 'features/rushingStats/RushingStatsAxios';
import React, { useEffect, useState, useRef } from 'react';
import ReactPaginate from 'react-paginate';
import styled from 'styled-components';
import { Row, Col } from 'styledComponents';

const SearchInput = styled.input`
  padding: 10px;
  border-radius: 4px;
  border: none;
  width: 250px;
`;

const DownloadButton = styled.button`
  border: none;
  border-radius: 4px;
  background-color: white;
  padding: 10px;
  float: right;
`;

const RushingStatsPage = () => {
  const [results, setResults] = useState([]);
  const [sort, setSort] = useState({ sortBy: 'yds', sortOrder: 'desc' });
  const [page, setPage] = useState(1);
  const [query, setQuery] = useState('');
  const [pageSize, setPageSize] = useState('10');
  const searchInterval = useRef();

  useEffect(() => {
    const getResults = async ({ pageNumber, sortBy, sortOrder }) => {
      const res = await handleSearchCall({
        page: pageNumber,
        pageSize,
        sortBy,
        sortOrder,
        query,
      });
      setResults(res);
    };

    getResults({
      pageNumber: page,
      sortBy: sort?.sortBy,
      sortOrder: sort?.sortOrder,
      query,
    });
  }, [setResults, sort, page, query, pageSize]);

  const handlePageChange = async ev => {
    const { selected } = ev;
    setPage(selected + 1);
  };
  return (
    <div>
      <div style={{ padding: 25 }}>
        <Row style={{ marginTop: 5 }}>
          <Col>
            <SearchInput
              // value={query}
              onChange={e => {
                const val = e.target.value;
                // wait for typing to stop to send query
                clearTimeout(searchInterval.current);
                searchInterval.current = setTimeout(() => {
                  setQuery(val);
                }, 500);
              }}
              placeholder="Start typing a player name..."
            />
          </Col>
          <Col>
            <DownloadButton
              type="button"
              onClick={() => {
                handleCSVCall({
                  page,
                  sortBy: sort?.sortBy,
                  sortOrder: sort?.sortOrder,
                  query,
                });
              }}
            >
              Download
            </DownloadButton>
          </Col>
        </Row>
        <Row style={{ marginTop: 15 }}>
          <Col style={{ display: 'flex' }}>
            <p style={{ paddingRight: 15 }}>Results per page</p>
            <select
              onChange={e => {
                const val = e.target.value;
                setPageSize(val.length > 0 ? val : undefined);
              }}
            >
              <option value="10">10</option>
              <option value="25">25</option>
              <option value="100">100</option>
              <option value="15000">15K</option>
            </select>
          </Col>
        </Row>
      </div>
      <div style={{ padding: 25, paddingTop: 0 }}>
        <Row style={{ marginTop: 5 }}>
          <Col>
            <RushingStatsTable
              players={results?.results}
              sort={sort}
              setSort={setSort}
            />
          </Col>
        </Row>
        <Row style={{ marginTop: 25 }}>
          <Col>
            <ReactPaginate
              nextLabel="next >"
              onPageChange={handlePageChange}
              pageRangeDisplayed={2}
              marginPagesDisplayed={1}
              pageCount={results?.pages || 0}
              previousLabel="< previous"
              pageClassName="page-item"
              pageLinkClassName="page-link"
              previousClassName="page-item"
              previousLinkClassName="page-link"
              nextClassName="page-item"
              nextLinkClassName="page-link"
              breakLabel="..."
              breakClassName="page-item"
              breakLinkClassName="page-link"
              containerClassName="pagination"
              activeClassName="active"
              renderOnZeroPageCount={null}
            />
          </Col>
        </Row>
      </div>
    </div>
  );
};

export default RushingStatsPage;
