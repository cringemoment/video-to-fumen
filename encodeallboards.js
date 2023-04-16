const fs = require('fs');
const { encoder, Field } = require('tetris-fumen');

const pages = [];

// Read the file line by line
const fileContents = fs.readFileSync('allboards.txt', 'utf-8');
const lines = fileContents.split('\n');

// Iterate through each line and add the field to pages
for (const line of lines) {
  if (line.trim() !== '') {
    // Create a field object from the line
    const field = Field.create(line.trim());
    // Add the field object to the pages array
    pages.push({ field });
  }
}

// Encode the pages array into a fumen
const fumen = encoder.encode(pages);

console.log(fumen);
