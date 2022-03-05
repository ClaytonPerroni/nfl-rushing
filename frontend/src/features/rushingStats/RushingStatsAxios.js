/* eslint-disable */
import axios from 'axios';

const BASE_SEARCH_URL = 'http://localhost:2001/rushing-stats/';

export const handleSearchCall = async ({ page, sortBy, sortOrder, query }) => {
  const getQueryParams = () => {
    const obj = {};
    if (sortBy) obj.order_by = sortBy;
    if (sortOrder) obj.order_direction = sortOrder;
    if (query.length > 0) obj.query = query;
    return obj;
  };

  try {
    const response = await axios.get(BASE_SEARCH_URL, {
      params: {
        page: page,
        page_size: 10,
        ...getQueryParams(),
      },
    });
    return response.data;
  } catch {
    return {};
  }
};

export const handleCSVCall = async ({ page, sortBy, sortOrder, query }) => {
  const getQueryParams = () => {
    const obj = {};
    if (sortBy) obj.order_by = sortBy;
    if (sortOrder) obj.order_direction = sortOrder;
    if (query.length > 0) obj.query = query;
    return obj;
  };

  try {
    const response = await axios.get(BASE_SEARCH_URL + 'csv', {
      params: {
        page: page,
        page_size: 10,
        ...getQueryParams(),
      },
    });
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'results.csv'); //or any other extension
    document.body.appendChild(link);
    link.click();
    return response.data;
  } catch {
    return {};
  }
};
