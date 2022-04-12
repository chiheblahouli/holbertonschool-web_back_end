export default function getListStudentIds(arr) {
  let rslt = [];
  try {
    rslt = arr.map((obj) => obj.id);
  } catch (e) {
    // pass
  }
  return rslt;
}
