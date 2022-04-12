import getNeighborhoodsList from './2-arrow.js';

const neighborhoodsList = new getNeighborhoodsList();
console.log(neighborhoodsList.sanFranciscoNeighborhoods);
const res = neighborhoodsList.addNeighborhood('Noe Valley');
console.log(res);
