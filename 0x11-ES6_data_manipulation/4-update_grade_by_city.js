export default function updateStudentGradeByCity(obj, city, newGrades) {
  if ((Array.isArray(obj))) {
    return obj.filter((val) => val.location === city).map((f) => {
      const j = f;
      for (const i of newGrades) {
        if (i.studentId === f.id) {
          j.grade = i.grade;
        } else j.grade = 'N/A';
      }
      return j;
    });
  }
  return [];
}
