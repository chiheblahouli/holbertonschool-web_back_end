const fs = require('fs');

async function countStudents(fp) {
  try {
    const myfile = await fs.promises.readFile(fp, { encoding: 'utf8' });
    const arr = myfile.trim().split('\n');
    const fields = {};
    const lis = {};
    /* eslint-disable */

        for (let i = 1; i < arr.length; i += 1) {
            const f = arr[i].split(',');
            const m = f[f.length - 1];
            if (fields[m] == null) fields[m] = 0;
            fields[m] = fields[m] + 1;
            if (lis[m] == null) lis[m] = [];
            lis[m].push(f[0]);
        }
        console.log(`Number of students: ${myfile.trim().split('\n').length - 1}`);
        Object.keys(fields).map((key) => {
            console.log(`Number of students in ${key}: ${fields[key]}. List: ${lis[key].toString().split(',').join(', ')}`);
        });
    } catch (err) {
        throw new Error('Cannot load the database');
        //console.log(err)
    }
}
module.exports = countStudents;