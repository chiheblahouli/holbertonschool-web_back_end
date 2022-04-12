export default function getStudentsByLocation(obj, elemnt) {
  if ((Array.isArray(obj))) return obj.filter((val) => val.location === elemnt);

  return [];
}
