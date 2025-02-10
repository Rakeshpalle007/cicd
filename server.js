'use strict';

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World, we are from the devops engineers working on the docker,and kubernaties.');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
