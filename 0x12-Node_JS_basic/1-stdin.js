const f = require('readline').createInterface({
  input: process.stdin,
});

process.stdout.write('Welcome to Holberton School, what is your name?\n');
f.question('readable', (name) => {
  if (name) process.stdout.write(`Your name is: ${name}\n`);
  if (!process.stdin.isTTY) {
    process.stdout.write('This important software is now closing\n');
  }
  f.close();
});
