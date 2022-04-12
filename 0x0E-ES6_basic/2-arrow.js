export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  this.addNeighborhood = (f) => {
    this.sanFranciscoNeighborhoods.push(f);
    return this.sanFranciscoNeighborhoods;
  };
}
