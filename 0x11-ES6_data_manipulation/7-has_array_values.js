export default function hasValuesFromArray(set, array) {
  return array.every((f) => set.has(f));
}
