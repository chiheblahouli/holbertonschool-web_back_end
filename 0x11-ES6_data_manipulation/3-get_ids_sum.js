export default function getStudentIdsSum(obj) {
  if ((Array.isArray(obj))) return obj.reduce((init, val) => init + val.id, 0);

  return 0;
}
